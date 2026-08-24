import re
import shutil

# Read index.html to extract common parts
with open('index.html', 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract parts from index.html
css_vars_match = re.search(r':root\s*{.*?}.*?body\s*{.*?}', index_content, flags=re.DOTALL)
css_vars = css_vars_match.group(0) if css_vars_match else ""

dark_override_match = re.search(r'\[data-theme="dark"\] \.hck-dot.*?}', index_content, flags=re.DOTALL)
dark_override = dark_override_match.group(0) if dark_override_match else ""

header_match = re.search(r'<header>.*?</header>', index_content, flags=re.DOTALL)
header = header_match.group(0) if header_match else ""

footer_match = re.search(r'<footer class="site-footer" id="about-us-footer">.*?</footer>', index_content, flags=re.DOTALL)
footer = footer_match.group(0) if footer_match else ""

js_theme_match = re.search(r'<script>\s*const themeBtn = document\.getElementById.*?</script>', index_content, flags=re.DOTALL)
js_theme = js_theme_match.group(0) if js_theme_match else ""

blog_section_match = re.search(r'<!-- =============  DIV 4 : BLOG SECTION                           === -->.*?</section>', index_content, flags=re.DOTALL)
blog_section = blog_section_match.group(0) if blog_section_match else ""

# 1. Update about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_content = f.read()

about_content = re.sub(r':root\s*{.*?}\s*html\s*{\s*scroll-behavior:\s*smooth;\s*}\s*html,\s*body\s*{.*?body\s*{.*?}', css_vars + '\n    html  { scroll-behavior: smooth; }\n    html, body { overflow-x: hidden; max-width: 100%; }\n    section { overflow-x: hidden; width: 100%; }\n    html, body { overflow-x: hidden; width: 100%; position: relative; }', about_content, flags=re.DOTALL)
about_content = re.sub(r'<header>.*?</header>', header, about_content, flags=re.DOTALL)
about_content = re.sub(r'<footer class="site-footer">.*?</footer>', footer, about_content, flags=re.DOTALL)
if dark_override and dark_override not in about_content:
    about_content = about_content.replace('</style>', dark_override + '\n  </style>')
if js_theme and js_theme not in about_content:
    about_content = about_content.replace('</body>', js_theme + '\n</body>')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_content)

# 2. Create blog.html from about.html
# We just replace the <main> or the about-section with the blog section.
blog_content = about_content
# Remove the about-section
blog_content = re.sub(r'<section id="about-section".*?</section>', blog_section, blog_content, flags=re.DOTALL)
# Also remove any secondary sections like #mission-section if present, to just leave the blog
blog_content = re.sub(r'<section id="mission-section".*?</section>', '', blog_content, flags=re.DOTALL)

with open('blog.html', 'w', encoding='utf-8') as f:
    f.write(blog_content)

print("Updated about.html and created blog.html successfully")