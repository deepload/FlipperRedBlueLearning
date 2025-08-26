#!/usr/bin/env python3
"""
Reliable PDF and EPUB Generator using built-in libraries
Avoids GTK dependencies that cause issues on Windows
"""

import os
import re
import markdown
import zipfile
import uuid
from datetime import datetime

def create_professional_html():
    """Create professional HTML version first"""
    print("📖 Reading markdown file...")
    
    with open("red_team_blue_team_guide.md", 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("🔄 Converting to HTML...")
    
    # Add professional title page content
    title_content = f"""
# Red Team & Blue Team Guide
## Flipper Zero Security Testing & Car Security Exploits

**A Comprehensive Professional Guide to Offensive and Defensive Cybersecurity Testing**

*Author: Cybersecurity Professional*  
*Publisher: Security Research Publications*  
*Publication Date: {datetime.now().strftime('%B %Y')}*

---

## Copyright and Legal Notice

© 2024 Security Research Publications. All rights reserved.

**IMPORTANT LEGAL DISCLAIMER:**
This guide is intended for educational and authorized security testing purposes only. The techniques described should only be used on systems you own or have explicit written permission to test. Unauthorized access to computer systems is illegal and may result in criminal prosecution.

**Publication Information:**
- Title: Red Team & Blue Team Guide: Flipper Zero Security Testing
- Publisher: Security Research Publications
- Publication Date: {datetime.now().strftime('%B %Y')}
- Language: English
- Format: Professional E-book

---

"""
    
    # Combine content
    full_content = title_content + content
    
    # Convert to HTML with extensions
    html_content = markdown.markdown(
        full_content,
        extensions=['codehilite', 'tables', 'toc', 'fenced_code', 'extra']
    )
    
    # Professional CSS styling
    css_styles = """
    @page {
        size: A4;
        margin: 2.5cm;
        @top-center {
            content: "Red Team & Blue Team Guide - Flipper Zero Security Testing";
            font-size: 10pt;
            color: #666;
            font-family: Arial, sans-serif;
        }
        @bottom-center {
            content: "Page " counter(page);
            font-size: 10pt;
            color: #666;
            font-family: Arial, sans-serif;
        }
    }
    
    @media print {
        h1 { page-break-before: always; }
        h1, h2, h3, h4 { page-break-after: avoid; }
        pre, blockquote { page-break-inside: avoid; }
        img { max-width: 100% !important; }
    }
    
    body {
        font-family: Georgia, 'Times New Roman', serif;
        line-height: 1.6;
        color: #333;
        font-size: 12pt;
        max-width: 100%;
        margin: 0 auto;
        padding: 20px;
    }
    
    h1 {
        color: #2c3e50;
        font-size: 24pt;
        font-weight: bold;
        margin-top: 40pt;
        margin-bottom: 20pt;
        border-bottom: 3px solid #3498db;
        padding-bottom: 10pt;
        text-align: left;
    }
    
    h2 {
        color: #34495e;
        font-size: 18pt;
        font-weight: bold;
        margin-top: 30pt;
        margin-bottom: 15pt;
        border-bottom: 1px solid #bdc3c7;
        padding-bottom: 5pt;
    }
    
    h3 {
        color: #2c3e50;
        font-size: 15pt;
        font-weight: bold;
        margin-top: 25pt;
        margin-bottom: 12pt;
    }
    
    h4 {
        color: #34495e;
        font-size: 13pt;
        font-weight: bold;
        margin-top: 20pt;
        margin-bottom: 10pt;
    }
    
    p {
        margin-bottom: 12pt;
        text-align: justify;
        orphans: 2;
        widows: 2;
    }
    
    code {
        background-color: #f8f9fa;
        padding: 2pt 4pt;
        border-radius: 3pt;
        font-family: 'Courier New', 'Consolas', monospace;
        font-size: 10pt;
        color: #e74c3c;
        border: 1px solid #e9ecef;
    }
    
    pre {
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 15pt;
        border-radius: 5pt;
        font-family: 'Courier New', 'Consolas', monospace;
        font-size: 9pt;
        line-height: 1.4;
        overflow-x: auto;
        margin: 15pt 0;
        border: 1px solid #34495e;
        white-space: pre-wrap;
        word-wrap: break-word;
    }
    
    pre code {
        background: none;
        color: #ecf0f1;
        border: none;
        padding: 0;
        font-size: 9pt;
    }
    
    blockquote {
        background-color: #f39c12;
        color: white;
        padding: 12pt 15pt;
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
        page-break-inside: avoid;
    }
    
    th, td {
        border: 1pt solid #bdc3c7;
        padding: 8pt;
        text-align: left;
        vertical-align: top;
    }
    
    th {
        background-color: #34495e;
        color: white;
        font-weight: bold;
        font-size: 10pt;
    }
    
    tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    
    ul, ol {
        margin: 12pt 0;
        padding-left: 25pt;
    }
    
    li {
        margin: 6pt 0;
        line-height: 1.5;
    }
    
    strong, b {
        color: #2c3e50;
        font-weight: bold;
    }
    
    em, i {
        color: #7f8c8d;
        font-style: italic;
    }
    
    .toc {
        background-color: #f8f9fa;
        border: 1px solid #dee2e6;
        border-radius: 5pt;
        padding: 15pt;
        margin: 20pt 0;
    }
    
    .toc h2 {
        margin-top: 0;
        color: #2c3e50;
        border-bottom: 1px solid #bdc3c7;
    }
    
    .highlight {
        background-color: #fff3cd;
        border: 1px solid #ffeaa7;
        border-radius: 3pt;
        padding: 10pt;
        margin: 10pt 0;
    }
    
    .warning {
        background-color: #f8d7da;
        border: 1px solid #f5c6cb;
        border-radius: 3pt;
        padding: 10pt;
        margin: 10pt 0;
        color: #721c24;
    }
    
    .info {
        background-color: #d1ecf1;
        border: 1px solid #bee5eb;
        border-radius: 3pt;
        padding: 10pt;
        margin: 10pt 0;
        color: #0c5460;
    }
    """
    
    # Create complete HTML document
    html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Red Team & Blue Team Guide - Flipper Zero Security Testing</title>
    <style>
        {css_styles}
    </style>
</head>
<body>
    {html_content}
</body>
</html>"""
    
    # Create output directory
    os.makedirs("output", exist_ok=True)
    
    # Save HTML file
    html_path = "output/Red_Team_Blue_Team_Guide_Professional.html"
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_document)
    
    print(f"✅ Professional HTML created: {html_path}")
    return html_path, html_content

def create_epub(html_content):
    """Create EPUB version"""
    print("📚 Creating EPUB...")
    
    epub_path = "output/Red_Team_Blue_Team_Guide_Professional.epub"
    
    # Create temporary directory for EPUB files
    temp_dir = "temp_epub"
    os.makedirs(temp_dir, exist_ok=True)
    os.makedirs(f"{temp_dir}/META-INF", exist_ok=True)
    os.makedirs(f"{temp_dir}/OEBPS", exist_ok=True)
    
    try:
        # Create mimetype
        with open(f"{temp_dir}/mimetype", 'w') as f:
            f.write("application/epub+zip")
        
        # Create container.xml
        container_xml = '''<?xml version="1.0"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
  <rootfiles>
    <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
  </rootfiles>
</container>'''
        
        with open(f"{temp_dir}/META-INF/container.xml", 'w', encoding='utf-8') as f:
            f.write(container_xml)
        
        # Create content.opf
        book_id = str(uuid.uuid4())
        content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="2.0">
  <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
    <dc:identifier id="BookId">{book_id}</dc:identifier>
    <dc:title>Red Team & Blue Team Guide: Flipper Zero Security Testing</dc:title>
    <dc:creator>Cybersecurity Professional</dc:creator>
    <dc:publisher>Security Research Publications</dc:publisher>
    <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
    <dc:language>en</dc:language>
    <dc:subject>Cybersecurity</dc:subject>
    <dc:subject>Penetration Testing</dc:subject>
    <dc:subject>Red Team</dc:subject>
    <dc:subject>Blue Team</dc:subject>
    <dc:subject>Flipper Zero</dc:subject>
    <dc:description>A comprehensive guide to offensive and defensive cybersecurity testing using Flipper Zero and advanced penetration testing techniques.</dc:description>
  </metadata>
  <manifest>
    <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
    <item id="content" href="content.xhtml" media-type="application/xhtml+xml"/>
    <item id="css" href="style.css" media-type="text/css"/>
  </manifest>
  <spine toc="ncx">
    <itemref idref="content"/>
  </spine>
</package>'''
        
        with open(f"{temp_dir}/OEBPS/content.opf", 'w', encoding='utf-8') as f:
            f.write(content_opf)
        
        # Create toc.ncx
        toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
  <head>
    <meta name="dtb:uid" content="{book_id}"/>
    <meta name="dtb:depth" content="1"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>Red Team & Blue Team Guide: Flipper Zero Security Testing</text>
  </docTitle>
  <navMap>
    <navPoint id="navpoint-1" playOrder="1">
      <navLabel>
        <text>Red Team & Blue Team Guide</text>
      </navLabel>
      <content src="content.xhtml"/>
    </navPoint>
  </navMap>
</ncx>'''
        
        with open(f"{temp_dir}/OEBPS/toc.ncx", 'w', encoding='utf-8') as f:
            f.write(toc_ncx)
        
        # Create CSS for EPUB
        epub_css = '''
        body {
            font-family: Georgia, serif;
            line-height: 1.6;
            color: #333;
            margin: 1em;
            font-size: 1em;
        }
        
        h1 {
            color: #2c3e50;
            font-size: 1.8em;
            margin-top: 1.5em;
            margin-bottom: 1em;
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5em;
        }
        
        h2 {
            color: #34495e;
            font-size: 1.4em;
            margin-top: 1.2em;
            margin-bottom: 0.8em;
        }
        
        h3 {
            color: #2c3e50;
            font-size: 1.2em;
            margin-top: 1em;
            margin-bottom: 0.6em;
        }
        
        h4 {
            color: #34495e;
            font-size: 1.1em;
            margin-top: 0.8em;
            margin-bottom: 0.5em;
        }
        
        p {
            margin-bottom: 0.8em;
            text-align: justify;
        }
        
        code {
            background-color: #f8f9fa;
            padding: 0.2em 0.4em;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }
        
        pre {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 1em;
            border-radius: 5px;
            font-family: 'Courier New', monospace;
            font-size: 0.8em;
            line-height: 1.4;
            overflow-x: auto;
            margin: 1em 0;
        }
        
        pre code {
            background: none;
            color: #ecf0f1;
            padding: 0;
        }
        
        blockquote {
            background-color: #f39c12;
            color: white;
            padding: 0.8em 1em;
            border-left: 4px solid #e67e22;
            margin: 1em 0;
            border-radius: 0 5px 5px 0;
            font-weight: bold;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1em 0;
            font-size: 0.9em;
        }
        
        th, td {
            border: 1px solid #bdc3c7;
            padding: 0.5em;
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
        
        ul, ol {
            margin: 0.8em 0;
            padding-left: 1.5em;
        }
        
        li {
            margin: 0.4em 0;
        }
        
        strong {
            color: #2c3e50;
            font-weight: bold;
        }
        
        em {
            color: #7f8c8d;
            font-style: italic;
        }
        '''
        
        with open(f"{temp_dir}/OEBPS/style.css", 'w', encoding='utf-8') as f:
            f.write(epub_css)
        
        # Create content.xhtml
        content_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Red Team & Blue Team Guide: Flipper Zero Security Testing</title>
    <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
    {html_content}
</body>
</html>'''
        
        with open(f"{temp_dir}/OEBPS/content.xhtml", 'w', encoding='utf-8') as f:
            f.write(content_xhtml)
        
        # Create ZIP file (EPUB)
        with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub_zip:
            # Add mimetype first (uncompressed)
            epub_zip.write(f"{temp_dir}/mimetype", "mimetype", compress_type=zipfile.ZIP_STORED)
            
            # Add other files
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    if file != "mimetype":
                        file_path = os.path.join(root, file)
                        arc_path = os.path.relpath(file_path, temp_dir)
                        epub_zip.write(file_path, arc_path)
        
        # Clean up temp directory
        import shutil
        shutil.rmtree(temp_dir)
        
        if os.path.exists(epub_path):
            size = os.path.getsize(epub_path) / (1024 * 1024)
            print(f"✅ EPUB created: {epub_path}")
            print(f"📊 Size: {size:.2f} MB")
            return epub_path
        else:
            print("❌ EPUB creation failed")
            return None
            
    except Exception as e:
        print(f"❌ EPUB creation error: {e}")
        return None

def create_publishing_info():
    """Create publishing information"""
    info_content = f"""
PROFESSIONAL E-BOOK PUBLISHING INFORMATION
==========================================

Title: Red Team & Blue Team Guide: Flipper Zero Security Testing
Subtitle: A Comprehensive Guide to Offensive and Defensive Cybersecurity Testing
Author: Cybersecurity Professional
Publisher: Security Research Publications
Publication Date: {datetime.now().strftime('%B %Y')}
Language: English

Generated Files:
- HTML: Red_Team_Blue_Team_Guide_Professional.html (for PDF conversion)
- EPUB: Red_Team_Blue_Team_Guide_Professional.epub (for e-readers)

To Create PDF:
1. Open the HTML file in Chrome/Edge
2. Print to PDF with these settings:
   - Paper size: A4
   - Margins: Default
   - Options: Background graphics enabled
   - More settings: Headers and footers enabled

Amazon KDP Requirements Met:
✅ Professional formatting and typography
✅ Table of contents
✅ Copyright page and legal disclaimers
✅ Proper metadata for discoverability
✅ E-reader compatible EPUB
✅ Print-ready HTML (convert to PDF)
✅ Professional styling throughout

Content Highlights:
- Comprehensive Flipper Zero security testing guide
- Red Team offensive testing techniques
- Blue Team detection and mitigation strategies
- Car security vulnerabilities and rolling code exploits
- Advanced RF signal analysis and forensics
- Custom firmware documentation (DarkWeb, RollBack, KeyMaster)
- Python code examples for detection systems
- Legal and ethical considerations

Marketing Keywords:
cybersecurity, penetration testing, red team, blue team, flipper zero,
security testing, ethical hacking, network security, wireless security,
incident response, forensics, security analysis, car security, rolling codes,
RF hacking, software defined radio, custom firmware

Target Categories:
- Computer Science > Security > Penetration Testing
- Technology > Computer Security
- Computer Science > Networking

Recommended Pricing:
- E-book: $19.99 - $29.99
- Print: $39.99 - $49.99

Target Audience:
- Cybersecurity professionals
- Penetration testers
- Security researchers
- IT security students
- Ethical hackers

Publishing Steps:
1. Convert HTML to PDF using browser print function
2. Upload PDF to Amazon KDP for print version
3. Upload EPUB to Amazon KDP for Kindle version
4. Create professional cover design
5. Write compelling book description
6. Set pricing and distribution options
"""
    
    with open("output/publishing_info.txt", 'w', encoding='utf-8') as f:
        f.write(info_content)
    
    print("📋 Publishing information saved to: output/publishing_info.txt")

def main():
    """Main function"""
    print("🚀 Starting reliable professional e-book generation...")
    
    if not os.path.exists("red_team_blue_team_guide.md"):
        print("❌ Error: red_team_blue_team_guide.md not found!")
        return
    
    try:
        # Create professional HTML
        html_path, html_content = create_professional_html()
        
        # Create EPUB
        epub_path = create_epub(html_content)
        
        # Create publishing info
        create_publishing_info()
        
        print("\n🎉 Professional e-book generation completed!")
        print(f"📄 HTML (for PDF): {html_path}")
        if epub_path:
            print(f"📚 EPUB: {epub_path}")
        
        print("\n📝 Instructions:")
        print("1. Open the HTML file in Chrome or Edge")
        print("2. Press Ctrl+P to print")
        print("3. Choose 'Save as PDF' as destination")
        print("4. Enable 'Background graphics' in More settings")
        print("5. This will create a professional PDF ready for Amazon KDP!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
