# Manual Fixes Guide for index.html

If you prefer to make changes manually in VS Code, follow this guide. Use Find & Replace (Ctrl+H) for each section.

## 1. Hero Section Updates

### 1.1 Update Hero Tag
**Find:** `INSTITUTIONAL-GRADE INTELLIGENCE`
**Replace:** `PROFESSIONAL MARKET INTELLIGENCE`

### 1.2 Update Hero Title
**Find:** `Trade Like the<br><em>Smart Money</em> Does`
**Replace:** `Trade Like the<br><em>Professional</em> Does`

### 1.3 Update Hero Subtext
**Find:** `Automated Order Block mapping, FVG detection, real-time signals across 60+ instruments, and AI chart analysis — all in one platform. Free forever.`
**Replace:** `Turn complex charts into effortless trading experience.`

### 1.4 Update Parallax Opacity
**Find:** `if (content) content.style.opacity = 1 - sy / 500;`
**Replace:** `if (content) content.style.opacity = Math.max(0.8, 1 - sy / 800);`

### 1.5 Hide Spline Watermark
**Find:** `#spline-bg{position:absolute;inset:0;z-index:0;width:100%;height:100%;border:none;pointer-events:none}`
**Replace:** `#spline-bg{position:absolute;inset:0;z-index:0;width:115%;height:115%;top:-7.5%;left:-7.5%;border:none;pointer-events:none}`

---

## 2. Feature Cards Updates

### 2.1 Smart Money → Market Structure
**Find:** `Smart Money Mapping`
**Replace:** `Market Structure Mapping`

### 2.2 Order Block Description
**Find:** `Automated Order Block detection, Fair Value Gaps, Premium/Discount zones and liquidity sweeps across all timeframes.`
**Replace:** `Automated support/resistance detection, price action zones, premium/discount zones and liquidity sweeps across all timeframes.`

### 2.3 Unicorn Models → High-Confidence
**Find:** `Scan all 60+ instruments simultaneously. Unicorn models and high-confidence setups surface automatically in seconds.`
**Replace:** `Scan all 60+ instruments simultaneously. High-confidence setups surface automatically in seconds.`

### 2.4 R:R → Risk-Reward
**Find:** `Upload any chart screenshot and receive instant AI-powered structure assessment, entry zones, and R:R calculations.`
**Replace:** `Upload any chart screenshot and receive instant AI-powered structure assessment, entry zones, and risk-reward calculations.`

### 2.5 Telegram Alerts
**Find:** `Live push notifications for Unicorn models, killzone activations, and high-confidence signals — straight to your phone.`
**Replace:** `Live push notifications for high-confidence signals — straight to your phone.`

### 2.6 R:R Distribution
**Find:** `Auto-log signals, track win rate, session performance, and R:R distribution.`
**Replace:** `Auto-log signals, track win rate, session performance, and risk-reward distribution.`

### 2.7 Killzone → Session Intelligence
**Find:** `Killzone Intelligence`
**Replace:** `Session Intelligence`

### 2.8 Session Description
**Find:** `Live session tracking, AMD phase detection, Silver Bullet windows, and SMT divergence alerts — all automated.`
**Replace:** `Live session tracking, market phase detection, volatility windows, and divergence alerts — all automated.`

### 2.9 Feature Tag
**Find:** `<span class="feat-tag">ICT CONCEPTS</span>`
**Replace:** `<span class="feat-tag">PROFESSIONAL ANALYSIS</span>`

---

## 3. Preview Section Updates

### 3.1 TradingView Overlays
**Find:** `Live TradingView charts with custom ICT overlays`
**Replace:** `Live TradingView charts with professional analysis overlays`

### 3.2 Order Block Visualization
**Find:** `Real-time Order Block and FVG visualization`
**Replace:** `Real-time support/resistance and price action zone visualization`

### 3.3 Liquidity Map
**Find:** `Liquidity map with BSL/SSL levels`
**Replace:** `Liquidity map with key level markers`

---

## 4. Terminal Mockup Updates

### 4.1 Silver Bullet Panel
**Find:** `<div class="tm-ptitle">SILVER BULLET</div>`
**Replace:** `<div class="tm-ptitle">MARKET STATUS</div>`

### 4.2 SMT Panel
**Find:** `<div class="tm-ptitle">SMT</div>`
**Replace:** `<div class="tm-ptitle">DIVERGENCE</div>`

### 4.3 SMT Divergence Alerts (EURUSD)
**Find:** `SMT Divergence on EURUSD: Bullish SMT`
**Replace:** `Divergence on EURUSD: Bullish Divergence`

### 4.4 SMT Divergence Alerts (US30)
**Find:** `SMT Divergence on US30: Bullish SMT`
**Replace:** `Divergence on US30: Bullish Divergence`

### 4.5 Unicorn Model Alerts
**Find:** `Unicorn Model detected`
**Replace:** `High-Confidence Signal`

### 4.6 Stats Label
**Find:** `<div class="tm-stat-lbl">OBs / FVGs</div>`
**Replace:** `<div class="tm-stat-lbl">Key Levels</div>`

---

## 5. How It Works Section

### 5.1 Analyze Step
**Find:** `A3-Elite maps structure, Order Blocks, FVGs, killzones, AMD phases and SMT divergence automatically — no manual work.`
**Replace:** `A3-Elite maps structure, support/resistance zones, price action patterns, market phases and divergence alerts automatically — no manual work.`

### 5.2 Signal Step
**Find:** `Receive a classified signal (Unicorn / A3-Elite / Alt) with entry, stop, target and confidence rating.`
**Replace:** `Receive a high-confidence signal with entry, stop, target and confidence rating.`

---

## 6. Testimonials Updates

### 6.1 First Testimonial
**Find:** `The Order Block detection alone saved me hours of manual analysis. I went from 40% to 68% win rate in 6 weeks using the Unicorn signals.`
**Replace:** `The support/resistance detection alone saved me hours of manual analysis. I went from 40% to 68% win rate in 6 weeks using the high-confidence signals.`

### 6.2 Third Testimonial
**Find:** `The Telegram alerts during London killzone are insane.`
**Replace:** `The Telegram alerts during London session are insane.`

---

## 7. Pricing Section

### 7.1 Plan Features
**Find:** `Order Block & FVG detection`
**Replace:** `Support/resistance & price action zone detection`

### 7.2 Pro Plan Features
**Find:** `Unicorn model alerts`
**Replace:** `High-confidence signal alerts`

---

## 8. Footer Updates

### 8.1 Footer Brand Description
**Find:** `Built on Smart Money concepts.`
**Replace:** `Built on professional market analysis concepts.`

### 8.2 Add Sign Up Link to Footer
**Find:** `<h4>COMPANY</h4>` section, after `<a href="#">Blog</a>`
**Add:** `<a href="signup.html">Sign Up</a>`

---

## 9. CTA Section

### 9.1 CTA Title
**Find:** `Ready to trade like<br><em>Smart Money</em>?`
**Replace:** `Ready to trade like<br><em>Professional</em>?`

---

## 10. Why Section

### 10.1 Section Description
**Find:** `Built on institutional Smart Money concepts — the same tools used by hedge funds and prop desks, now accessible to every trader.`
**Replace:** `Built on professional market analysis concepts — the same tools used by hedge funds and prop desks, now accessible to every trader.`

---

## 11. Signup Modal - Remove Prices

### 11.1 Free Plan
**Find:** `<div class="auth-plan selected" data-plan="free" onclick="selectPlan('free')"><div class="auth-plan-name">FREE</div><div class="auth-plan-price">€0<span>/mo</span></div></div>`
**Replace:** `<div class="auth-plan selected" data-plan="free" onclick="selectPlan('free')"><div class="auth-plan-name">FREE</div></div>`

### 11.2 Pro Plan
**Find:** `<div class="auth-plan" data-plan="pro" onclick="selectPlan('pro')"><div class="auth-plan-name">PRO</div><div class="auth-plan-price">€12<span>/mo</span></div></div>`
**Replace:** `<div class="auth-plan" data-plan="pro" onclick="selectPlan('pro')"><div class="auth-plan-name">PRO</div></div>`

### 11.3 Business Plan
**Find:** `<div class="auth-plan" data-plan="business" onclick="selectPlan('business')"><div class="auth-plan-name">BIZ</div><div class="auth-plan-price">€39<span>/mo</span></div></div>`
**Replace:** `<div class="auth-plan" data-plan="business" onclick="selectPlan('business')"><div class="auth-plan-name">BIZ</div></div>`

---

## 12. Login Modal - Add Forgot Password & OAuth

### 12.1 Replace Entire Login Modal
**Find:** The entire `<div id="auth-login" style="display:none">` block (from opening to closing `</div>`)

**Replace with:**
```html
    <div id="auth-login" style="display:none">
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
    </div>
```

---

## 13. Add CSS for OAuth & Forgot Password

### 13.1 Find and Update Auth Switch CSS
**Find:** 
```css
.auth-switch{text-align:center;margin-top:18px;font-size:14px;color:var(--text2)}
.auth-switch a{color:var(--accent);cursor:pointer;text-decoration:underline}
```

**Replace with:**
```css
.auth-switch{text-align:center;margin-top:18px;font-size:14px;color:var(--text2)}
.auth-switch a{color:var(--accent);cursor:pointer;text-decoration:underline}
.auth-or{display:flex;align-items:center;gap:12px;margin:20px 0}
.or-line{flex:1;height:1px;background:var(--border)}
.or-text{font-size:11px;color:var(--text3);font-family:var(--mono);letter-spacing:1px;white-space:nowrap}
.auth-oauth{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin-bottom:4px}
.oauth-btn{display:flex;align-items:center;justify-content:center;gap:6px;background:var(--bg3);border:1px solid var(--border2);color:var(--text);padding:10px 8px;border-radius:6px;font-size:12px;font-weight:600;cursor:pointer;transition:all .2s;font-family:var(--font)}
.oauth-btn:hover{border-color:var(--accent);background:rgba(0,255,178,0.05);transform:translateY(-1px)}
```

---

## 14. Add JavaScript Functions

### 14.1 Find the showErr Function
**Find:** `function showErr(el, msg) { el.textContent = msg; el.style.display = 'block'; }`

### 14.2 Add After showErr Function
**Add the following code right after the showErr function:**

```javascript

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
}
```

---

## Summary

**Total Changes:** 19 sections
- 5 Hero section updates
- 8 Feature card updates
- 3 Preview section updates
- 6 Terminal mockup updates
- 2 How it works updates
- 2 Testimonial updates
- 2 Pricing updates
- 1 Footer update
- 1 CTA update
- 1 Why section update
- 3 Signup modal price removals
- 1 Login modal replacement
- 1 CSS addition
- 1 JavaScript addition

**Recommended Approach:**
1. Use Find & Replace (Ctrl+H) for sections 1-11
2. Manually replace the login modal (section 12)
3. Manually update CSS (section 13)
4. Manually add JavaScript functions (section 14)

All changes maintain UTF-8 encoding and clean formatting.
