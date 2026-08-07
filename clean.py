import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the previously injected blocks
html = re.sub(r'@media \(max-width: 1024px\) \{\s*\.hero-grid \{.*?\}\s*</style>', '</style>', html, flags=re.DOTALL)

# Add our clean mobile override block right before the final </style>
# Wait, let's just insert it right before </head> to be safe.
# Actually, inserting it at the end of the main <style> block is best.

# Let's find the first </style> which belongs to the main block.
clean_css = '''
/* FINAL MOBILE FIXES */
@media (max-width: 1024px) {
  /* Fix text cut-off */
  .tick { white-space: normal !important; align-items: flex-start !important; }
  .tick i { margin-top: 4px; }
  
  /* Stack the hero section properly */
  .hero-grid { 
    display: flex !important; 
    flex-direction: column !important; 
    align-items: center !important;
    padding-top: 0 !important;
  }
  
  /* Ensure hero elements don't push boundaries */
  .hero-left, .hero-right {
    width: 100% !important;
    max-width: 100vw !important;
    padding: 0 10px !important;
    margin: 0 !important;
  }
  
  .hero-right {
    justify-content: center !important;
    margin-top: 20px !important;
  }

  .tradingview-widget-container, .tradingview-widget-container iframe {
    max-width: 100vw !important;
    width: 100% !important;
  }

  /* Prevent grid blowouts */
  .bm-four-cols, .cards-grid {
    display: flex !important;
    flex-direction: column !important;
  }
  
  .stats-banner {
    display: flex !important;
    flex-wrap: wrap !important;
    justify-content: center !important;
  }
  .sc { flex: 1 1 40% !important; }

  /* Ensure body doesn't zoom out */
  html, body {
    overflow-x: hidden !important;
    width: 100vw !important;
    max-width: 100% !important;
  }
}

@media (max-width: 768px) {
  .hero-h1 { font-size: 32px !important; }
  .hero-desc { font-size: 16px !important; }
  .sc { flex: 1 1 100% !important; }
}
'''

# Find the first </style>
first_style_end = html.find('</style>')
if first_style_end != -1:
    html = html[:first_style_end] + clean_css + html[first_style_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
