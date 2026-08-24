import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace Membership Section
membership_old_pattern = r'<!-- =============  DIV 3 : MEMBERSHIP PLANS SECTION  =========== -->.*?<!-- =============  DIV 4 : BLOG SECTION                           === -->'
membership_new = '''<!-- =============  DIV 3 : MEMBERSHIP PLANS SECTION  =========== -->
<!-- ============================================================ -->
<section id="membership-section" style="padding: 100px 0; background: var(--bg2);">
  <div class="container">
    <div class="sec-head reveal">
      <h2 class="sec-h2">Membership <span class="hl">Plans</span></h2>
      <p class="sec-sub">Choose the perfect plan to accelerate your trading journey.</p>
    </div>

    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 30px; margin-top: 50px;">
      
      <!-- 1 Month Plan -->
      <div class="fcard reveal" style="padding: 40px 30px; text-align: center; border: 1px solid var(--border); border-radius: 20px; background: var(--bg-card); display: flex; flex-direction: column;">
        <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 15px;">1 Month</h3>
        <div style="text-decoration: line-through; color: var(--w40); font-size: 18px; margin-bottom: -5px;">
          <span style="margin-right: 10px;">₹9,990</span> ₹4,990
        </div>
        <div style="font-size: 48px; font-weight: 900; color: var(--blue); margin-bottom: 30px;">
          ₹2,990
        </div>
        <ul style="list-style: none; text-align: left; margin-bottom: 30px; display: flex; flex-direction: column; gap: 15px; font-size: 16px; color: var(--w70); flex-grow: 1;">
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Live market Insight</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Get market updates</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Daily news</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Live Trading signal</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Doubt session</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Trade logic video</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Advanced watchlist</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> All market included</li>
        </ul>
        <button class="btn-green" style="width: 100%; font-size: 18px; padding: 15px;">Buy Now</button>
      </div>

      <!-- 3 Month Plan -->
      <div class="fcard reveal" style="padding: 40px 30px; text-align: center; border: 2px solid var(--blue); border-radius: 20px; background: var(--bg-card); position: relative; transform: scale(1.05); z-index: 10; display: flex; flex-direction: column;">
        <div style="position: absolute; top: -15px; left: 50%; transform: translateX(-50%); background: var(--blue); color: #fff; padding: 5px 15px; border-radius: 20px; font-size: 14px; font-weight: 700;">Best Value</div>
        <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 15px;">3 Month</h3>
        <div style="text-decoration: line-through; color: var(--w40); font-size: 18px; margin-bottom: -5px;">
          ₹8,990
        </div>
        <div style="font-size: 48px; font-weight: 900; color: var(--blue); margin-bottom: 30px;">
          ₹4,990
        </div>
        <ul style="list-style: none; text-align: left; margin-bottom: 30px; display: flex; flex-direction: column; gap: 15px; font-size: 16px; color: var(--w70); flex-grow: 1;">
          <li><i class="fa-solid fa-check-double" style="color: var(--blue); margin-right: 10px;"></i> <strong>All 1 Month Features</strong></li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Extended Support</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Premium Group Access</li>
        </ul>
        <button class="btn-green" style="width: 100%; font-size: 18px; padding: 15px;">Buy Now</button>
      </div>

      <!-- Yearly Plan -->
      <div class="fcard reveal" style="padding: 40px 30px; text-align: center; border: 1px solid var(--border); border-radius: 20px; background: var(--bg-card); display: flex; flex-direction: column;">
        <h3 style="font-size: 24px; font-weight: 700; margin-bottom: 15px;">Yearly</h3>
        <div style="text-decoration: line-through; color: var(--w40); font-size: 18px; margin-bottom: -5px;">
          ₹36,000
        </div>
        <div style="font-size: 48px; font-weight: 900; color: var(--blue); margin-bottom: 30px;">
          ₹14,990
        </div>
        <ul style="list-style: none; text-align: left; margin-bottom: 30px; display: flex; flex-direction: column; gap: 15px; font-size: 16px; color: var(--w70); flex-grow: 1;">
          <li><i class="fa-solid fa-check-double" style="color: var(--blue); margin-right: 10px;"></i> <strong>All 1 Month Features</strong></li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> 1-on-1 Mentorship (Monthly)</li>
          <li><i class="fa-solid fa-circle-check" style="color: #22c55e; margin-right: 10px;"></i> Lifetime Community Access</li>
        </ul>
        <button class="btn-green" style="width: 100%; font-size: 18px; padding: 15px;">Buy Now</button>
      </div>

    </div>
  </div>
</section>

<!-- ============================================================ -->
<!-- =============  NEW: CLIENT FEEDBACK SECTION                  -->
<!-- ============================================================ -->
<section id="feedback-section" style="padding: 100px 0;">
  <div class="container">
    <div class="sec-head reveal">
      <h2 class="sec-h2">Student <span class="hl">Feedback</span></h2>
      <p class="sec-sub">See what our successful traders have to say.</p>
    </div>

    <!-- Video Feedback Placeholder -->
    <div style="margin-top: 50px; background: var(--bg2); padding: 40px; border-radius: 20px; text-align: center; border: 1px dashed var(--blue);">
      <h3 style="font-size: 22px; margin-bottom: 20px;"><i class="fa-solid fa-video" style="color: var(--blue);"></i> Video Feedback Space</h3>
      <p style="color: var(--w70);">Upload your student video testimonials here.</p>
    </div>

    <!-- Client Screenshots Placeholder -->
    <div style="margin-top: 30px; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px;">
      <div style="height: 300px; background: var(--bg2); border-radius: 15px; display: flex; align-items: center; justify-content: center; border: 1px dashed var(--w40); color: var(--w70);">Client Screenshot 1</div>
      <div style="height: 300px; background: var(--bg2); border-radius: 15px; display: flex; align-items: center; justify-content: center; border: 1px dashed var(--w40); color: var(--w70);">Client Screenshot 2</div>
      <div style="height: 300px; background: var(--bg2); border-radius: 15px; display: flex; align-items: center; justify-content: center; border: 1px dashed var(--w40); color: var(--w70);">Client Screenshot 3</div>
      <div style="height: 300px; background: var(--bg2); border-radius: 15px; display: flex; align-items: center; justify-content: center; border: 1px dashed var(--w40); color: var(--w70);">Client Screenshot 4</div>
    </div>

    <!-- 10 Sec Tutoring Snaps Placeholder -->
    <div style="margin-top: 30px; background: var(--bg2); padding: 40px; border-radius: 20px; text-align: center; border: 1px dashed var(--blue);">
      <h3 style="font-size: 22px; margin-bottom: 20px;"><i class="fa-solid fa-bolt" style="color: #f59e0b;"></i> 10 Sec Trading & Tutoring Snaps Space</h3>
      <p style="color: var(--w70);">Upload your short clips and snippets here.</p>
    </div>

  </div>
</section>

<!-- ============================================================ -->
<!-- =============  DIV 4 : BLOG SECTION                           === -->'''
content = re.sub(membership_old_pattern, membership_new, content, flags=re.DOTALL)

# 2. Update Footer / About Us
footer_old_pattern = r'<footer class="site-footer">.*?</footer>'
footer_new = '''<footer class="site-footer" id="about-us-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-col">
          <div class="footer-brand" style="font-size: 24px; font-weight: 800; color: #fff; margin-bottom: 16px; display: flex; align-items: center; gap: 10px;">
            <i class="fa-solid fa-chart-line" style="color: var(--blue-l);"></i> About Us
          </div>
          <p class="footer-desc" style="font-size: 14px; color: #9ca3af; margin-bottom: 24px; line-height: 1.6;">
            The Investing School is India's most trusted stock market education platform. We help you learn exactly how top 1% traders think, plan and execute.
          </p>
          <div class="footer-social">
            <a href="#" onclick="alert('Instagram link coming soon')" target="_blank" title="Instagram"><i class="fa-brands fa-instagram"></i></a>
            <a href="#" onclick="alert('YouTube link coming soon')" target="_blank" title="YouTube"><i class="fa-brands fa-youtube"></i></a>
            <a href="#" onclick="alert('Telegram link coming soon')" target="_blank" title="Telegram"><i class="fa-brands fa-telegram"></i></a>
            <a href="#" onclick="alert('Discord link coming soon')" target="_blank" title="Discord"><i class="fa-brands fa-discord"></i></a>
          </div>
          <p style="color: var(--blue-l); font-size: 12px; margin-top: 10px;">* I will share the link</p>
        </div>
        
        <div class="footer-col">
          <h4 style="font-size: 18px; font-weight: 700; color: #fff; margin-bottom: 20px;">Quick Links</h4>
          <ul class="footer-links">
            <li><a href="#membership-section">Membership Plans</a></li>
            <li><a href="#feedback-section">Student Feedback</a></li>
            <li><a href="#blog-section">Blog</a></li>
            <li><a href="courses.html">Courses</a></li>
          </ul>
        </div>
        
        <div class="footer-col">
          <h4 style="font-size: 18px; font-weight: 700; color: #fff; margin-bottom: 20px;">Contact</h4>
          <div class="contact-item" style="margin-bottom: 15px;">
            <i class="fa-solid fa-envelope icon-yellow"></i> <span class="text-white">theinvestingschool1@gmail.com</span>
          </div>
          <div class="contact-item" style="margin-bottom: 15px;">
            <i class="fa-solid fa-phone icon-green"></i> <span class="text-white">7061408487</span>
          </div>
        </div>
      </div>
      
      <div class="footer-bottom">
        <p>&copy; 2026 The Investing School. All Rights Reserved.</p>
        <div class="footer-bottom-links">
          <a href="#">Privacy Policy</a>
          <a href="#">Terms of Service</a>
        </div>
      </div>
    </div>
</footer>'''
content = re.sub(footer_old_pattern, footer_new, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated Membership, Feedback, and Footer successfully.")