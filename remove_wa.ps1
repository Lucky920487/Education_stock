$files = Get-ChildItem -Filter *.html
$regex = '(?s)<!-- ============================================================ -->\s*<!-- =============  FLOATING WHATSAPP CHAT BUTTON  ============== -->\s*<!-- ============================================================ -->\s*<div id="whatsapp-wrapper">.*?</div>'

foreach ($f in $files) {
    $content = [System.IO.File]::ReadAllText($f.FullName, [System.Text.Encoding]::UTF8)
    $newContent = $content -replace $regex, ''
    [System.IO.File]::WriteAllText($f.FullName, $newContent, [System.Text.Encoding]::UTF8)
}
