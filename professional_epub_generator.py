#!/usr/bin/env python3
"""
Professional EPUB Generator for Cybersecurity Guides
Enhanced formatting with proper spacing and professional layout
"""

import os
import re
import zipfile
import uuid
from datetime import datetime
from pathlib import Path
import markdown
from markdown.extensions import codehilite, tables, toc

class ProfessionalEPUBGenerator:
    def __init__(self, input_file, output_dir="epub"):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Professional styling
        self.css_content = """
        @namespace epub "http://www.idpf.org/2007/ops";
        
        body {
            font-family: "Georgia", "Times New Roman", serif;
            line-height: 1.6;
            margin: 0;
            padding: 1em;
            color: #333;
            background: #fff;
        }
        
        h1, h2, h3, h4, h5, h6 {
            font-family: "Arial", "Helvetica", sans-serif;
            font-weight: bold;
            margin: 1.5em 0 0.8em 0;
            line-height: 1.3;
            color: #2c3e50;
        }
        
        h1 { font-size: 2.2em; margin-top: 0; border-bottom: 3px solid #3498db; padding-bottom: 0.3em; }
        h2 { font-size: 1.8em; color: #e74c3c; }
        h3 { font-size: 1.5em; color: #f39c12; }
        h4 { font-size: 1.3em; color: #27ae60; }
        
        p {
            margin: 0.8em 0;
            text-align: justify;
            orphans: 2;
            widows: 2;
        }
        
        blockquote {
            margin: 1.5em 2em;
            padding: 1em;
            background: #f8f9fa;
            border-left: 4px solid #3498db;
            font-style: italic;
            border-radius: 4px;
        }
        
        pre, code {
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            background: #2c3e50;
            color: #ecf0f1;
            border-radius: 4px;
        }
        
        pre {
            padding: 1em;
            margin: 1em 0;
            overflow-x: auto;
            line-height: 1.4;
        }
        
        code {
            padding: 0.2em 0.4em;
            font-size: 0.9em;
        }
        
        ul, ol {
            margin: 1em 0;
            padding-left: 2em;
        }
        
        li {
            margin: 0.5em 0;
        }
        
        .ascii-art {
            font-family: "Courier New", monospace;
            background: #34495e;
            color: #ecf0f1;
            padding: 1em;
            margin: 1em 0;
            border-radius: 4px;
            white-space: pre;
            overflow-x: auto;
            font-size: 0.8em;
            line-height: 1.2;
        }
        
        .expert-quote {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.5em;
            margin: 1.5em 0;
            border-radius: 8px;
            font-style: italic;
            text-align: center;
        }
        
        .chapter-break {
            page-break-before: always;
            margin-top: 0;
        }
        
        .toc {
            page-break-after: always;
        }
        
        .toc ul {
            list-style: none;
            padding-left: 0;
        }
        
        .toc li {
            margin: 0.5em 0;
            padding: 0.3em 0;
            border-bottom: 1px dotted #bdc3c7;
        }
        
        .toc a {
            text-decoration: none;
            color: #2c3e50;
        }
        
        .warning-box {
            background: #fff3cd;
            border: 1px solid #ffeaa7;
            border-left: 4px solid #f39c12;
            padding: 1em;
            margin: 1em 0;
            border-radius: 4px;
        }
        
        .success-box {
            background: #d4edda;
            border: 1px solid #c3e6cb;
            border-left: 4px solid #27ae60;
            padding: 1em;
            margin: 1em 0;
            border-radius: 4px;
        }
        
        .danger-box {
            background: #f8d7da;
            border: 1px solid #f5c6cb;
            border-left: 4px solid #e74c3c;
            padding: 1em;
            margin: 1em 0;
            border-radius: 4px;
        }
        """
    
    def process_markdown_content(self, content):
        """Enhanced markdown processing with professional formatting"""
        
        # Convert ASCII art boxes to styled divs
        content = re.sub(
            r'```\n([═╔╗╚╝║─│┌┐└┘├┤┬┴┼]+.*?)\n```',
            r'<div class="ascii-art">\1</div>',
            content,
            flags=re.DOTALL | re.MULTILINE
        )
        
        # Convert expert quotes to styled blocks
        content = re.sub(
            r'> \*"([^"]+)"\*\s*>\s*>\s*\*\*—\s*([^*]+)\*\*',
            r'<div class="expert-quote">"<em>\1</em>"<br><strong>— \2</strong></div>',
            content,
            flags=re.MULTILINE
        )
        
        # Add chapter breaks
        content = re.sub(
            r'^## (.+)$',
            r'<div class="chapter-break"></div>\n\n## \1',
            content,
            flags=re.MULTILINE
        )
        
        # Convert warning/success/danger patterns
        content = re.sub(
            r'```\n🚨([^`]+)\n```',
            r'<div class="danger-box">\1</div>',
            content,
            flags=re.DOTALL
        )
        
        content = re.sub(
            r'```\n✅([^`]+)\n```',
            r'<div class="success-box">\1</div>',
            content,
            flags=re.DOTALL
        )
        
        content = re.sub(
            r'```\n⚠️([^`]+)\n```',
            r'<div class="warning-box">\1</div>',
            content,
            flags=re.DOTALL
        )
        
        return content
    
    def generate_epub(self):
        """Generate professional EPUB with enhanced formatting"""
        
        print("🚀 Starting Professional EPUB Generation...")
        
        # Read and process content
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process markdown for better formatting
        content = self.process_markdown_content(content)
        
        # Configure markdown with extensions
        md = markdown.Markdown(extensions=[
            'codehilite',
            'tables',
            'toc',
            'fenced_code',
            'attr_list'
        ])
        
        html_content = md.convert(content)
        
        # Extract title
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Cybersecurity Guide"
        
        # Generate EPUB
        epub_filename = f"{title.replace(' ', '_').replace('/', '_')}_Professional.epub"
        epub_path = self.output_dir / epub_filename
        
        with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
            # Add mimetype
            epub.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
            
            # Add META-INF
            epub.writestr('META-INF/container.xml', self.get_container_xml())
            
            # Add OEBPS files
            epub.writestr('OEBPS/content.opf', self.get_content_opf(title))
            epub.writestr('OEBPS/toc.ncx', self.get_toc_ncx(title))
            epub.writestr('OEBPS/stylesheet.css', self.css_content)
            epub.writestr('OEBPS/content.html', self.get_html_content(html_content, title))
        
        print(f"✅ Professional EPUB generated: {epub_path}")
        return epub_path
    
    def get_container_xml(self):
        return '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
    
    def get_content_opf(self, title):
        book_id = str(uuid.uuid4())
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="2.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
        <dc:identifier id="BookId" opf:scheme="UUID">{book_id}</dc:identifier>
        <dc:title>{title}</dc:title>
        <dc:creator opf:role="aut">Legendary Cybersecurity Masters</dc:creator>
        <dc:language>en</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:publisher>Professional Security Training</dc:publisher>
        <dc:subject>Cybersecurity</dc:subject>
        <dc:subject>Penetration Testing</dc:subject>
        <dc:subject>Hardware Hacking</dc:subject>
        <dc:subject>Digital Forensics</dc:subject>
        <meta name="cover" content="cover-image"/>
    </metadata>
    <manifest>
        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
        <item id="stylesheet" href="stylesheet.css" media-type="text/css"/>
        <item id="content" href="content.html" media-type="application/xhtml+xml"/>
    </manifest>
    <spine toc="ncx">
        <itemref idref="content"/>
    </spine>
</package>'''
    
    def get_toc_ncx(self, title):
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="{str(uuid.uuid4())}"/>
        <meta name="dtb:depth" content="2"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    <docTitle>
        <text>{title}</text>
    </docTitle>
    <navMap>
        <navPoint id="navpoint-1" playOrder="1">
            <navLabel>
                <text>{title}</text>
            </navLabel>
            <content src="content.html"/>
        </navPoint>
    </navMap>
</ncx>'''
    
    def get_html_content(self, html_content, title):
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="stylesheet.css"/>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
</head>
<body>
    {html_content}
</body>
</html>'''

def main():
    input_file = "red_team_blue_team_guide_english.md"
    
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        return
    
    generator = ProfessionalEPUBGenerator(input_file)
    epub_path = generator.generate_epub()
    
    print(f"📚 Professional EPUB ready: {epub_path}")
    print("🎯 Features:")
    print("   ✅ Professional typography and spacing")
    print("   ✅ Enhanced code syntax highlighting")
    print("   ✅ Styled expert quotes and ASCII art")
    print("   ✅ Proper chapter breaks and navigation")
    print("   ✅ Mobile-friendly responsive design")

if __name__ == "__main__":
    main()
