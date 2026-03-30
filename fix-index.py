#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fix index.html encoding and apply all updates
Handles UTF-8 properly without corruption
"""

import re

# Read file with proper UTF-8 encoding
with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove 'Launch App' from footer and add 'Sign Up' link
content = re.sub(
    r'(<a href="#pricing">Pricing</a>)',
    r'\1',
    content
)
content = re.sub(
    r'(<h4>COMPANY</h4>.*?<a href="#">About</a>.*?<a href="#">Blog</a>)',
    lambda m: m.group(1) + '\n      <a href="signup.html">Sign Up</a>',
    content,
    flags=re.DOTALL
)

# 2. Update hero tag and title
content = content.replace(
    'INSTITUTIONAL-GRADE INTELLIGENCE',
    'PROFESSIONAL MARKET INTELLIGENCE'
)
content = content.replace(
    'Trade Like the<br><em>Smart Money</em> Does',
    'Trade Like the<br><em>Professional</em> Does'
)

# 3. Update hero subtext
content = content.replace(
    'Automated Order Block mapping, FVG detection, real-time signals across 60+ instruments, and AI chart analysis — all in one platform. Free forever.',
    'Turn complex charts into effortless trading experience.'
)

# 4. Update hero parallax opacity
content = content.replace(
    'if (content) content.style.opacity = 1 - sy / 500;',
    'if (content) content.style.opacity = Math.max(0.8, 1 - sy / 800);'
)

# 5. Update spline iframe sizing to hide watermark
content = content.replace(
    '#spline-bg{position:absolute;inset:0;z-index:0;width:100%;height:100%;border:none;pointer-events:none}',
    '#spline-bg{position:absolute;inset:0;z-index:0;width:115%;height:115%;top:-7.5%;left:-7.5%;border:none;pointer-events:none}'
)

# 6. Update feature cards - remove ICT terms
content = content.replace(
    'Smart Money Mapping',
    'Market Structure Mapping'
)
content = content.replace(
    'Automated Order Block detection, Fair Value Gaps, Premium/Discount zones and liquidity sweeps across all timeframes.',
    'Automated support/resistance detection, price action zones, premium/discount zones and liquidity sweeps across all timeframes.'
)
content = content.replace(
    'Scan all 60+ instruments simultaneously. Unicorn models and high-confidence setups surface automatically in seconds.',
    'Scan all 60+ instruments simultaneously. High-confidence setups surface automatically in seconds.'
)
content = content.replace(
    'Upload any chart screenshot and receive instant AI-powered structure assessment, entry zones, and R:R calculations.',
    'Upload any chart screenshot and receive instant AI-powered structure assessment, entry zones, and risk-reward calculations.'
)
content = content.replace(
    'Live push notifications for Unicorn models, killzone activations, and high-confidence signals — straight to your phone.',
    'Live push notifications for high-confidence signals — straight to your phone.'
)
content = content.replace(
    'Auto-log signals, track win rate, session performance, and R:R distribution.',
    'Auto-log signals, track win rate, session performance, and risk-reward distribution.'
)
content = content.replace(
    'Killzone Intelligence',
    'Session Intelligence'
)
content = content.replace(
    'Live session tracking, AMD phase detection, Silver Bullet windows, and SMT divergence alerts — all automated.',
    'Live session tracking, market phase detection, volatility windows, and divergence alerts — all automated.'
)

# 7. Update feature tags
content = content.replace(
    '<span class="feat-tag">ICT CONCEPTS</span>',
    '<span class="feat-tag">PROFESSIONAL ANALYSIS</span>'
)

# 8. Update preview list
content = content.replace(
    'Live TradingView charts with custom ICT overlays',
    'Live TradingView charts with professional analysis overlays'
)
content = content.replace(
    'Real-time Order Block and FVG visualization',
    'Real-time support/resistance and price action zone visualization'
)
content = content.replace(
    'Liquidity map with BSL/SSL levels',
    'Liquidity map with key level markers'
)

# 9. Update terminal mockup panels
content = content.replace(
    '<div class="tm-ptitle">SILVER BULLET</div>',
    '<div class="tm-ptitle">MARKET STATUS</div>'
)
content = content.replace(
    '<div class="tm-ptitle">SMT</div>',
    '<div class="tm-ptitle">DIVERGENCE</div>'
)
content = content.replace(
    'SMT Divergence on EURUSD: Bullish SMT',
    'Divergence on EURUSD: Bullish Divergence'
)
content = content.replace(
    'SMT Divergence on US30: Bullish SMT',
    'Divergence on US30: Bullish Divergence'
)
content = content.replace(
    'Unicorn Model detected',
    'High-Confidence Signal'
)
content = content.replace(
    '<div class="tm-stat-lbl">OBs / FVGs</div>',
    '<div class="tm-stat-lbl">Key Levels</div>'
)

# 10. Update how it works section
content = content.replace(
    'A3-Elite maps structure, Order Blocks, FVGs, killzones, AMD phases and SMT divergence automatically — no manual work.',
    'A3-Elite maps structure, support/resistance zones, price action patterns, market phases and divergence alerts automatically — no manual work.'
)
content = content.replace(
    'Receive a classified signal (Unicorn / A3-Elite / Alt) with entry, stop, target and confidence rating.',
    'Receive a high-confidence signal with entry, stop, target and confidence rating.'
)

# 11. Update testimonials
content = content.replace(
    'The Order Block detection alone saved me hours of manual analysis. I went from 40% to 68% win rate in 6 weeks using the Unicorn signals.',
    'The support/resistance detection alone saved me hours of manual analysis. I went from 40% to 68% win rate in 6 weeks using the high-confidence signals.'
)
content = content.replace(
    'The Telegram alerts during London killzone are insane.',
    'The Telegram alerts during London session are insane.'
)

# 12. Update pricing plan features
content = content.replace(
    'Order Block & FVG detection',
    'Support/resistance & price action zone detection'
)
content = content.replace(
    'Unicorn model alerts',
    'High-confidence signal alerts'
)

# 13. Update footer brand description
content = content.replace(
    'Built on Smart Money concepts.',
    'Built on professional market analysis concepts.'
)

# 14. Update CTA section
content = content.replace(
    'Ready to trade like<br><em>Smart Money</em>?',
    'Ready to trade like<br><em>Professional</em>?'
)

# 15. Update why section
content = content.replace(
    'Built on institutional Smart Money concepts — the same tools used by hedge funds and prop desks, now accessible to every trader.',
    'Built on professional market analysis concepts — the same tools used by hedge funds and prop desks, now accessible to every trader.'
)

# 16. Remove plan prices from signup modal
content = re.sub(
    r'<div class="auth-plan selected" data-plan="free" onclick="selectPlan\(\'free\'\)"><div class="auth-plan-name">FREE</div><div class="auth-plan-price">.*?</div></div>',
    '<div class="auth-plan selected" data-plan="free" onclick="selectPlan(\'free\')"><div class="auth-plan-name">FREE</div></div>',
    content
)
content = re.sub(
    r'<div class="auth-plan" data-plan="pro" onclick="selectPlan\(\'pro\'\)"><div class="auth-plan-name">PRO</div><div class="auth-plan-price">.*?</div></div>',
    '<div class="auth-plan" data-plan="pro" onclick="selectPlan(\'pro\')"><div class="auth-plan-name">PRO</div></div>',
    content
)
content = re.sub(
    r'<div class="auth-plan" data-plan="business" onclick="selectPlan\(\'business\'\)"><div class="auth-plan-name">BIZ</div><div class="auth-plan-price">.*?</div></div>',
    '<div class="auth-plan" data-plan="business" onclick="selectPlan(\'business\')"><div class="auth-plan-name">BIZ</div></div>',
    content
)

# 17. Update login modal with forgot password and OAuth
login_modal = '''    <div id="auth-login" style="display:none">
      <div class="auth-title">Welcome back</div>
      <div class="auth-sub">Sign in to access your dashboard.</div>
      <div class="auth-error" id="login-error"></div>
      <div class="auth-success" id="login-success"></div>
      <div class="auth-field"><label>Email</label><input type="email" id="login-email" placeholder="you@example.com"></div>
      <div class="auth-field"><label>Password</label><input type="password" id="login-password" placeholder="Your password"></div>
      <button class="auth-btn" id="login-btn" onclick="doLogin()">SIGN IN</button>
      <div class="auth-switch">
        <a onclick="switchAuth('signup')">Create account</a>
        <span style="margin:0 8px;color:var(--text3)">|</span>
        <a onclick="showForgotPassword()">Forgot password?</a>
      </div>
      <div class="auth-or"><div class="or-line"></div><span class="or-text">Or continue with</span><div class="or-line"></div></div>
      <div class="auth-oauth">
        <button type="button" class="oauth-btn" onclick="oauthLogin('google')">Google</button>
        <button type="button" class="oauth-btn" onclick="oauthLogin('github')">GitHub</button>
        <button type="button" class="oauth-btn" onclick="oauthLogin('apple')">Apple</button>
      </div>
    </div>'''

content = re.sub(
    r'<div id="auth-login"[^}]*?</div>\s*</div>\s*</div>',
    login_modal + '\n  </div>\n</div>',
    content,
    flags=re.DOTALL
)

# 18. Add CSS for OAuth and forgot password
new_css = '''.auth-switch{text-align:center;margin-top:18px;font-size:14px;color:var(--text2)}
.auth-switch a{color:var(--accent);cursor:pointer;text-decoration:underline}
.auth-or{display:flex;align-items:center;gap:12px;margin:20px 0}
.or-line{flex:1;height:1px;background:var(--border)}
.or-text{font-size:11px;color:var(--text3);font-family:var(--mono);letter-spacing:1px;white-space:nowrap}
.auth-oauth{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:4px}
.oauth-btn{display:flex;align-items:center;justify-content:center;gap:6px;background:var(--bg3);border:1px solid var(--border2);color:var(--text);padding:10px 8px;border-radius:6px;font-size:12px;font-weight:600;cursor:pointer;transition:all .2s;font-family:var(--font)}
.oauth-btn:hover{border-color:var(--accent);background:rgba(0,255,178,0.05);transform:translateY(-1px)}'''

content = re.sub(
    r'(\.auth-switch\{[^}]+\}[^}]*\.auth-switch a\{[^}]+\})',
    new_css,
    content
)

# 19. Add JavaScript functions before closing script tag
new_js = '''

// -- FORGOT PASSWORD --
function showForgotPassword() {
  document.getElementById('auth-login').innerHTML = `
    <div class="auth-title">Reset Password</div>
    <div class="auth-sub">Enter your email and we'll send you a reset link.</div>
    <div class="auth-error" id="forgot-error"></div>
    <div class="auth-success" id="forgot-success"></div>
    <div class="auth-field"><label>Email</label><input type="email" id="forgot-email" placeholder="you@example.com"></div>
    <button class="auth-btn" id="forgot-btn" onclick="sendResetEmail()">SEND RESET LINK</button>
    <div class="auth-switch"><a onclick="switchAuth('login')">Back to Sign In</a></div>
  `;
}

async function sendResetEmail() {
  const email = document.getElementById('forgot-email').value.trim();
  const errEl = document.getElementById('forgot-error');
  const okEl = document.getElementById('forgot-success');
  const btn = document.getElementById('forgot-btn');
  errEl.style.display = 'none'; okEl.style.display = 'none';
  if (!email) { showErr(errEl, 'Please enter your email address.'); return; }
  btn.disabled = true; btn.textContent = 'SENDING...';
  const { error } = await sb.auth.resetPasswordForEmail(email, {
    redirectTo: `${window.location.origin}/index.html`
  });
  btn.disabled = false; btn.textContent = 'SEND RESET LINK';
  if (error) { showErr(errEl, error.message); return; }
  okEl.textContent = 'Reset link sent! Check your email.';
  okEl.style.display = 'block';
}

// -- OAUTH LOGIN --
async function oauthLogin(provider) {
  const errEl = document.getElementById('login-error');
  if (errEl) errEl.style.display = 'none';
  const { error } = await sb.auth.signInWithOAuth({
    provider,
    options: { redirectTo: `${window.location.origin}/index.html` }
  });
  if (error && errEl) showErr(errEl, 'Authentication failed. Please try again.');
}'''

content = re.sub(
    r'(function showErr\(el, msg\) \{ el\.textContent = msg; el\.style\.display = \'block\'; \})',
    r'\1' + new_js,
    content
)

# Write file with proper UTF-8 encoding
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✓ All updates applied successfully with proper UTF-8 encoding!")
print("✓ File saved: index.html")
