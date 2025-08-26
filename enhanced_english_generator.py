#!/usr/bin/env python3
"""
Enhanced English E-book Generator
Creates comprehensive PDF and EPUB from enhanced English guide
"""

import os
import markdown
import zipfile
import uuid
from datetime import datetime

def create_enhanced_english_ebook():
    """Create professional e-book from enhanced English content"""
    
    print("🚀 Creating enhanced English e-book...")
    
    # Read the enhanced English guide
    if not os.path.exists("red_team_blue_team_guide_enhanced_english.md"):
        print("❌ Enhanced English guide not found!")
        return
    
    with open("red_team_blue_team_guide_enhanced_english.md", 'r', encoding='utf-8') as f:
        content = f.read()
    
    print("📖 Processing enhanced content...")
    
    # Convert to HTML with all extensions
    html_content = markdown.markdown(
        content,
        extensions=['codehilite', 'tables', 'toc', 'fenced_code', 'extra', 'nl2br']
    )
    
    # Enhanced professional CSS
    css_styles = """
    @page {
        size: A4;
        margin: 2.5cm;
        @top-center {
            content: "Red Team & Blue Team Guide - Enhanced Edition";
            font-size: 10pt;
            color: #666;
        }
        @bottom-center {
            content: "Page " counter(page);
            font-size: 10pt;
            color: #666;
        }
    }
    
    @media print {
        h1 { page-break-before: always; }
        h1, h2, h3, h4 { page-break-after: avoid; }
        pre, blockquote { page-break-inside: avoid; }
        .code-block { page-break-inside: avoid; }
    }
    
    body {
        font-family: 'Georgia', 'Times New Roman', serif;
        line-height: 1.7;
        color: #2c3e50;
        font-size: 12pt;
        max-width: 100%;
        margin: 0 auto;
        padding: 20px;
    }
    
    h1 {
        color: #1a252f;
        font-size: 26pt;
        font-weight: bold;
        margin-top: 40pt;
        margin-bottom: 25pt;
        border-bottom: 4px solid #3498db;
        padding-bottom: 15pt;
        text-align: left;
    }
    
    h2 {
        color: #2c3e50;
        font-size: 20pt;
        font-weight: bold;
        margin-top: 35pt;
        margin-bottom: 18pt;
        border-bottom: 2px solid #bdc3c7;
        padding-bottom: 8pt;
    }
    
    h3 {
        color: #34495e;
        font-size: 16pt;
        font-weight: bold;
        margin-top: 28pt;
        margin-bottom: 15pt;
    }
    
    h4 {
        color: #2c3e50;
        font-size: 14pt;
        font-weight: bold;
        margin-top: 22pt;
        margin-bottom: 12pt;
    }
    
    p {
        margin-bottom: 14pt;
        text-align: justify;
        orphans: 2;
        widows: 2;
    }
    
    code {
        background-color: #f8f9fa;
        padding: 3pt 6pt;
        border-radius: 4pt;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 10pt;
        color: #e74c3c;
        border: 1px solid #e9ecef;
    }
    
    pre {
        background-color: #2c3e50;
        color: #ecf0f1;
        padding: 20pt;
        border-radius: 8pt;
        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
        font-size: 9pt;
        line-height: 1.5;
        overflow-x: auto;
        margin: 20pt 0;
        border: 2px solid #34495e;
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
        background: linear-gradient(135deg, #f39c12, #e67e22);
        color: white;
        padding: 15pt 20pt;
        border-left: 6pt solid #d35400;
        margin: 20pt 0;
        border-radius: 0 8pt 8pt 0;
        font-weight: bold;
        box-shadow: 0 2pt 4px rgba(0,0,0,0.1);
    }
    
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 20pt 0;
        font-size: 10pt;
        page-break-inside: avoid;
        box-shadow: 0 2pt 4px rgba(0,0,0,0.1);
    }
    
    th, td {
        border: 1pt solid #bdc3c7;
        padding: 10pt;
        text-align: left;
        vertical-align: top;
    }
    
    th {
        background: linear-gradient(135deg, #34495e, #2c3e50);
        color: white;
        font-weight: bold;
        font-size: 10pt;
    }
    
    tr:nth-child(even) {
        background-color: #f8f9fa;
    }
    
    tr:hover {
        background-color: #e8f4f8;
    }
    
    ul, ol {
        margin: 15pt 0;
        padding-left: 30pt;
    }
    
    li {
        margin: 8pt 0;
        line-height: 1.6;
    }
    
    strong, b {
        color: #1a252f;
        font-weight: bold;
    }
    
    em, i {
        color: #7f8c8d;
        font-style: italic;
    }
    
    .toc {
        background-color: #f8f9fa;
        border: 2px solid #dee2e6;
        border-radius: 8pt;
        padding: 20pt;
        margin: 25pt 0;
    }
    
    .toc h2 {
        margin-top: 0;
        color: #2c3e50;
        border-bottom: 2px solid #bdc3c7;
    }
    
    .highlight {
        background-color: #fff3cd;
        border: 2px solid #ffeaa7;
        border-radius: 6pt;
        padding: 15pt;
        margin: 15pt 0;
    }
    
    .warning {
        background-color: #f8d7da;
        border: 2px solid #f5c6cb;
        border-radius: 6pt;
        padding: 15pt;
        margin: 15pt 0;
        color: #721c24;
    }
    
    .info {
        background-color: #d1ecf1;
        border: 2px solid #bee5eb;
        border-radius: 6pt;
        padding: 15pt;
        margin: 15pt 0;
        color: #0c5460;
    }
    
    .code-block {
        margin: 20pt 0;
        border-radius: 8pt;
        overflow: hidden;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .chapter-title {
        text-align: center;
        color: #1a252f;
        font-size: 28pt;
        margin: 40pt 0;
        text-transform: uppercase;
        letter-spacing: 2pt;
    }
    """
    
    # Create complete HTML document
    html_document = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="author" content="Cybersecurity Professional">
    <meta name="description" content="Comprehensive guide to Red Team and Blue Team cybersecurity testing with Flipper Zero">
    <meta name="keywords" content="cybersecurity, penetration testing, red team, blue team, flipper zero, car security">
    <title>Red Team & Blue Team Guide - Enhanced Edition</title>
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
    
    # Save enhanced HTML file
    html_path = "output/Red_Team_Blue_Team_Guide_Enhanced_English.html"
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_document)
    
    print(f"✅ Enhanced HTML created: {html_path}")
    
    # Create EPUB
    print("📚 Creating enhanced EPUB...")
    epub_path = create_enhanced_epub(html_content)
    
    # Create publishing information
    create_enhanced_publishing_info()
    
    print("\n🎉 Enhanced English e-book generation completed!")
    print(f"📄 HTML (for PDF): {html_path}")
    if epub_path:
        print(f"📚 EPUB: {epub_path}")
    
    print("\n📝 Instructions for PDF creation:")
    print("1. Open the HTML file in Chrome or Edge")
    print("2. Press Ctrl+P to print")
    print("3. Choose 'Save as PDF' as destination")
    print("4. Set margins to 'Default'")
    print("5. Enable 'Background graphics' in More settings")
    print("6. This creates a professional PDF ready for Amazon KDP!")

def create_enhanced_epub(html_content):
    """Create enhanced EPUB version"""
    
    epub_path = "output/Red_Team_Blue_Team_Guide_Enhanced_English.epub"
    
    # Create temporary directory for EPUB files
    temp_dir = "temp_epub_enhanced"
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
    <dc:title>Red Team & Blue Team Guide: Enhanced Edition</dc:title>
    <dc:creator>Cybersecurity Professional</dc:creator>
    <dc:publisher>Security Research Publications</dc:publisher>
    <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
    <dc:language>en</dc:language>
    <dc:subject>Cybersecurity</dc:subject>
    <dc:subject>Penetration Testing</dc:subject>
    <dc:subject>Red Team</dc:subject>
    <dc:subject>Blue Team</dc:subject>
    <dc:subject>Flipper Zero</dc:subject>
    <dc:subject>Car Security</dc:subject>
    <dc:subject>RF Hacking</dc:subject>
    <dc:description>A comprehensive enhanced guide to offensive and defensive cybersecurity testing using Flipper Zero, with detailed examples, practical exercises, and advanced techniques for car security testing.</dc:description>
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
    <meta name="dtb:depth" content="3"/>
    <meta name="dtb:totalPageCount" content="0"/>
    <meta name="dtb:maxPageNumber" content="0"/>
  </head>
  <docTitle>
    <text>Red Team & Blue Team Guide: Enhanced Edition</text>
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
        
        # Create enhanced CSS for EPUB
        epub_css = '''
        body {
            font-family: Georgia, serif;
            line-height: 1.7;
            color: #2c3e50;
            margin: 1.5em;
            font-size: 1em;
        }
        
        h1 {
            color: #1a252f;
            font-size: 2em;
            margin-top: 2em;
            margin-bottom: 1.5em;
            border-bottom: 3px solid #3498db;
            padding-bottom: 0.8em;
        }
        
        h2 {
            color: #2c3e50;
            font-size: 1.6em;
            margin-top: 1.8em;
            margin-bottom: 1.2em;
            border-bottom: 1px solid #bdc3c7;
            padding-bottom: 0.5em;
        }
        
        h3 {
            color: #34495e;
            font-size: 1.3em;
            margin-top: 1.5em;
            margin-bottom: 1em;
        }
        
        h4 {
            color: #2c3e50;
            font-size: 1.1em;
            margin-top: 1.2em;
            margin-bottom: 0.8em;
        }
        
        p {
            margin-bottom: 1em;
            text-align: justify;
        }
        
        code {
            background-color: #f8f9fa;
            padding: 0.3em 0.5em;
            border-radius: 4px;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 0.9em;
            color: #e74c3c;
        }
        
        pre {
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 1.5em;
            border-radius: 8px;
            font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
            font-size: 0.8em;
            line-height: 1.5;
            overflow-x: auto;
            margin: 1.5em 0;
        }
        
        pre code {
            background: none;
            color: #ecf0f1;
            padding: 0;
        }
        
        blockquote {
            background: linear-gradient(135deg, #f39c12, #e67e22);
            color: white;
            padding: 1.2em 1.5em;
            border-left: 5px solid #d35400;
            margin: 1.5em 0;
            border-radius: 0 8px 8px 0;
            font-weight: bold;
        }
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1.5em 0;
            font-size: 0.9em;
        }
        
        th, td {
            border: 1px solid #bdc3c7;
            padding: 0.8em;
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
            margin: 1em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.5em 0;
        }
        
        strong {
            color: #1a252f;
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
    <title>Red Team & Blue Team Guide: Enhanced Edition</title>
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
            print(f"✅ Enhanced EPUB created: {epub_path} ({size:.2f} MB)")
            return epub_path
        else:
            print("❌ EPUB creation failed")
            return None
            
    except Exception as e:
        print(f"❌ EPUB creation error: {e}")
        return None

def create_enhanced_publishing_info():
    """Create enhanced publishing information"""
    
    info_content = f"""
ENHANCED ENGLISH E-BOOK PUBLISHING INFORMATION
==============================================

Title: Red Team & Blue Team Guide: Enhanced Edition
Subtitle: Advanced Cybersecurity Testing with Flipper Zero and Car Security Exploits
Author: Cybersecurity Professional
Publisher: Security Research Publications
Publication Date: {datetime.now().strftime('%B %Y')}
Language: English (Enhanced Edition)
Edition: Professional Enhanced Version

Generated Files:
- HTML: Red_Team_Blue_Team_Guide_Enhanced_English.html
- EPUB: Red_Team_Blue_Team_Guide_Enhanced_English.epub

ENHANCED FEATURES:
✅ Comprehensive technical examples and code snippets
✅ Detailed step-by-step Red Team procedures
✅ Advanced Blue Team detection methods with Python implementations
✅ Practical laboratory exercises
✅ Real-world car security testing scenarios
✅ Professional incident response playbooks
✅ Enhanced formatting and typography
✅ Improved code syntax highlighting
✅ Advanced CSS styling for professional appearance

CONTENT HIGHLIGHTS:
- 10+ chapters of comprehensive cybersecurity content
- 50+ practical code examples and scripts
- Detailed vulnerability assessment procedures
- Advanced RF signal analysis techniques
- Custom firmware exploitation methods
- Professional detection and monitoring systems
- Incident response and forensics procedures
- Legal and ethical framework guidance

TECHNICAL SPECIFICATIONS:
- Enhanced markdown with extended syntax
- Professional CSS styling with gradients and shadows
- Responsive design for multiple devices
- Print-optimized layout for PDF conversion
- E-reader optimized EPUB format
- Comprehensive metadata for discoverability

AMAZON KDP OPTIMIZATION:
✅ Professional formatting meeting KDP standards
✅ Comprehensive table of contents
✅ Copyright and legal disclaimers
✅ Enhanced metadata for search optimization
✅ Print-ready HTML for PDF conversion
✅ Kindle-compatible EPUB format
✅ Professional typography and layout

MARKETING KEYWORDS:
Primary: cybersecurity, penetration testing, red team, blue team, flipper zero
Secondary: car security, rolling codes, RF hacking, wireless security, ethical hacking
Long-tail: flipper zero car security testing, red team blue team guide, 
          cybersecurity penetration testing manual, RF signal analysis

TARGET CATEGORIES:
1. Computer Science > Security > Penetration Testing
2. Technology > Computer Security > Network Security
3. Computer Science > Networking > Wireless
4. Technology > Electronics > Radio Frequency

PRICING STRATEGY:
- E-book (Kindle): $24.99 - $34.99 (premium pricing for enhanced content)
- Print-on-Demand: $49.99 - $59.99 (professional reference pricing)
- Bundle discount: 15% for both formats

TARGET AUDIENCE:
Primary:
- Professional penetration testers
- Cybersecurity consultants
- Security researchers
- Red/Blue team members

Secondary:
- IT security students
- Ethical hackers
- Security enthusiasts
- Academic researchers

COMPETITIVE ADVANTAGES:
- Only comprehensive guide covering Flipper Zero car security
- Includes both offensive and defensive perspectives
- Practical code examples and real-world scenarios
- Professional-grade detection and monitoring tools
- Enhanced edition with premium content and formatting

PUBLISHING TIMELINE:
1. Convert HTML to PDF using browser print function
2. Upload PDF to Amazon KDP for print version
3. Upload EPUB to Amazon KDP for Kindle version
4. Create professional cover design (recommended: cybersecurity theme)
5. Write compelling book description (focus on practical value)
6. Set up author profile and marketing materials
7. Configure pricing and distribution options
8. Launch with promotional campaign

PDF CONVERSION INSTRUCTIONS:
1. Open Red_Team_Blue_Team_Guide_Enhanced_English.html in Chrome/Edge
2. Press Ctrl+P (Windows) or Cmd+P (Mac)
3. Destination: Save as PDF
4. Paper size: A4
5. Margins: Default
6. Options: Background graphics ENABLED
7. More settings: Headers and footers ENABLED
8. Save as: Red_Team_Blue_Team_Guide_Enhanced_Professional.pdf

This creates a publication-ready PDF suitable for Amazon KDP print-on-demand services.
"""
    
    with open("output/enhanced_publishing_info.txt", 'w', encoding='utf-8') as f:
        f.write(info_content)
    
    print("📋 Enhanced publishing information saved to: output/enhanced_publishing_info.txt")

if __name__ == "__main__":
    create_enhanced_english_ebook()
