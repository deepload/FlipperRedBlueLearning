#!/usr/bin/env python3
"""
Diagram EPUB Generator - Converts ASCII art to styled visual elements
No external dependencies required
"""

import os
import re
import zipfile
import uuid
from datetime import datetime
from pathlib import Path

class DiagramEPUBGenerator:
    def __init__(self, input_file, output_dir="epub"):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Enhanced CSS with diagram styling
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
        
        p {
            margin: 0.3em 0;
            text-align: justify;
            text-indent: 0;
            orphans: 2;
            widows: 2;
        }
        
        ul, ol {
            margin: 0.3em 0 0.3em 1.5em;
            padding: 0;
        }
        
        li {
            margin: 0.1em 0;
            line-height: 1.3;
        }
        
        pre {
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            background: #2c3e50 !important;
            color: #ffffff !important;
            padding: 0.8em;
            margin: 0.3em 0;
            border-radius: 4px;
            overflow-x: auto;
            line-height: 1.2;
            font-size: 0.9em;
            white-space: pre-wrap;
            border: 1px solid #34495e;
        }
        
        pre code {
            background: transparent !important;
            color: #ffffff !important;
            padding: 0;
        }
        
        pre * {
            color: #ffffff !important;
        }
        
        code {
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            background: #f8f9fa;
            color: #2c3e50;
            padding: 0.1em 0.3em;
            border-radius: 2px;
            font-size: 0.9em;
            border: 1px solid #dee2e6;
        }
        
        /* Professional diagram styling */
        .diagram-container {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border: 3px solid #3498db;
            border-radius: 12px;
            margin: 1.5em 0;
            padding: 0;
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
            overflow: hidden;
        }
        
        .diagram-header {
            background: rgba(44, 62, 80, 0.9);
            color: #ecf0f1;
            padding: 0.8em 1.2em;
            font-family: "Arial", "Helvetica", sans-serif;
            font-weight: bold;
            font-size: 1.1em;
            text-align: center;
            border-bottom: 2px solid #3498db;
        }
        
        .diagram-content {
            font-family: "Consolas", "Monaco", "Courier New", monospace;
            background: #ffffff;
            color: #2c3e50;
            padding: 1.2em;
            line-height: 1.4;
            font-size: 0.9em;
            white-space: pre;
            overflow-x: auto;
            border: 2px solid rgba(52, 152, 219, 0.3);
            margin: 0.5em;
            border-radius: 6px;
            text-shadow: none;
        }
        
        .framework-diagram {
            background: linear-gradient(135deg, #ff6b6b 0%, #ee5a24 100%);
        }
        
        .matrix-diagram {
            background: linear-gradient(135deg, #4834d4 0%, #686de0 100%);
        }
        
        .methodology-diagram {
            background: linear-gradient(135deg, #00d2d3 0%, #54a0ff 100%);
        }
        
        .architecture-diagram {
            background: linear-gradient(135deg, #5f27cd 0%, #a55eea 100%);
        }
        
        .checklist-diagram {
            background: linear-gradient(135deg, #00d84a 0%, #05c46b 100%);
        }
        
        .specifications-diagram {
            background: linear-gradient(135deg, #fd79a8 0%, #fdcb6e 100%);
        }
        
        .expert-quote {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 1.2em;
            margin: 1em 0;
            border-radius: 8px;
            font-style: italic;
            text-align: center;
            line-height: 1.4;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .expert-quote strong {
            display: block;
            margin-top: 0.5em;
            font-style: normal;
            font-weight: bold;
        }
        
        blockquote {
            margin: 0.8em 1em;
            padding: 0.8em;
            background: #f8f9fa;
            border-left: 4px solid #3498db;
            font-style: italic;
            border-radius: 4px;
            line-height: 1.4;
        }
        
        .chapter-break {
            page-break-before: always;
            margin-top: 0;
        }
        
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
        """
    
    def convert_ascii_to_diagram(self, ascii_content):
        """Convert ASCII art to styled diagram"""
        
        # Determine diagram type and styling
        diagram_type = "diagram"
        title = "Security Diagram"
        
        if "FRAMEWORK" in ascii_content.upper():
            diagram_type = "framework-diagram"
            title = "🏗️ Security Framework"
        elif "MATRIX" in ascii_content.upper():
            diagram_type = "matrix-diagram"
            title = "📊 Security Matrix"
        elif "METHODOLOGY" in ascii_content.upper():
            diagram_type = "methodology-diagram"
            title = "🔬 Methodology Overview"
        elif "ARCHITECTURE" in ascii_content.upper():
            diagram_type = "architecture-diagram"
            title = "🏛️ System Architecture"
        elif "CHECKLIST" in ascii_content.upper():
            diagram_type = "checklist-diagram"
            title = "✅ Security Checklist"
        elif "SPECIFICATIONS" in ascii_content.upper():
            diagram_type = "specifications-diagram"
            title = "⚙️ Technical Specifications"
        elif "ANALYSIS" in ascii_content.upper():
            diagram_type = "methodology-diagram"
            title = "🔍 Analysis Framework"
        elif "PLATFORM" in ascii_content.upper():
            diagram_type = "architecture-diagram"
            title = "🚀 Platform Overview"
        
        # Clean up ASCII content for better display
        clean_content = self.clean_ascii_content(ascii_content)
        
        return f'''<div class="diagram-container {diagram_type}">
    <div class="diagram-header">{title}</div>
    <div class="diagram-content">{clean_content}</div>
</div>'''
    
    def clean_ascii_content(self, content):
        """Clean ASCII content for better visual presentation"""
        
        # Replace Unicode box drawing with ASCII equivalents for better compatibility
        replacements = {
            '═': '=', '║': '|', '╔': '+', '╗': '+', '╚': '+', '╝': '+',
            '╠': '+', '╣': '+', '╦': '+', '╩': '+', '╬': '+',
            '─': '-', '│': '|', '┌': '+', '┐': '+', '└': '+', '┘': '+',
            '├': '+', '┤': '+', '┬': '+', '┴': '+', '┼': '+'
        }
        
        # Replace emojis with text equivalents for better compatibility
        emoji_replacements = {
            '🎯': '[TARGET]', '🔬': '[ANALYSIS]', '📡': '[RF]', 
            '🛠️': '[TOOLS]', '⚖️': '[LEGAL]', '🚨': '[ALERT]',
            '✅': '[OK]', '⚠️': '[WARN]', '💰': '[COST]', '📊': '[DATA]',
            '🎮': '[SCENARIO]', '🔴': '[RED]', '🔵': '[BLUE]', '🟣': '[PURPLE]',
            '🟡': '[YELLOW]', '⚪': '[WHITE]', '🏆': '[AWARD]', '🥇': '[GOLD]',
            '🥈': '[SILVER]', '🥉': '[BRONZE]', '📎': '[PLATINUM]',
            '🐬': '[FLIPPER]', '🦅': '[PREDATOR]', '📶': '[WIFI]', '🛰️': '[GPS]',
            '🔋': '[BATTERY]', '🔌': '[POWER]', '🧠': '[CPU]', '💾': '[MEMORY]',
            '🌊': '[SPECTRUM]', '🔍': '[SEARCH]', '🕵️': '[DETECTIVE]', '⏰': '[TIME]',
            '🧩': '[PUZZLE]', '📸': '[CAMERA]', '🧪': '[LAB]', '📋': '[CHECKLIST]'
        }
        
        # Apply replacements
        for old, new in replacements.items():
            content = content.replace(old, new)
        
        for old, new in emoji_replacements.items():
            content = content.replace(old, new)
        
        return content
    
    def process_content(self, content):
        """Process markdown content and convert ASCII diagrams"""
        
        # Remove excessive empty lines
        content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
        
        # Convert ASCII diagrams to styled containers
        def replace_ascii_diagram(match):
            ascii_content = match.group(1)
            
            # Skip if it's just regular code without diagram characters
            if not any(char in ascii_content for char in '═║╔╗╚╝╠╣╦╩╬─│┌┐└┘├┤┬┴┼'):
                return f'<pre><code>{ascii_content}</code></pre>'
            
            return self.convert_ascii_to_diagram(ascii_content)
        
        # Replace ASCII art blocks with styled diagrams
        content = re.sub(
            r'```\n([═╔╗╚╝║─│┌┐└┘├┤┬┴┼🎯🔬📡🛠️⚖️🚨✅⚠️💰📊🎮🔴🔵🟣🟡⚪🏆🥇🥈🥉📎🐬🦅📶🛰️🔋🔌🧠💾🌊🔍🕵️⏰🧩📸🧪📋\s\w\W]*?)\n```',
            replace_ascii_diagram,
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
        
        # Convert placeholder images
        content = re.sub(
            r'!\[([^\]]*)\]\([^)]+\)',
            r'<div class="diagram-container"><div class="diagram-header">📷 \1</div></div>',
            content
        )
        
        # Add chapter breaks
        content = re.sub(
            r'^## (.+)$',
            r'<div class="chapter-break"></div>\n\n## \1',
            content,
            flags=re.MULTILINE
        )
        
        return content
    
    def markdown_to_html(self, content):
        """Convert markdown to HTML"""
        
        # Headers
        content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
        content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
        content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
        content = re.sub(r'^#### (.+)$', r'<h4>\1</h4>', content, flags=re.MULTILINE)
        
        # Bold and italic
        content = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', content)
        content = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', content)
        
        # Code blocks (remaining ones)
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
        """Generate EPUB with professional diagram styling"""
        
        print("🚀 Starting Diagram EPUB Generation...")
        print("🎨 Converting ASCII diagrams to professional visuals...")
        
        # Read content
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process content
        content = self.process_content(content)
        html_content = self.markdown_to_html(content)
        
        # Extract title
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Professional Cybersecurity Guide"
        title = re.sub(r'[🎯📖🏆]+\s*', '', title).strip()
        
        # Generate filename
        safe_title = re.sub(r'[^\w\s-]', '', title).strip()
        safe_title = re.sub(r'[-\s]+', '_', safe_title)
        epub_filename = f"{safe_title}_Professional.epub"
        epub_path = self.output_dir / epub_filename
        
        print(f"📚 Creating Professional EPUB: {epub_filename}")
        
        # Create EPUB
        with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
            # Mimetype
            epub.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
            
            # Container
            epub.writestr('META-INF/container.xml', self._get_container_xml())
            
            # Content files
            epub.writestr('OEBPS/content.opf', self._get_content_opf(title))
            epub.writestr('OEBPS/toc.ncx', self._get_toc_ncx(title))
            epub.writestr('OEBPS/stylesheet.css', self.css_content)
            epub.writestr('OEBPS/content.html', self._get_html_wrapper(html_content, title))
        
        print(f"✅ Professional EPUB generated successfully!")
        print(f"📍 Location: {epub_path}")
        print("🎯 Professional Features:")
        print("   ✅ ASCII diagrams converted to styled visuals")
        print("   ✅ Color-coded diagram types")
        print("   ✅ Professional typography and spacing")
        print("   ✅ Enhanced readability on all devices")
        
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
        <dc:description>Professional cybersecurity guide with enhanced visual diagrams</dc:description>
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
    
    generator = DiagramEPUBGenerator(input_file)
    epub_path = generator.generate_epub()
    
    print(f"\n🎉 Professional EPUB ready with enhanced diagrams!")

if __name__ == "__main__":
    main()
