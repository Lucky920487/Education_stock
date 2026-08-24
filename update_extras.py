import re
import glob

# 1. Inject Extras into all HTML files
html_files = glob.glob('*.html')
for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'css/extras.css' not in content:
        content = content.replace('</head>', '  <link rel="stylesheet" href="css/extras.css" />\n</head>')
    if 'js/extras.js' not in content:
        content = content.replace('</body>', '  <script src="js/extras.js"></script>\n</body>')
        
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update 'Your Journey Starts Here' in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Replace the existing become-member-section grid with the new layout
old_bm = r'<div class="bm-four-cols reveal">.*?<div class="bm-cta-center reveal">'
new_bm = '''<div class="bm-two-cols reveal" style="display: grid; grid-template-columns: 1fr 1fr; gap: 40px; margin-top: 50px; align-items: start;">
      
      <!-- Left: Features -->
      <div style="background: var(--bg-card); border: 1px solid var(--border); padding: 40px; border-radius: 20px;">
        <ul style="list-style:none; display:flex; flex-direction:column; gap:20px; font-size:18px; color:var(--text-main); font-weight:500;">
          <li><i class="fa-solid fa-1" style="color:var(--blue); width:30px;"></i> Only 1 strategies for all market.</li>
          <li><i class="fa-solid fa-video" style="color:var(--blue); width:30px;"></i> Live Trading session</li>
          <li><i class="fa-solid fa-play" style="color:var(--blue); width:30px;"></i> Recorded and live classes.</li>
          <li><i class="fa-solid fa-infinity" style="color:var(--blue); width:30px;"></i> Life time Access.</li>
          <li><i class="fa-solid fa-headset" style="color:var(--blue); width:30px;"></i> Priority customer support</li>
        </ul>
        <div style="margin-top: 40px; display:flex; gap:15px; flex-wrap:wrap;">
          <button class="btn-green" onclick="window.location.href=\'#membership-section\'">Join Now</button>
          <button class="btn-outline" onclick="window.location.href=\'courses.html\'">See Inside the course</button>
        </div>
        <div style="margin-top: 30px; display:inline-flex; align-items:center; gap:10px; font-weight:600; color:var(--text-main); background:var(--bg2); padding:10px 20px; border-radius:50px;">
          WhatsApp Chat with us <a href="https://wa.me/917061408487" target="_blank" style="color:#25D366; font-size:24px; margin-left:5px;"><i class="fa-brands fa-whatsapp"></i></a>
        </div>
      </div>

      <!-- Right: Course List -->
      <div style="background: linear-gradient(135deg, var(--blue), var(--blue-d)); padding: 40px; border-radius: 20px; color: #fff;">
        <h3 style="font-size: 24px; margin-bottom: 25px; font-weight: 800;">Course Modules Included:</h3>
        <ul style="list-style:none; display:flex; flex-direction:column; gap:15px; font-size:16px; font-weight:500;">
          <li><i class="fa-solid fa-circle-check" style="color:#fbbf24; margin-right:10px;"></i> Nifty Daily Trading Technique</li>
          <li><i class="fa-solid fa-circle-check" style="color:#fbbf24; margin-right:10px;"></i> Stock Cash Swing strategies</li>
          <li><i class="fa-solid fa-circle-check" style="color:#fbbf24; margin-right:10px;"></i> Stock selection concept</li>
          <li><i class="fa-solid fa-circle-check" style="color:#fbbf24; margin-right:10px;"></i> Sectoral Analysis</li>
          <li><i class="fa-solid fa-circle-check" style="color:#fbbf24; margin-right:10px;"></i> Smart money concept and price action</li>
          <li><i class="fa-solid fa-circle-check" style="color:#fbbf24; margin-right:10px;"></i> Entry and Exit Module</li>
          <li><i class="fa-solid fa-circle-check" style="color:#fbbf24; margin-right:10px;"></i> Nifty 50 ...</li>
        </ul>
      </div>

    </div>

    <div class="bm-cta-center reveal" style="display:none;">'''

idx_content = re.sub(old_bm, new_bm, idx_content, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(idx_content)

print("Injected extras and updated index.html section.")