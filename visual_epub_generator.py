#!/usr/bin/env python3
"""
Visual EPUB Generator with ASCII-to-Image Conversion
Converts ASCII diagrams and schemas into professional images
"""

import os
import re
import zipfile
import uuid
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import io
import base64

class VisualEPUBGenerator:
    def __init__(self, input_file, output_dir="epub"):
        self.input_file = Path(input_file)
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.images_dir = self.output_dir / "images"
        self.images_dir.mkdir(exist_ok=True)
        
        # Image generation settings
        self.font_size = 14
        self.line_height = 18
        self.padding = 20
        self.bg_color = (44, 62, 80)  # Dark blue
        self.text_color = (236, 240, 241)  # Light gray
        self.border_color = (52, 152, 219)  # Blue
        
        # Professional CSS with image support
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
            margin: 0.5em 0;
            text-align: justify;
            text-indent: 0;
            orphans: 2;
            widows: 2;
        }
        
        ul, ol {
            margin: 0.5em 0 0.5em 1.5em;
            padding: 0;
        }
        
        li {
            margin: 0.2em 0;
            line-height: 1.4;
        }
        
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
        
        .diagram-image {
            display: block;
            max-width: 100%;
            height: auto;
            margin: 1em auto;
            border: 2px solid #3498db;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        
        .diagram-caption {
            text-align: center;
            font-style: italic;
            color: #7f8c8d;
            margin: 0.5em 0 1em 0;
            font-size: 0.9em;
        }
        
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
    
    def create_ascii_image(self, ascii_text, image_name):
        """Convert ASCII art to a professional image"""
        
        lines = ascii_text.strip().split('\n')
        max_width = max(len(line) for line in lines) if lines else 50
        
        # Calculate image dimensions
        char_width = 8
        img_width = max_width * char_width + (self.padding * 2)
        img_height = len(lines) * self.line_height + (self.padding * 2)
        
        # Create image
        img = Image.new('RGB', (img_width, img_height), self.bg_color)
        draw = ImageDraw.Draw(img)
        
        # Try to use a monospace font, fallback to default
        try:
            font = ImageFont.truetype("consola.ttf", self.font_size)
        except:
            try:
                font = ImageFont.truetype("DejaVuSansMono.ttf", self.font_size)
            except:
                font = ImageFont.load_default()
        
        # Draw border
        border_width = 2
        draw.rectangle([0, 0, img_width-1, img_height-1], 
                      outline=self.border_color, width=border_width)
        
        # Draw text
        y_pos = self.padding
        for line in lines:
            # Clean up the line (remove excessive Unicode characters)
            clean_line = self.clean_ascii_line(line)
            draw.text((self.padding, y_pos), clean_line, 
                     fill=self.text_color, font=font)
            y_pos += self.line_height
        
        # Save image
        image_path = self.images_dir / f"{image_name}.png"
        img.save(image_path, "PNG", optimize=True)
        
        return f"images/{image_name}.png"
    
    def clean_ascii_line(self, line):
        """Clean ASCII line for better image rendering"""
        # Replace box drawing characters with simpler alternatives
        replacements = {
            '═': '=', '║': '|', '╔': '+', '╗': '+', '╚': '+', '╝': '+',
            '╠': '+', '╣': '+', '╦': '+', '╩': '+', '╬': '+',
            '─': '-', '│': '|', '┌': '+', '┐': '+', '└': '+', '┘': '+',
            '├': '+', '┤': '+', '┬': '+', '┴': '+', '┼': '+',
            '🎯': '[TARGET]', '🔬': '[ANALYSIS]', '📡': '[RF]', 
            '🛠️': '[TOOLS]', '⚖️': '[LEGAL]', '🚨': '[ALERT]',
            '✅': '[OK]', '⚠️': '[WARN]', '💰': '[COST]', '📊': '[DATA]',
            '🎮': '[SCENARIO]', '🔴': '[RED]', '🔵': '[BLUE]', '🟣': '[PURPLE]',
            '🟡': '[YELLOW]', '⚪': '[WHITE]', '🏆': '[AWARD]', '🥇': '[GOLD]',
            '🥈': '[SILVER]', '🥉': '[BRONZE]', '📎': '[PLATINUM]'
        }
        
        for old, new in replacements.items():
            line = line.replace(old, new)
        
        return line
    
    def extract_ascii_diagrams(self, content):
        """Extract ASCII diagrams and convert them to images"""
        
        image_counter = 0
        
        def replace_ascii_with_image(match):
            nonlocal image_counter
            ascii_content = match.group(1)
            
            # Skip if it's just text without diagram characters
            if not any(char in ascii_content for char in '═║╔╗╚╝╠╣╦╩╬─│┌┐└┘├┤┬┴┼'):
                return match.group(0)  # Return original
            
            image_counter += 1
            image_name = f"diagram_{image_counter:03d}"
            image_path = self.create_ascii_image(ascii_content, image_name)
            
            # Extract caption if available
            caption = ""
            if "FRAMEWORK" in ascii_content:
                caption = "Security Framework Diagram"
            elif "MATRIX" in ascii_content:
                caption = "Security Matrix"
            elif "METHODOLOGY" in ascii_content:
                caption = "Methodology Overview"
            elif "ARCHITECTURE" in ascii_content:
                caption = "System Architecture"
            elif "CHECKLIST" in ascii_content:
                caption = "Security Checklist"
            elif "SPECIFICATIONS" in ascii_content:
                caption = "Technical Specifications"
            else:
                caption = f"Security Diagram {image_counter}"
            
            return f'<img src="{image_path}" alt="{caption}" class="diagram-image"/>\n<p class="diagram-caption">{caption}</p>'
        
        # Replace ASCII art blocks with images
        content = re.sub(
            r'```\n([═╔╗╚╝║─│┌┐└┘├┤┬┴┼🎯🔬📡🛠️⚖️🚨✅⚠️💰📊🎮🔴🔵🟣🟡⚪🏆🥇🥈🥉📎\s\w\W]*?)\n```',
            replace_ascii_with_image,
            content,
            flags=re.DOTALL | re.MULTILINE
        )
        
        return content
    
    def process_content(self, content):
        """Process markdown content with image conversion"""
        
        # Remove excessive empty lines
        content = re.sub(r'\n\s*\n\s*\n+', '\n\n', content)
        
        # Convert ASCII diagrams to images
        content = self.extract_ascii_diagrams(content)
        
        # Convert expert quotes
        content = re.sub(
            r'> \*"([^"]+)"\*\s*>\s*>\s*\*\*—\s*([^*]+)\*\*',
            r'<div class="expert-quote">"<em>\1</em>"<strong>— \2</strong></div>',
            content,
            flags=re.MULTILINE
        )
        
        # Convert placeholder images to styled divs
        content = re.sub(
            r'!\[([^\]]*)\]\([^)]+\)',
            r'<div class="diagram-caption">📷 \1</div>',
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
        """Generate visual EPUB with converted diagrams"""
        
        print("🚀 Starting Visual EPUB Generation...")
        print("🎨 Converting ASCII diagrams to images...")
        
        # Read content
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Process content and convert diagrams
        content = self.process_content(content)
        html_content = self.markdown_to_html(content)
        
        # Extract title
        title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
        title = title_match.group(1) if title_match else "Visual Cybersecurity Guide"
        title = re.sub(r'[🎯📖🏆]+\s*', '', title).strip()
        
        # Generate filename
        safe_title = re.sub(r'[^\w\s-]', '', title).strip()
        safe_title = re.sub(r'[-\s]+', '_', safe_title)
        epub_filename = f"{safe_title}_Visual.epub"
        epub_path = self.output_dir / epub_filename
        
        print(f"📚 Creating Visual EPUB: {epub_filename}")
        
        # Create EPUB with images
        with zipfile.ZipFile(epub_path, 'w', zipfile.ZIP_DEFLATED) as epub:
            # Mimetype
            epub.writestr('mimetype', 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
            
            # Container
            epub.writestr('META-INF/container.xml', self._get_container_xml())
            
            # Add all generated images
            image_files = []
            for img_file in self.images_dir.glob("*.png"):
                epub.write(img_file, f"OEBPS/images/{img_file.name}")
                image_files.append(img_file.name)
            
            # Content files
            epub.writestr('OEBPS/content.opf', self._get_content_opf(title, image_files))
            epub.writestr('OEBPS/toc.ncx', self._get_toc_ncx(title))
            epub.writestr('OEBPS/stylesheet.css', self.css_content)
            epub.writestr('OEBPS/content.html', self._get_html_wrapper(html_content, title))
        
        print(f"✅ Visual EPUB generated successfully!")
        print(f"📍 Location: {epub_path}")
        print("🎯 Visual Enhancements:")
        print(f"   ✅ {len(list(self.images_dir.glob('*.png')))} ASCII diagrams converted to images")
        print("   ✅ Professional diagram styling")
        print("   ✅ Enhanced visual presentation")
        print("   ✅ E-reader optimized images")
        
        return epub_path
    
    def _get_container_xml(self):
        return '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
    
    def _get_content_opf(self, title, image_files):
        book_id = str(uuid.uuid4())
        
        # Generate image manifest items
        image_items = ""
        for img_file in image_files:
            img_id = img_file.replace('.png', '').replace('-', '_')
            image_items += f'        <item id="img_{img_id}" href="images/{img_file}" media-type="image/png"/>\n'
        
        return f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="BookId" version="2.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
        <dc:identifier id="BookId" opf:scheme="UUID">{book_id}</dc:identifier>
        <dc:title>{title}</dc:title>
        <dc:creator opf:role="aut">Legendary Cybersecurity Masters</dc:creator>
        <dc:language>en</dc:language>
        <dc:date>{datetime.now().strftime('%Y-%m-%d')}</dc:date>
        <dc:publisher>Professional Security Training</dc:publisher>
        <dc:description>Visual cybersecurity guide with professional diagrams</dc:description>
        <dc:subject>Cybersecurity</dc:subject>
        <dc:subject>Penetration Testing</dc:subject>
        <dc:subject>Hardware Hacking</dc:subject>
        <dc:subject>Digital Forensics</dc:subject>
    </metadata>
    <manifest>
        <item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>
        <item id="stylesheet" href="stylesheet.css" media-type="text/css"/>
        <item id="content" href="content.html" media-type="application/xhtml+xml"/>
{image_items}    </manifest>
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
    
    generator = VisualEPUBGenerator(input_file)
    epub_path = generator.generate_epub()
    
    print(f"\n🎉 Visual EPUB ready with professional diagrams!")
    print(f"📱 All ASCII art converted to high-quality images")

if __name__ == "__main__":
    main()
