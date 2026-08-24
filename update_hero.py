import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS variables for Day/Night Mode
css_insert = '''
    :root {
      --bg:          #f0f6ff;
      --bg2:         #e8f0fa;
      --bg-card:     #ffffff;
      --blue:        #0099ff;
      --blue-l:      #0284c7;
      --blue-d:      #0369a1;
      --cyan:        #06b6d4;
      --gold:        #f59e0b;
      --white:       #ffffff;
      --w70:         rgba(15,30,60,0.75);
      --w40:         rgba(15,30,60,0.45);
      --w10:         rgba(0,100,200,0.07);
      --border:      rgba(0,153,255,0.2);
      --font:        'Outfit', sans-serif;
      --ease:        all 0.35s cubic-bezier(0.4, 0, 0.2, 1);
      
      --text-main:   #0f1e3c;
      --nav-bg:      rgba(255,255,255,0.92);
    }
    
    [data-theme="dark"] {
      --bg:          #0a0f1d;
      --bg2:         #111827;
      --bg-card:     #1a2335;
      --white:       #0a0f1d;
      --w70:         rgba(255,255,255,0.75);
      --w40:         rgba(255,255,255,0.45);
      --w10:         rgba(255,255,255,0.07);
      --border:      rgba(255,255,255,0.1);
      --text-main:   #f8fafc;
      --nav-bg:      rgba(10,15,29,0.92);
    }
    
    body  { font-family: var(--font);  color: var(--text-main); background-color: var(--bg); overflow-x: hidden; line-height: 1.6; transition: background-color 0.3s, color 0.3s; }
    
    .theme-toggle {
        background: transparent; border: 1.5px solid var(--border);
        border-radius: 50%; width: 38px; height: 38px;
        display: flex; align-items: center; justify-content: center;
        cursor: pointer; color: var(--w70); transition: var(--ease);
    }
    .theme-toggle:hover { background: var(--w10); color: var(--blue); }
'''
content = re.sub(r':root\s*{.*?}\s*html\s*{\s*scroll-behavior:\s*smooth;\s*}\s*html,\s*body\s*{.*?body\s*{.*?}', css_insert + '\n    html  { scroll-behavior: smooth; }\n    html, body { overflow-x: hidden; max-width: 100%; }\n    section { overflow-x: hidden; width: 100%; }\n    html, body { overflow-x: hidden; width: 100%; position: relative; }', content, flags=re.DOTALL)


# 2. Update Header
header_old = r'<ul class="nav-links">.*?<div class="nav-actions">'
header_new = '''<ul class="nav-links">
          <li><a href="index.html" class="active" id="nav-home">Home</a></li>
          <li><a href="courses.html" id="nav-courses">Course</a></li>
          <li><a href="index.html#membership-section" id="nav-membership">Membership</a></li>
          <li><a href="index.html#expert-mentors-section" id="nav-mentorship">Mentorship</a></li>
          <li><a href="blog.html" id="nav-blog">Blog</a></li>
          <li><a href="about.html" id="nav-about">About</a></li>
        </ul>
  
        <div class="nav-actions">
          <button id="themeToggleBtn" class="theme-toggle" aria-label="Toggle Dark Mode">
             <i class="fa-solid fa-moon"></i>
          </button>'''
content = re.sub(header_old, header_new, content, flags=re.DOTALL)

# 3. Add JS for Theme Toggle at end of body
js_theme = '''
<script>
  const themeBtn = document.getElementById('themeToggleBtn');
  if (themeBtn) {
      const icon = themeBtn.querySelector('i');
      
      const savedTheme = localStorage.getItem('theme');
      if (savedTheme === 'dark') {
          document.documentElement.setAttribute('data-theme', 'dark');
          icon.classList.replace('fa-moon', 'fa-sun');
      }
      
      themeBtn.addEventListener('click', () => {
          const currentTheme = document.documentElement.getAttribute('data-theme');
          if (currentTheme === 'dark') {
              document.documentElement.removeAttribute('data-theme');
              localStorage.setItem('theme', 'light');
              icon.classList.replace('fa-sun', 'fa-moon');
          } else {
              document.documentElement.setAttribute('data-theme', 'dark');
              localStorage.setItem('theme', 'dark');
              icon.classList.replace('fa-moon', 'fa-sun');
          }
      });
  }
</script>
</body>
'''
content = content.replace("</body>", js_theme)

# 4. Update Hero Section Left
hero_old = r'<div class="hero-left">.*?</div>\s*<!-- RIGHT PHONE VISUAL'
hero_new = '''<div class="hero-left">
            <h1 class="hero-h1">
              Where Traders are built not just taught.<br/>
              <span class="cycle-wrap"><span id="cycle-word">Stock Market</span></span>
            </h1>
            
            <p style="font-size: 22px; font-weight: 700; color: var(--blue); margin-top: -10px;">Join the Investing School...</p>
            
            <p class="hero-desc" style="margin-top: 10px;">
              India's most trusted stock market education platform. Learn exactly How Top 1% Traders think, plan and Execute.
            </p>
  
            <div class="hero-checks">
              <div class="hck"><div class="hck-dot">1</div>Only one Trading strategies for all market.</div>
              <div class="hck"><div class="hck-dot">2</div>Live Trading session with expert.</div>
              <div class="hck"><div class="hck-dot">3</div>Daily wrap-up video, Trade logic.</div>
              <div class="hck"><div class="hck-dot">4</div>Free community Access for lifetime.</div>
            </div>
  
            <div class="hero-cta">
              <button onclick="window.open('https://t.me/theinvestingschool', '_blank')" class="btn-hero btn-green" id="btn-get-started">
                Get Started Free
              </button>
              <button onclick="document.getElementById('demo-modal').style.display='flex'" class="btn-ghost" id="btn-watch-demo">
                <div class="play-btn"><i class="fa-solid fa-play"></i></div> Watch demo
              </button>
            </div>
  
            <div class="hero-stats" style="gap: 20px; flex-wrap: wrap;">
              <div class="stat"><span class="stat-n">1000+</span><span class="stat-l">Students trained</span></div>
              <div class="stat"><span class="stat-n">20+</span><span class="stat-l">Trading modules</span></div>
              <div class="stat"><span class="stat-n">4.9</span><span class="stat-l">Ratings</span></div>
              <div class="stat"><span class="stat-n">6 Yrs</span><span class="stat-l">Experience</span></div>
              <div class="stat"><span class="stat-n">Online+Offline</span><span class="stat-l">sessions</span></div>
            </div>
          </div>
          <!-- RIGHT PHONE VISUAL'''
content = re.sub(hero_old, hero_new, content, flags=re.DOTALL)

# 5. Add Demo Modal (Popup)
modal_html = '''
<!-- WATCH DEMO MODAL -->
<div id="demo-modal" style="display:none; position:fixed; inset:0; z-index:99999; background:rgba(0,0,0,0.8); align-items:center; justify-content:center; padding:20px;">
  <div style="background:#000; width:100%; max-width:800px; border-radius:12px; position:relative; overflow:hidden; aspect-ratio:16/9; box-shadow: 0 0 50px rgba(0,153,255,0.3);">
    <button onclick="document.getElementById('demo-modal').style.display='none'" style="position:absolute; top:15px; right:15px; z-index:10; background:rgba(255,255,255,0.2); border:none; color:#fff; width:36px; height:36px; border-radius:50%; cursor:pointer; display:flex; align-items:center; justify-content:center;"><i class="fa-solid fa-xmark"></i></button>
    <div style="width:100%; height:100%; display:flex; align-items:center; justify-content:center; color:#fff; flex-direction:column; gap:10px;">
      <i class="fa-solid fa-video" style="font-size: 40px; color: var(--blue);"></i>
      <p>Your Demo Video Here</p>
    </div>
  </div>
</div>
'''
content = content.replace("<body>", f"<body>\n{modal_html}")

# 6. Update Right Side Charts
charts_old = r'<div class="phone-showcase">.*?<!-- TradingView Widgets END -->'
charts_new = '''<div class="phone-showcase">
            <!-- TradingView Widgets BEGIN -->
            <div style="display: flex; flex-direction: column; gap: 15px; width: 100%; max-width: 650px;">
              
              <!-- NIFTY -->
              <div class="tradingview-widget-container" style="width: 100%; height: 160px; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);">
                <div class="tradingview-widget-container__widget"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
                { "symbol": "NSE:NIFTY", "width": "100%", "height": "100%", "locale": "en", "dateRange": "1M", "colorTheme": "light", "isTransparent": false, "autosize": true, "largeChartUrl": "" }
                </script>
              </div>
              
              <!-- XAUUSD -->
              <div class="tradingview-widget-container" style="width: 100%; height: 160px; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);">
                <div class="tradingview-widget-container__widget"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
                { "symbol": "OANDA:XAUUSD", "width": "100%", "height": "100%", "locale": "en", "dateRange": "1M", "colorTheme": "light", "isTransparent": false, "autosize": true, "largeChartUrl": "" }
                </script>
              </div>
  
              <!-- BTCUSD -->
              <div class="tradingview-widget-container" style="width: 100%; height: 160px; border-radius: 15px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.1); border: 1px solid rgba(0,0,0,0.05);">
                <div class="tradingview-widget-container__widget"></div>
                <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-mini-symbol-overview.js" async>
                { "symbol": "BINANCE:BTCUSDT", "width": "100%", "height": "100%", "locale": "en", "dateRange": "1M", "colorTheme": "light", "isTransparent": false, "autosize": true, "largeChartUrl": "" }
                </script>
              </div>

            </div>
            <!-- TradingView Widgets END -->'''
content = re.sub(charts_old, charts_new, content, flags=re.DOTALL)

# 7. Update Cycle Word Script
script_old = r"const words = \['Institutional Level Trading', 'Option Buying Strategies', 'Swing Trading Setups'\];"
script_new = "const words = ['Stock Market', 'Crypto', 'Forex'];"
content = re.sub(script_old, script_new, content)

# 8. Add dark mode overrides to components
css_dark_overrides = '''
    [data-theme="dark"] .hck-dot { background: rgba(255,255,255,0.1); color: var(--blue); }
    [data-theme="dark"] .fcard, [data-theme="dark"] .course-card { background: var(--bg-card); border-color: var(--border); box-shadow: none; }
    [data-theme="dark"] .hero-h1 { color: #fff; }
    [data-theme="dark"] .tradingview-widget-container { filter: invert(1) hue-rotate(180deg); }
'''
content = content.replace("</style>", css_dark_overrides + "\n  </style>")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("HTML Replaced successfully")