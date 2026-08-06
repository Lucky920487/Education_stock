$footerHtml = @"
<style>
/* ===== ENHANCED FOOTER ===== */
.premium-footer {
  background: #0f1e3c;
  color: #a0aec0;
  padding: 80px 0 30px;
  border-top: 5px solid var(--blue);
}
.footer-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
  gap: 40px;
  margin-bottom: 50px;
}
.footer-brand {
  font-size: 24px;
  font-weight: 900;
  color: #fff;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  gap: 10px;
}
.footer-brand i { color: var(--blue-l); }
.footer-desc {
  line-height: 1.6;
  margin-bottom: 25px;
  font-size: 15px;
}
.social-links {
  display: flex;
  gap: 15px;
}
.social-links a {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 40px;
  height: 40px;
  background: rgba(255,255,255,0.05);
  color: #fff;
  border-radius: 50%;
  transition: var(--ease);
}
.social-links a:hover {
  background: var(--blue-l);
  transform: translateY(-3px);
}
.footer-col-title {
  font-size: 18px;
  font-weight: 700;
  color: #fff;
  margin-bottom: 20px;
  position: relative;
  padding-bottom: 10px;
}
.footer-col-title::after {
  content: '';
  position: absolute;
  bottom: 0; left: 0;
  width: 40px; height: 3px;
  background: var(--blue-l);
  border-radius: 2px;
}
.footer-links {
  list-style: none;
}
.footer-links li {
  margin-bottom: 12px;
}
.footer-links a {
  transition: var(--ease);
}
.footer-links a:hover {
  color: var(--blue-l);
  padding-left: 5px;
}
.footer-newsletter p {
  margin-bottom: 15px;
  font-size: 14px;
}
.footer-form {
  display: flex;
}
.footer-form input {
  flex: 1;
  padding: 12px 15px;
  border: none;
  border-radius: 4px 0 0 4px;
  outline: none;
}
.footer-form button {
  background: var(--blue-l);
  color: #fff;
  border: none;
  padding: 0 15px;
  border-radius: 0 4px 4px 0;
  cursor: pointer;
  transition: var(--ease);
  font-weight: 700;
}
.footer-form button:hover {
  background: var(--blue-d);
}
.footer-bottom {
  border-top: 1px solid rgba(255,255,255,0.1);
  padding-top: 30px;
  text-align: center;
  font-size: 14px;
}
.footer-bottom-links {
  margin-top: 10px;
  display: flex;
  justify-content: center;
  gap: 20px;
}
.footer-bottom-links a:hover {
  color: #fff;
}
</style>

<!-- FOOTER -->
<footer class="premium-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-col">
        <div class="footer-brand">
          <i class="fa-solid fa-chart-line"></i> The Investing School
        </div>
        <p class="footer-desc">Empowering traders with institutional grade knowledge and battle-tested strategies to achieve financial freedom.</p>
        <div class="social-links">
          <a href="#"><i class="fa-brands fa-youtube"></i></a>
          <a href="#"><i class="fa-brands fa-instagram"></i></a>
          <a href="#"><i class="fa-brands fa-telegram"></i></a>
          <a href="#"><i class="fa-brands fa-twitter"></i></a>
        </div>
      </div>
      
      <div class="footer-col">
        <h4 class="footer-col-title">Quick Links</h4>
        <ul class="footer-links">
          <li><a href="#premium-courses-section">Premium Courses</a></li>
          <li><a href="#live-signals-section">Live Signals</a></li>
          <li><a href="#expert-mentors-section">Our Mentors</a></li>
          <li><a href="#blog-section">Trading Blog</a></li>
        </ul>
      </div>
      
      <div class="footer-col">
        <h4 class="footer-col-title">Support</h4>
        <ul class="footer-links">
          <li><a href="#">Help Center</a></li>
          <li><a href="#">Contact Us</a></li>
          <li><a href="#">Student Dashboard</a></li>
          <li><a href="#">Terms & Conditions</a></li>
        </ul>
      </div>
      
      <div class="footer-col footer-newsletter">
        <h4 class="footer-col-title">Weekly Newsletter</h4>
        <p>Get our free weekend market analysis and stock picks delivered to your inbox.</p>
        <form class="footer-form" onsubmit="event.preventDefault(); alert('Subscribed!');">
          <input type="email" placeholder="Email Address" required>
          <button type="submit">Join</button>
        </form>
      </div>
    </div>
    
    <div class="footer-bottom">
      <p>&copy; 2026 The Investing School. All Rights Reserved. Educational Stock Market Platform.</p>
      <div class="footer-bottom-links">
        <a href="#">Privacy Policy</a>
        <a href="#">Refund Policy</a>
        <a href="#">Disclaimer</a>
      </div>
    </div>
  </div>
</footer>
"@

$content = [System.IO.File]::ReadAllText(".\index.html", [System.Text.Encoding]::UTF8)

# Replace the old footer
$content = $content -replace '(?s)<!-- FOOTER -->\s*<footer>.*?</footer>', $footerHtml

[System.IO.File]::WriteAllText(".\index.html", $content, [System.Text.Encoding]::UTF8)
