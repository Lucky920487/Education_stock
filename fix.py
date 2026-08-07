import sys

css = '''
<style>
/* COMPREHENSIVE MOBILE RESPONSIVENESS FIXES */
@media (max-width: 768px) {
  /* Global Resets */
  html, body {
    overflow-x: hidden !important;
    width: 100% !important;
    max-width: 100vw !important;
    position: relative !important;
  }
  
  /* Hero Section */
  .hero-grid {
    grid-template-columns: 1fr !important;
    display: flex !important;
    flex-direction: column !important;
    align-items: center !important;
    padding-top: 10px !important;
    gap: 30px !important;
  }

  .hero-left {
    width: 100% !important;
    text-align: center !important;
    align-items: center !important;
    justify-content: center !important;
    padding: 0 15px !important;
  }

  .hero-left p, .hero-left h1, .hero-h1 {
    text-align: center !important;
    white-space: normal !important;
  }
  
  .hero-h1 {
    font-size: 36px !important;
    line-height: 1.25 !important;
  }

  .hero-desc {
    font-size: 16px !important;
    max-width: 100% !important;
  }

  .hero-btns {
    display: flex !important;
    flex-direction: column !important;
    width: 100% !important;
    gap: 15px !important;
  }

  .hero-btn {
    width: 100% !important;
    justify-content: center !important;
  }

  /* TradingView Widgets & Cards */
  .hero-right {
    width: 100% !important;
    justify-content: center !important;
    align-items: center !important;
    margin-top: 0 !important;
    padding: 0 15px !important;
  }

  .tradingview-widget-container, .tradingview-widget-container iframe {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 0 !important;
  }
  
  /* Stats Banner */
  .stats-banner {
    display: grid !important;
    grid-template-columns: 1fr 1fr !important;
    gap: 15px !important;
    padding: 15px !important;
    width: 100% !important;
    margin-top: 20px !important;
  }

  .sc {
    padding: 15px 10px !important;
    width: 100% !important;
  }
  
  .sc-n {
    font-size: 26px !important;
  }

  /* Feature Sections (BM Four Cols) */
  .bm-four-cols {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 20px !important;
    padding: 0 20px !important;
    width: 100% !important;
  }

  .bm-divider {
    display: none !important;
  }

  /* Feature Grids */
  .cards-grid {
    display: grid !important;
    grid-template-columns: 1fr !important;
    gap: 20px !important;
    width: 100% !important;
    padding: 0 15px !important;
  }

  .fcard {
    width: 100% !important;
  }

  /* Background Orbs & Floating elements */
  .orb-1, .orb-2, .feat-glow, .fc-signal, .fc-achieve {
    display: none !important; 
  }
  
  /* Fix blank space by overriding min-heights */
  #hero-section {
    min-height: auto !important;
    padding-bottom: 40px !important;
  }
}

@media (max-width: 480px) {
  .stats-banner {
    grid-template-columns: 1fr !important;
  }
  .hero-h1 {
    font-size: 32px !important;
  }
}
</style>
</body>
'''

with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("</body>", css)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)
