$content = [System.IO.File]::ReadAllText(".\index.html", [System.Text.Encoding]::UTF8)

# Currency and arrows
$content = $content -replace '\?(\d{1,3}(,\d{3})+)', '₹$1'
$content = $content -replace '\?(\d{3})', '₹$1'
$content = $content -replace 'Entry \?2,764 \? Target \?3,100', 'Entry ₹2,764 → Target ₹3,100'

# Icons and symbols
$content = $content -replace '<span class="up">\? ', '<span class="up">▲ '
$content = $content -replace '<span class="down">\? ', '<span class="down">▼ '
$content = $content -replace '4\.9 \?', '4.9 ⭐'
$content = $content -replace 'Login to Account \?</button>', 'Login to Account →</button>'
$content = $content -replace 'Create Student Account \?</button>', 'Create Student Account →</button>'
$content = $content -replace 'Read Full Article \?</a>', 'Read Full Article →</a>'
$content = $content -replace 'Login / Sign Up \?</a>', 'Login / Sign Up →</a>'

# Emojis
$content = $content -replace 'content: ''\?\?''', "content: '📡'"
$content = $content -replace '\?\? Live Now', '🔴 Live Now'
$content = $content -replace '\+34\.55% \?\?', '+34.55% 📈'
$content = $content -replace '\?\? Limited Time Offer', '🔥 Limited Time Offer'
$content = $content -replace '<div class="play-btn">\?</div>', '<div class="play-btn">▶</div>'

# Standalone double ??
$content = $content -replace '^\s*\?\?\s*$', '          📈'

# Any missed ??
$content = $content.Replace("??", "📈")
$content = $content.Replace("???", "🚀")

# The subtext ?
$content = $content -replace 'faster and grow your wealth \? all in one', 'faster and grow your wealth — all in one'
$content = $content -replace 'confident trader \? under one roof', 'confident trader — under one roof'

# The toast
$content = $content -replace '\?\? Login Successful', '✅ Login Successful'
$content = $content -replace '\? Registration Successful', '✅ Registration Successful'

[System.IO.File]::WriteAllText(".\index.html", $content, [System.Text.Encoding]::UTF8)
