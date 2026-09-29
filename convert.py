import markdown

with open("README.md", encoding="utf-8") as f:
    text = f.read()

body = markdown.markdown(text, extensions=["fenced_code", "tables", "sane_lists"])

style = """
body{font-family:Arial,Helvetica,sans-serif;max-width:800px;margin:2rem auto;padding:0 1rem;line-height:1.6;color:#222}
h1,h2{border-bottom:1px solid #ddd;padding-bottom:.3rem}
pre{background:#f4f4f4;padding:1rem;border-radius:6px;overflow-x:auto}
code{background:#f4f4f4;padding:2px 4px;border-radius:4px}
pre code{padding:0}
table{border-collapse:collapse}
th,td{border:1px solid #ccc;padding:6px 12px}
th{background:#eee}
blockquote{border-left:4px solid #ccc;margin-left:0;padding-left:1rem;color:#555}
"""

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Expense Tracker README</title>
<style>{style}</style>
</head>
<body>
{body}
</body>
</html>"""

with open("README.html", "w", encoding="utf-8") as f:
    f.write(html)

print("README.html created")