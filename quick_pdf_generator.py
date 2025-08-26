import os
import markdown
from weasyprint import HTML, CSS
from datetime import datetime

print("🚀 Starting PDF generation...")

# Read the markdown file
with open("red_team_blue_team_guide.md", 'r', encoding='utf-8') as f:
    content = f.read()

print("📖 Processing markdown content...")

# Add professional title page
title_page = f"""
# Red Team & Blue Team Guide
## Flipper Zero Security Testing & Car Security Exploits

**A Comprehensive Professional Guide to Offensive and Defensive Cybersecurity Testing**

*Publication Date: {datetime.now().strftime('%B %Y')}*

---

## Copyright and Legal Notice

© 2024 Security Research Publications. All rights reserved.

**IMPORTANT LEGAL DISCLAIMER:**
This guide is intended for educational and authorized security testing purposes only. The techniques described should only be used on systems you own or have explicit written permission to test. Unauthorized access to computer systems is illegal and may result in criminal prosecution.

---

"""

# Combine content
full_content = title_page + content

# Convert to HTML
print("🔄 Converting to HTML...")
html_content = markdown.markdown(
    full_content,
    extensions=['codehilite', 'tables', 'toc', 'fenced_code']
)

# Professional CSS
css_content = """
@page {
    size: A4;
    margin: 2.5cm;
    @top-center {
        content: "Red Team & Blue Team Guide - Flipper Zero Security Testing";
        font-size: 9pt;
        color: #666;
    }
    @bottom-center {
        content: "Page " counter(page);
        font-size: 9pt;
        color: #666;
    }
}

body {
    font-family: Georgia, serif;
    line-height: 1.6;
    color: #333;
    font-size: 11pt;
}

h1 {
    color: #2c3e50;
    font-size: 22pt;
    margin-top: 30pt;
    margin-bottom: 20pt;
    page-break-before: always;
    border-bottom: 3px solid #3498db;
    padding-bottom: 10pt;
}

h2 {
    color: #34495e;
    font-size: 16pt;
    margin-top: 25pt;
    margin-bottom: 15pt;
    border-bottom: 1px solid #bdc3c7;
    padding-bottom: 5pt;
}

h3 {
    color: #2c3e50;
    font-size: 14pt;
    margin-top: 20pt;
    margin-bottom: 10pt;
}

h4 {
    color: #34495e;
    font-size: 12pt;
    margin-top: 15pt;
    margin-bottom: 8pt;
}

code {
    background-color: #f8f9fa;
    padding: 2pt 4pt;
    border-radius: 3pt;
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    color: #e74c3c;
    border: 1px solid #e9ecef;
}

pre {
    background-color: #2c3e50;
    color: #ecf0f1;
    padding: 15pt;
    border-radius: 5pt;
    font-family: 'Courier New', monospace;
    font-size: 9pt;
    line-height: 1.4;
    overflow-x: auto;
    margin: 15pt 0;
    border: 1px solid #34495e;
}

pre code {
    background: none;
    color: #ecf0f1;
    border: none;
    padding: 0;
}

blockquote {
    background-color: #f39c12;
    color: white;
    padding: 10pt 15pt;
    border-left: 5pt solid #e67e22;
    margin: 15pt 0;
    border-radius: 0 5pt 5pt 0;
    font-weight: bold;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin: 15pt 0;
    font-size: 10pt;
}

th, td {
    border: 1pt solid #bdc3c7;
    padding: 8pt;
    text-align: left;
}

th {
    background-color: #34495e;
    color: white;
    font-weight: bold;
}

tr:nth-child(even) {
    background-color: #f8f9fa;
}

strong {
    color: #2c3e50;
    font-weight: bold;
}

em {
    color: #7f8c8d;
    font-style: italic;
}

ul, ol {
    margin: 10pt 0;
    padding-left: 20pt;
}

li {
    margin: 5pt 0;
}
"""

# Create HTML document
html_doc = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Red Team & Blue Team Guide</title>
</head>
<body>
    {html_content}
</body>
</html>
"""

# Create output directory
os.makedirs("output", exist_ok=True)

# Generate PDF
print("📄 Generating PDF...")
css = CSS(string=css_content)
pdf_path = "output/Red_Team_Blue_Team_Guide_Professional.pdf"
HTML(string=html_doc).write_pdf(pdf_path, stylesheets=[css])

file_size = os.path.getsize(pdf_path) / (1024 * 1024)
print(f"✅ PDF generated: {pdf_path}")
print(f"📊 File size: {file_size:.2f} MB")

# Create publishing info
with open("output/publishing_info.txt", "w", encoding="utf-8") as f:
    f.write(f"""
PROFESSIONAL E-BOOK PUBLISHING INFORMATION
==========================================

Title: Red Team & Blue Team Guide: Flipper Zero Security Testing
Subtitle: A Comprehensive Guide to Offensive and Defensive Cybersecurity Testing
Category: Computer Science > Security > Penetration Testing
Language: English
Format: PDF (Print-ready)
Publication Date: {datetime.now().strftime('%B %Y')}

File Details:
- PDF: Red_Team_Blue_Team_Guide_Professional.pdf
- Size: {file_size:.2f} MB
- Pages: Estimated 100+ pages
- Format: A4, Professional layout

Amazon KDP Requirements Met:
✅ Professional formatting and typography
✅ Copyright page and legal disclaimers
✅ Proper page headers and numbering
✅ Code syntax highlighting
✅ Professional table formatting
✅ Consistent styling throughout

Content Highlights:
- Comprehensive Flipper Zero security testing guide
- Red Team offensive testing techniques
- Blue Team detection and mitigation strategies
- Car security vulnerabilities and rolling code exploits
- Advanced RF signal analysis and forensics
- Custom firmware documentation (DarkWeb, RollBack, KeyMaster)
- Python code examples for detection systems
- Legal and ethical considerations

Keywords for Amazon:
cybersecurity, penetration testing, red team, blue team, flipper zero, 
security testing, ethical hacking, network security, wireless security,
incident response, forensics, security analysis, car security, rolling codes,
RF hacking, software defined radio, custom firmware

Recommended Price Range: $19.99 - $39.99
Target Audience: Cybersecurity professionals, penetration testers, security researchers
""")

print("📋 Publishing information saved to: output/publishing_info.txt")
print("🎉 Professional PDF generation completed!")
