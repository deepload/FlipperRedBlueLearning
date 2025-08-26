#!/usr/bin/env python3
"""
Enhanced EPUB Generator with Superior Formatting
Fixes line spacing, layout issues, and creates professional output
"""

import os
import re
import zipfile
import uuid
from datetime import datetime
from pathlib import Path

class EnhancedEPUBFormatter:
    def __init__(self, input_file, output_dir="epub"):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Professional CSS with fixed spacing
        self.css_content = """
        @namespace epub "http://www.idpf.org/2007/ops";
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        
        body {
            font-family: "Georgia", "Times New Roman", serif;
            font-size: 16px;
            line-height: 1.5;
            color: #2c3e50;
            background: #ffffff;
            margin: 1em;
            text-align: left;
        }
        
        /* Headings with controlled spacing */
        h1 {
            font-family: "Arial", "Helvetica", sans-serif;
            font-size: 2.2em;
            font-weight: bold;
            color: #e74c3c;
            margin: 1.5em 0 0.8em 0;
            padding-bottom: 0.3em;
            border-bottom: 3px solid #3498db;
            page-break-after: avoid;
            line-height: 1.2;
        }
        
        h2 {
            font-family: "Arial", "Helvetica", sans-serif;
            font-size: 1.8em;
            font-weight: bold;
            color: #2980b9;
            margin: 1.2em 0 0.6em 0;
            page-break-after: avoid;
            line-height: 1.3;
        }
        
        h3 {
            font-family: "Arial", "Helvetica", sans-serif;
            font-size: 1.4em;
            font-weight: bold;
            color: #27ae60;
            margin: 1em 0 0.5em 0;
            page-break-after: avoid;
            line-height: 1.3;
        }
        
        h4 {
            font-family: "Arial", "Helvetica", sans-serif;
            font-size: 1.2em;
            font-weight: bold;
            color: #f39c12;
            margin: 0.8em 0 0.4em 0;
            page-break-after: avoid;
            line-height: 1.3;
        }
        
        /* Paragraphs with proper spacing */
        p {
            margin: 0.5em 0;
            text-align: justify;
            text-indent: 0;
            orphans: 2;
            widows: 2;
        }
        
        /* Lists with controlled spacing */
        ul, ol {
            margin: 0.5em 0 0.5em 1.5em;
            padding: 0;
        }
        
        li {
            margin: 0.2em 0;
            line-height: 1.4;
        }
        
        /* Code blocks with minimal spacing */
        pre {
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            background: #2c3e50;
            color: #ecf0f1;
            padding: 0.8em;
            margin: 0.5em 0;
            border-radius: 4px;
            overflow-x: auto;
            line-height: 1.3;
            font-size: 0.9em;
            white-space: pre-wrap;
        }
        
        code {
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            background: #ecf0f1;
            color: #2c3e50;
            padding: 0.1em 0.3em;
            border-radius: 2px;
            font-size: 0.9em;
        }
        
        /* ASCII art boxes */
        .ascii-box {
            font-family: "Courier New", monospace;
            background: #34495e;
            color: #ecf0f1;
            padding: 0.8em;
            margin: 0.5em 0;
            border-radius: 4px;
            white-space: pre;
            overflow-x: auto;
            font-size: 0.8em;
            line-height: 1.1;
            text-align: left;
        }
        
        /* Expert quotes */
        .expert-quote {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1em;
            margin: 0.8em 0;
            border-radius: 6px;
            font-style: italic;
            text-align: center;
            line-height: 1.4;
        }
        
        .expert-quote strong {
            display: block;
            margin-top: 0.5em;
            font-style: normal;
            font-weight: bold;
        }
        
        /* Blockquotes */
        blockquote {
            margin: 0.8em 1em;
            padding: 0.8em;
            background: #f8f9fa;
            border-left: 4px solid #3498db;
            font-style: italic;
            border-radius: 4px;
            line-height: 1.4;
        }
        
        /* Tables */
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 0.5em 0;
        }
        
        th, td {
            border: 1px solid #bdc3c7;
            padding: 0.5em;
            text-align: left;
            line-height: 1.3;
        }
        
        th {
            background: #ecf0f1;
            font-weight: bold;
        }
        
        /* Chapter breaks */
        .chapter-break {
            page-break-before: always;
            margin-top: 0;
        }
        
        /* Remove excessive spacing */
        .no-margin {
            margin: 0 !important;
        }
        
        .tight-spacing {
            margin: 0.2em 0 !important;
        }
        
        /* Warning boxes */
        .warning-box {
            background: #fff3cd;
            border-left: 4px solid #f39c12;
            padding: 0.8em;
            margin: 0.5em 0;
            border-radius: 4px;
            line-height: 1.4;
        }
        
        .success-box {
            background: #d4edda;
            border-left: 4px solid #27ae60;
            padding: 0.8em;
            margin: 0.5em 0;
            border-radius: 4px;
            line-height: 1.4;
        }
        
        .danger-box {
            background: #f8d7da;
            border-left: 4px solid #e74c3c;
            padding: 0.8em;
            margin: 0.5em 0;
            border-radius: 4px;
            line-height: 1.4;
        }
        
        /* Image placeholders */
        .image-placeholder {
            background: #ecf0f1;
            border: 2px dashed #bdc3c7;
            padding: 1em;
            text-align: center;
            margin: 0.5em 0;
            border-radius: 4px;
            color: #7f8c8d;
            font-style: italic;
        }
        """
    
    def clean_markdown_content(self, content):
        """Clean and optimize markdown content for better EPUB formatting"""
        
        # Remove excessive empty lines
        content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
        
        # Convert ASCII art boxes to proper divs
        content = re.sub(
            r'```\n([═╔╗╚╝║─│┌┐└┘├┤┬┴┼🎯🔬📡🛠️⚖️🚨✅⚠️💰📊🎮🔴🔵🟣🟡⚪🏆🥇🥈🥉📎🎆🏛️🔧🧠💾📺🎛️🔋🔌📶🛰️🎨🟢🟡🔴🔵⚪🎯🔬📡📶🛰️🔋🔌🎮🚗🏢🔍🎯📋⏱️👁️📊💡🔄🎯📈🔧🧠💾🤖📊🌍🎯⚡🔒🔍🔬🎯⚡🛡️📊⏰🔍🎯📱🏠🔐🚗🏭🔑🕵️🔍⏰🧩📊🎯📸🔍⏰🧪📊🔒📸🔍⏰🧪📊🎯📋🧪⚖️📋🦅🔧📡📶🛰️🔌🎨🟢🟡🔴🔵⚪🎯🔬📡📶🛰️🔋🔌🎮🚗🏢🔍🎯📋⏱️👁️📊💡🔄🎯📈🔧🧠💾🤖📊🌍🎯⚡🔒🔍🔬🎯⚡🛡️📊⏰🔍🎯📱🏠🔐🚗🏭🔑🕵️🔍⏰🧩📊🎯📸🔍⏰🧪📊🔒📸🔍⏰🧪📊🎯📋🧪⚖️📋\s\w\W]+?)\n```',
            r'<div class="ascii-box">\1</div>',
            content,
            flags=re.DOTALL | re.MULTILINE
        )
        
        # Convert expert quotes
        content = re.sub(
            r'> \*"([^"]+)"\*\s*>\s*>\s*\*\*—\s*([^*]+)\*\*',
            r'<div class="expert-quote">"<em>\1</em>"<strong>— \2</strong></div>',
            content,
            flags=re.MULTILINE
        )
        
        # Convert image placeholders
        content = re.sub(
            r'!\[([^\]]*)\]\([^)]+\)',
            r'<div class="image-placeholder">📷 \1</div>',
            content
        )
        
        # Add chapter breaks for major sections
        content = re.sub(
            r'^## (.+)$',
            r'<div class="chapter-break"></div>\n\n## \1',
            content,
            flags=re.MULTILINE
        )
        
        return content
    
    def markdown_to_html(self, content):
        """Convert markdown to HTML with proper formatting"""
        
        # Headers
        content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
        content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
        content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
        content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', content, flags=re.MULTILINE)
        
        # Bold and italic
        content = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', content)
        content = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', content)
        
        # Code blocks
        content = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code>\2</code></pre>', content, flags=re.DOTALL)
        content = re.sub(r'`([^`]+)`', r'<code>\1</code>', content)
        
        # Lists
        content = re.sub(r'^- (.+)$', r'<li>\1</li>', content, flags=re.MULTILINE)
        content = re.sub(r'(<li>.*</li>)', r'<ul>\1</ul>', content, flags=re.DOTALL)
        content = re.sub(r'</ul>\s*<ul>', '', content)
        
        # Paragraphs
        lines = content.split('\n')
        html_lines = []
        in_paragraph = False
        
        for line in lines:
            line = line.strip()
            if not line:
                if in_paragraph:
                    html_lines.append('</p>')
                    in_paragraph = False
                continue
            
            if line.startswith('<'):
                if in_paragraph:
                    html_lines.append('</p>')
                    in_paragraph = False
                html_lines.append(line)
            else:
                if not in_paragraph:
                    html_lines.append('<p>')
                    in_paragraph = True
                html_lines.append(line)
        
        if in_paragraph:
            html_lines.append('</p>')
        
        return '\n'.join(html_lines)
    
    def generate_epub(self):
        """Generate enhanced EPUB with superior formatting"""
        
        print("🚀 Starting Enhanced EPUB Generation...")
        print("📝 Processing markdown content...")
        
        # Read content
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean and process content
        content = self.clean_markdown_content(content)
        html_content = self.markdown_to_html(content)
        
        # Extract title
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Enhanced Cybersecurity Guide"
        title = re.sub(r'[🎯📖🏆]+\s*', '', title).strip()
        
        # Generate filename
        safe_title = re.sub(r'[^\w\s-]', '', title).strip()
        safe_title = re.sub(r'[-\s]+', '_', safe_title)
        epub_filename = f"{safe_title}_Enhanced.epub"
        epub_path = self.output_dir / epub_filename
        
        print(f"📚 Creating EPUB: {epub_filename}")
        
        # Create EPUB
        with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
            # Mimetype (uncompressed)
            epub.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
            
            # Container
            epub.writestr('META-INF/container.xml', self._get_container_xml())
            
            # Content files
            epub.writestr('OEBPS/content.opf', self._get_content_opf(title))
            epub.writestr('OEBPS/toc.ncx', self._get_toc_ncx(title))
            epub.writestr('OEBPS/stylesheet.css', self.css_content)
            epub.writestr('OEBPS/content.html', self._get_html_wrapper(html_content, title))
        
        print(f"✅ Enhanced EPUB generated successfully!")
        print(f"📍 Location: {epub_path}")
        print("🎯 Improvements:")
        print("   ✅ Fixed line spacing issues")
        print("   ✅ Professional typography")
        print("   ✅ Optimized for e-readers")
        print("   ✅ Enhanced code formatting")
        print("   ✅ Better ASCII art rendering")
        
        return epub_path
    
    def _get_container_xml(self):
        return '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
    
    def _get_content_opf(self, title):
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
        <dc:description>Enhanced professional cybersecurity guide with superior formatting</dc:description>
        <dc:subject>Cybersecurity</dc:subject>
        <dc:subject>Penetration Testing</dc:subject>
        <dc:subject>Hardware Hacking</dc:subject>
        <dc:subject>Digital Forensics</dc:subject>
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
    
    def _get_toc_ncx(self, title):
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="{str(uuid.uuid4())}"/>
        <meta name="dtb:depth" content="3"/>
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
    
    def _get_html_wrapper(self, html_content, title):
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
    
    formatter = EnhancedEPUBFormatter(input_file)
    epub_path = formatter.generate_epub()
    
    print(f"\n🎉 Enhanced EPUB ready for reading!")
    print(f"📱 Optimized for all e-readers and devices")

if __name__ == "__main__":
    main()
