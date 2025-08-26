#!/usr/bin/env python3
"""
Simple Amazon EPUB Generator
Creates EPUB from enhanced_guide.md using only built-in Python libraries.
"""

import os
import re
import uuid
import zipfile
from datetime import datetime

def create_amazon_epub():
    """Create EPUB file from enhanced_guide.md for Amazon KDP"""
    
    print("📚 Creating EPUB for Amazon from enhanced_guide.md...")
    
    # Ensure output directory exists
    os.makedirs("output2", exist_ok=True)
    
    # Read the enhanced guide
    with open("enhanced_guide.md", 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Convert markdown to HTML
    html_content = markdown_to_html(content)
    
    # Split into chapters
    chapters = split_into_chapters(html_content)
    
    # Create EPUB
    epub_path = "output2/Red_Team_Blue_Team_Guide_Professional.epub"
    create_epub_file(chapters, epub_path)
    
    # Create publishing info
    create_publishing_info(epub_path)
    
    print(f"✅ EPUB created: {epub_path}")
    print(f"📊 File size: {os.path.getsize(epub_path) / 1024:.1f} KB")
    return epub_path

def markdown_to_html(markdown_text):
    """Convert markdown to HTML"""
    html = markdown_text
    
    # Clean up any remaining emojis in headers
    html = re.sub(r'#{1,6}\s*[🔴🔵🟡⚫⚪🟢🟠🟣🔶🔷🔸🔹💻📱🌐🔒🔓📊📈📉💡⚡🛡️🎯📝📚💼🚨]\s*', '', html)
    
    # Headers
    html = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', html, flags=re.MULTILINE)
    
    # Bold and italic
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*([^*\n]+?)\*', r'<em>\1</em>', html)
    
    # Code blocks
    html = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code>\2</code></pre>', html, flags=re.DOTALL)
    html = re.sub(r'`([^`\n]+?)`', r'<code>\1</code>', html)
    
    # Lists
    lines = html.split('\n')
    in_list = False
    result_lines = []
    
    for line in lines:
        if re.match(r'^- ', line):
            if not in_list:
                result_lines.append('<ul>')
                in_list = True
            item_text = re.sub(r'^- ', '', line)
            result_lines.append(f'<li>{item_text}</li>')
        else:
            if in_list:
                result_lines.append('</ul>')
                in_list = False
            result_lines.append(line)
    
    if in_list:
        result_lines.append('</ul>')
    
    html = '\n'.join(result_lines)
    
    # Convert paragraphs
    paragraphs = html.split('\n\n')
    formatted_paragraphs = []
    
    for p in paragraphs:
        p = p.strip()
        if p and not p.startswith('<'):
            p = f'<p>{p}</p>'
        if p:
            formatted_paragraphs.append(p)
    
    return '\n\n'.join(formatted_paragraphs)

def split_into_chapters(html_content):
    """Split content into chapters based on h1 headers"""
    # Split by h1 headers (chapters)
    chapter_parts = re.split(r'(<h1>.*?</h1>)', html_content)
    
    chapters = []
    current_title = "Introduction"
    current_content = ""
    
    for i, part in enumerate(chapter_parts):
        if part.startswith('<h1>') and part.endswith('</h1>'):
            # Save previous chapter if it has content
            if current_content.strip():
                chapters.append((current_title, current_content))
            
            # Start new chapter
            current_title = re.sub(r'</?h1>', '', part)
            current_content = part
        else:
            current_content += part
    
    # Add the last chapter
    if current_content.strip():
        chapters.append((current_title, current_content))
    
    return chapters

def create_epub_file(chapters, epub_path):
    """Create the EPUB file"""
    
    book_id = str(uuid.uuid4())
    
    # Create EPUB as ZIP file
    with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub_zip:
        
        # Add mimetype (must be first and uncompressed)
        epub_zip.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        
        # Add META-INF/container.xml
        container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
        epub_zip.writestr("META-INF/container.xml", container_xml)
        
        # Add OEBPS/content.opf
        manifest_items = ['<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>']
        manifest_items.append('<item id="css" href="styles.css" media-type="text/css"/>')
        
        spine_items = []
        
        for i, (title, content) in enumerate(chapters):
            chapter_id = f"chapter{i+1}"
            chapter_file = f"chapter{i+1}.xhtml"
            manifest_items.append(f'<item id="{chapter_id}" href="{chapter_file}" media-type="application/xhtml+xml"/>')
            spine_items.append(f'<itemref idref="{chapter_id}"/>')
        
        content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="2.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
        <dc:identifier id="BookId">{book_id}</dc:identifier>
        <dc:title>Red Team &amp; Blue Team Guide: Flipper Zero Security Testing</dc:title>
        <dc:creator opf:role="aut">Cybersecurity Professional</dc:creator>
        <dc:language>en</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:publisher>Security Research Publications</dc:publisher>
        <dc:description>Comprehensive guide for Red Team and Blue Team cybersecurity operations using Flipper Zero with Predator module. Covers advanced RF and WiFi attack techniques, detection strategies, forensic analysis, and defensive countermeasures.</dc:description>
        <dc:subject>Cybersecurity</dc:subject>
        <dc:subject>Penetration Testing</dc:subject>
        <dc:subject>Red Team</dc:subject>
        <dc:subject>Blue Team</dc:subject>
        <dc:subject>Flipper Zero</dc:subject>
        <dc:rights>All rights reserved</dc:rights>
    </metadata>
    <manifest>
        {chr(10).join(manifest_items)}
    </manifest>
    <spine toc="ncx">
        {chr(10).join(spine_items)}
    </spine>
</package>'''
        epub_zip.writestr("OEBPS/content.opf", content_opf)
        
        # Add OEBPS/toc.ncx
        nav_points = []
        for i, (title, content) in enumerate(chapters):
            nav_points.append(f'''
        <navPoint id="navpoint-{i+1}" playOrder="{i+1}">
            <navLabel>
                <text>{title}</text>
            </navLabel>
            <content src="chapter{i+1}.xhtml"/>
        </navPoint>''')
        
        toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="{book_id}"/>
        <meta name="dtb:depth" content="1"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>Red Team &amp; Blue Team Guide: Flipper Zero Security Testing</text>
    </docTitle>
    <navMap>
        {chr(10).join(nav_points)}
    </navMap>
</ncx>'''
        epub_zip.writestr("OEBPS/toc.ncx", toc_ncx)
        
        # Add CSS
        css_content = '''
body {
    font-family: "Times New Roman", serif;
    line-height: 1.6;
    margin: 0;
    padding: 1em;
    color: #333;
}

h1, h2, h3, h4, h5, h6 {
    font-family: "Arial", sans-serif;
    font-weight: bold;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
    color: #2c3e50;
}

h1 {
    font-size: 2em;
    border-bottom: 3px solid #3498db;
    padding-bottom: 0.3em;
    page-break-before: always;
}

h2 {
    font-size: 1.5em;
    color: #34495e;
}

h3 {
    font-size: 1.3em;
    color: #7f8c8d;
}

p {
    margin: 1em 0;
    text-align: justify;
}

code {
    font-family: "Courier New", monospace;
    background-color: #f8f9fa;
    padding: 0.2em 0.4em;
    border-radius: 3px;
    font-size: 0.9em;
}

pre {
    background-color: #f8f9fa;
    border: 1px solid #e9ecef;
    border-radius: 5px;
    padding: 1em;
    overflow-x: auto;
    margin: 1em 0;
}

pre code {
    background-color: transparent;
    padding: 0;
}

ul, ol {
    margin: 1em 0;
    padding-left: 2em;
}

li {
    margin: 0.5em 0;
}

strong {
    font-weight: bold;
    color: #2c3e50;
}

em {
    font-style: italic;
}
'''
        epub_zip.writestr("OEBPS/styles.css", css_content)
        
        # Add chapter files
        for i, (title, content) in enumerate(chapters):
            chapter_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="styles.css"/>
</head>
<body>
{content}
</body>
</html>'''
            epub_zip.writestr(f"OEBPS/chapter{i+1}.xhtml", chapter_xhtml)

def create_publishing_info(epub_path):
    """Create publishing information file"""
    info_content = f"""EPUB Generation Complete for Amazon KDP
========================================

File: {epub_path}
Title: Red Team & Blue Team Guide: Flipper Zero Security Testing
Author: Cybersecurity Professional
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Amazon Publishing Notes:
- EPUB format is compatible with Amazon KDP
- Professional formatting applied
- Proper metadata included for discoverability
- Code blocks formatted for e-reader compatibility
- Table of contents automatically generated

Next Steps for Amazon Publishing:
1. Upload the EPUB file to Amazon KDP
2. Add cover image (recommended size: 2560x1600 pixels)
3. Set pricing and distribution options
4. Review and publish

File size: {os.path.getsize(epub_path) / 1024:.1f} KB

Content Highlights:
- Comprehensive Flipper Zero security testing guide
- Red Team offensive testing techniques
- Blue Team detection and mitigation strategies
- Car security vulnerabilities and rolling code exploits
- Advanced RF signal analysis and forensics
- Custom firmware documentation
- Python code examples for detection systems
- Legal and ethical considerations

Marketing Keywords:
cybersecurity, penetration testing, red team, blue team, flipper zero,
security testing, ethical hacking, network security, wireless security,
incident response, forensics, security analysis, car security, rolling codes

Target Categories:
- Computer Science > Security > Penetration Testing
- Technology > Computer Security
- Computer Science > Networking

Recommended Pricing:
- E-book: $19.99 - $29.99

Target Audience:
- Cybersecurity professionals
- Penetration testers
- Security researchers
- IT security students
- Ethical hackers
"""
    
    with open("output2/publishing_info.txt", 'w', encoding='utf-8') as f:
        f.write(info_content)

if __name__ == "__main__":
    create_amazon_epub()
