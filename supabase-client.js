// ============================================================================
// A3-Elite — Supabase Client
// Handles auth state, journal, alerts, settings, and telegram config
// Falls back to localStorage when user is not signed in
// ============================================================================

const SUPABASE_URL = 'https://rvjelddscvscsixvkngr.supabase.co';
const SUPABASE_KEY = 'sb_publishable_L7zt01EEtWgU6pvo0gqQmw_e_v9Gwn-';
const _sb = supabase.createClient(SUPABASE_URL, SUPABASE_KEY);

let _currentUser = null;

// ── AUTH ─────────────────────────────────────────────────────────────────────

_sb.auth.onAuthStateChange((event, session) => {
  _currentUser = session?.user || null;
  updateNavAuthUI(session);
  if (event === 'SIGNED_IN') {
    // Sync localStorage data to Supabase on first login
    _migrateLocalData();
  }
});

async function _getUser() {
  if (_currentUser) return _currentUser;
  const { data } = await _sb.auth.getUser();
  _currentUser = data?.user || null;
  return _currentUser;
}

function updateNavAuthUI(session) {
  const area = document.getElementById('nav-auth-area');
  if (!area) return;
  if (session) {
    const name = session.user.user_metadata?.full_name || session.user.email;
    const plan = session.user.user_metadata?.plan || 'free';
    area.innerHTML = `
      <div style="display:flex;align-items:center;gap:10px;font-size:12px">
        <span style="font-family:var(--mono);color:var(--accent)">${name.split(' ')[0].toUpperCase()}</span>
        <span style="font-size:10px;padding:2px 7px;border-radius:2px;background:rgba(14,165,233,.15);color:var(--accent2);font-family:var(--mono)">${plan.toUpperCase()}</span>
        <button onclick="sbSignOut()" style="background:none;border:1px solid var(--border2);color:var(--text2);padding:4px 10px;border-radius:3px;font-size:11px;cursor:pointer">SIGN OUT</button>
      </div>`;
  } else {
    area.innerHTML = `<button onclick="window.location.href='index.html'" style="background:var(--accent);color:#000;border:none;padding:5px 14px;font-family:var(--font);font-size:13px;font-weight:700;letter-spacing:1px;cursor:pointer;border-radius:3px">SIGN IN</button>`;
  }
}

async function sbSignOut() {
  await _sb.auth.signOut();
  _currentUser = null;
  window.location.href = 'index.html';
}

// ── MIGRATE localStorage → Supabase on first login ───────────────────────────

async function _migrateLocalData() {
  const user = await _getUser();
  if (!user) return;

  // Migrate journal
  const localJournal = JSON.parse(localStorage.getItem('a3journal') || '[]');
  if (localJournal.length) {
    const rows = localJournal.map(t => ({
      user_id: user.id,
      symbol: t.sym,
      direction: t.dir,
      entry: t.entry,
      stop_loss: t.sl,
      take_profit: t.tp,
      lot_size: t.lot || 0.1,
      status: (t.status || 'OPEN').toLowerCase(),
      notes: t.notes || '',
      pnl: t.exit ? ((t.dir === 'LONG' ? t.exit - t.entry : t.entry - t.exit) / t.entry * 100 * (t.lot || 0.1)) : null,
      opened_at: new Date(t.date).toISOString(),
      closed_at: t.exit ? new Date(t.date).toISOString() : null
    }));
    await _sb.from('trades').upsert(rows, { onConflict: 'id', ignoreDuplicates: true });
    localStorage.removeItem('a3journal');
  }

  // Migrate settings
  const localSettings = JSON.parse(localStorage.getItem('a3settings') || 'null');
  if (localSettings) {
    await _sb.from('profiles').update({ settings: localSettings }).eq('id', user.id);
    localStorage.removeItem('a3settings');
  }

  // Migrate telegram config
  const localTg = JSON.parse(localStorage.getItem('a3telegram') || 'null');
  if (localTg) {
    await _sb.from('profiles').update({
      telegram_bot_token: localTg.botToken || '',
      telegram_chat_id: localTg.chatId || '',
      telegram_connected: localTg.connected || false,
      settings: { ...(localSettings || {}), telegramAlertTypes: localTg.alertTypes }
    }).eq('id', user.id);
    localStorage.removeItem('a3telegram');
  }
}

// ── JOURNAL ──────────────────────────────────────────────────────────────────

async function sbLoadJournal() {
  const user = await _getUser();
  if (!user) return JSON.parse(localStorage.getItem('a3journal') || '[]');

  const { data, error } = await _sb.from('trades')
    .select('*')
    .eq('user_id', user.id)
    .order('opened_at', { ascending: false });

  if (error) return JSON.parse(localStorage.getItem('a3journal') || '[]');

  // Map DB rows → app format
  return (data || []).map(r => ({
    _id: r.id,
    date: new Date(r.opened_at).getTime(),
    sym: r.symbol,
    dir: r.direction,
    entry: r.entry,
    sl: r.stop_loss,
    tp: r.take_profit,
    lot: r.lot_size,
    exit: r.pnl != null ? r.take_profit : null, // approximate
    status: r.status.toUpperCase(),
    notes: r.notes,
    review: r.notes
  }));
}

async function sbSaveTrade(trade) {
  const user = await _getUser();
  if (!user) {
    const j = JSON.parse(localStorage.getItem('a3journal') || '[]');
    j.push(trade);
    localStorage.setItem('a3journal', JSON.stringify(j));
    return null;
  }

  const { data, error } = await _sb.from('trades').insert({
    user_id: user.id,
    symbol: trade.sym,
    direction: trade.dir,
    entry: trade.entry,
    stop_loss: trade.sl,
    take_profit: trade.tp,
    lot_size: trade.lot || 0.1,
    status: (trade.status || 'open').toLowerCase(),
    notes: trade.notes || '',
    opened_at: new Date(trade.date).toISOString()
  }).select().single();

  if (error) console.error('sbSaveTrade:', error);
  return data;
}

async function sbUpdateTrade(id, updates) {
  const user = await _getUser();
  if (!user) return;

  const dbUpdates = {};
  if (updates.status !== undefined) dbUpdates.status = updates.status.toLowerCase();
  if (updates.exit !== undefined) {
    dbUpdates.closed_at = updates.exit ? new Date().toISOString() : null;
  }
  if (updates.review !== undefined) dbUpdates.notes = updates.review;

  const { error } = await _sb.from('trades').update(dbUpdates).eq('id', id).eq('user_id', user.id);
  if (error) console.error('sbUpdateTrade:', error);
}

// ── ALERTS ───────────────────────────────────────────────────────────────────

async function sbLoadAlerts() {
  const user = await _getUser();
  if (!user) return JSON.parse(localStorage.getItem('a3alerts') || '[]');

  const { data } = await _sb.from('alerts')
    .select('*')
    .eq('user_id', user.id)
    .order('created_at', { ascending: false })
    .limit(20);

  return (data || []).map(r => ({
    _id: r.id,
    msg: r.message,
    type: r.type,
    sym: r.symbol,
    ts: new Date(r.created_at).getTime()
  }));
}

async function sbSaveAlert(alert) {
  const user = await _getUser();
  if (!user) return;

  await _sb.from('alerts').insert({
    user_id: user.id,
    type: alert.type,
    message: alert.msg,
    symbol: alert.sym || null
  });
}

async function sbDeleteAlert(id) {
  const user = await _getUser();
  if (!user) return;
  await _sb.from('alerts').delete().eq('id', id).eq('user_id', user.id);
}

// ── SETTINGS ─────────────────────────────────────────────────────────────────

async function sbLoadSettings() {
  const user = await _getUser();
  if (!user) return JSON.parse(localStorage.getItem('a3settings') || 'null');

  const { data } = await _sb.from('profiles').select('settings').eq('id', user.id).single();
  return data?.settings || null;
}

async function sbSaveSettings(settings) {
  const user = await _getUser();
  if (!user) {
    localStorage.setItem('a3settings', JSON.stringify(settings));
    return;
  }
  await _sb.from('profiles').update({ settings }).eq('id', user.id);
}

// ── TELEGRAM CONFIG ───────────────────────────────────────────────────────────

async function sbLoadTelegramConfig() {
  const user = await _getUser();
  if (!user) return JSON.parse(localStorage.getItem('a3telegram') || 'null');

  const { data } = await _sb.from('profiles')
    .select('telegram_bot_token, telegram_chat_id, telegram_connected, settings')
    .eq('id', user.id).single();

  if (!data) return null;
  return {
    botToken: data.telegram_bot_token || '',
    chatId: data.telegram_chat_id || '',
    connected: data.telegram_connected || false,
    alertTypes: data.settings?.telegramAlertTypes || { unicorn: true, highconf: true, killzone: true, smt: false, news: false }
  };
}

async function sbSaveTelegramConfig(cfg) {
  const user = await _getUser();
  if (!user) {
    localStorage.setItem('a3telegram', JSON.stringify(cfg));
    return;
  }
  // Load existing settings to merge
  const { data } = await _sb.from('profiles').select('settings').eq('id', user.id).single();
  const existingSettings = data?.settings || {};

  await _sb.from('profiles').update({
    telegram_bot_token: cfg.botToken,
    telegram_chat_id: cfg.chatId,
    telegram_connected: cfg.connected,
    settings: { ...existingSettings, telegramAlertTypes: cfg.alertTypes }
  }).eq('id', user.id);
}
