#!/usr/bin/env python3
"""
Enhanced EPUB Generator for Amazon KDP
Converts red_team_blue_team_guide_english.md to professional EPUB format
"""

import os
import re
import uuid
import zipfile
from datetime import datetime
from pathlib import Path
import markdown
from markdown.extensions import codehilite, toc, fenced_code, attr_list, tables

class AmazonKDPEpubGenerator:
    def __init__(self, input_file, output_dir="epub"):
        self.input_file = input_file
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        
        # Book metadata
        self.title = "Complete Red Team & Blue Team Guide"
        self.subtitle = "Using Flipper Zero with Predator Module"
        self.author = "Cybersecurity Training Institute"
        self.publisher = "Professional Security Press"
        self.language = "en"
        self.isbn = "978-0-000000-00-0"  # Placeholder
        self.uuid = str(uuid.uuid4())
        self.creation_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")
        
        # EPUB structure
        self.epub_file = self.output_dir / "Red_Team_Blue_Team_Guide_Professional.epub"
        self.temp_dir = self.output_dir / "temp_epub"
        
    def create_epub_structure(self):
        """Create EPUB directory structure"""
        print("📁 Creating EPUB structure...")
        
        # Clean and create temp directory
        if self.temp_dir.exists():
            import shutil
            shutil.rmtree(self.temp_dir)
        
        # Create EPUB structure
        dirs = [
            self.temp_dir / "META-INF",
            self.temp_dir / "OEBPS" / "content",
            self.temp_dir / "OEBPS" / "styles",
            self.temp_dir / "OEBPS" / "images"
        ]
        
        for dir_path in dirs:
            dir_path.mkdir(parents=True, exist_ok=True)
            
        print("✅ EPUB structure created")
        
    def create_mimetype(self):
        """Create mimetype file"""
        mimetype_path = self.temp_dir / "mimetype"
        with open(mimetype_path, 'w', encoding='utf-8') as f:
            f.write("application/epub+zip")
            
    def create_container_xml(self):
        """Create META-INF/container.xml"""
        container_xml = '''<?xml version="1.0" encoding="UTF-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
    <rootfiles>
        <rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/>
    </rootfiles>
</container>'''
        
        container_path = self.temp_dir / "META-INF" / "container.xml"
        with open(container_path, 'w', encoding='utf-8') as f:
            f.write(container_xml)
            
    def create_css_styles(self):
        """Create professional CSS styles"""
        css_content = '''/* Professional Cybersecurity Guide Styles */

@import url('https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700&family=Roboto+Mono:wght@400;500&display=swap');

/* Base styles */
body {
    font-family: 'Roboto', Arial, sans-serif;
    font-size: 16px;
    line-height: 1.6;
    color: #2c3e50;
    margin: 0;
    padding: 20px;
    background-color: #ffffff;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    font-weight: 500;
    margin-top: 2em;
    margin-bottom: 1em;
    color: #2c3e50;
}

h1 {
    font-size: 2.5em;
    text-align: center;
    border-bottom: 3px solid #e74c3c;
    padding-bottom: 0.5em;
    margin-bottom: 1.5em;
}

h2 {
    font-size: 2em;
    color: #e74c3c;
    border-left: 4px solid #e74c3c;
    padding-left: 15px;
}

h3 {
    font-size: 1.5em;
    color: #3498db;
}

h4 {
    font-size: 1.3em;
    color: #27ae60;
}

/* Code blocks */
pre {
    background-color: #2c3e50;
    color: #ecf0f1;
    padding: 20px;
    border-radius: 8px;
    overflow-x: auto;
    font-family: 'Roboto Mono', monospace;
    font-size: 14px;
    line-height: 1.4;
    margin: 1.5em 0;
    border-left: 4px solid #3498db;
}

code {
    font-family: 'Roboto Mono', monospace;
    background-color: #ecf0f1;
    color: #e74c3c;
    padding: 2px 6px;
    border-radius: 3px;
    font-size: 0.9em;
}

pre code {
    background-color: transparent;
    color: inherit;
    padding: 0;
}

/* Visual boxes and callouts */
.warning-box {
    background-color: #fff3cd;
    border: 1px solid #ffeaa7;
    border-left: 4px solid #f39c12;
    padding: 15px;
    margin: 1.5em 0;
    border-radius: 4px;
}

.info-box {
    background-color: #d1ecf1;
    border: 1px solid #bee5eb;
    border-left: 4px solid #3498db;
    padding: 15px;
    margin: 1.5em 0;
    border-radius: 4px;
}

.success-box {
    background-color: #d4edda;
    border: 1px solid #c3e6cb;
    border-left: 4px solid #27ae60;
    padding: 15px;
    margin: 1.5em 0;
    border-radius: 4px;
}

.danger-box {
    background-color: #f8d7da;
    border: 1px solid #f5c6cb;
    border-left: 4px solid #e74c3c;
    padding: 15px;
    margin: 1.5em 0;
    border-radius: 4px;
}

/* Tables */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 1.5em 0;
    background-color: #ffffff;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

th, td {
    padding: 12px;
    text-align: left;
    border-bottom: 1px solid #ecf0f1;
}

th {
    background-color: #34495e;
    color: #ffffff;
    font-weight: 500;
}

tr:hover {
    background-color: #f8f9fa;
}

/* Lists */
ul, ol {
    margin: 1em 0;
    padding-left: 2em;
}

li {
    margin: 0.5em 0;
}

/* Links */
a {
    color: #3498db;
    text-decoration: none;
}

a:hover {
    text-decoration: underline;
}

/* Images */
img {
    max-width: 100%;
    height: auto;
    display: block;
    margin: 1.5em auto;
    border-radius: 4px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* Page breaks for print/EPUB */
.page-break {
    page-break-before: always;
}

/* Chapter styling */
.chapter {
    page-break-before: always;
    margin-top: 0;
}

/* Table of contents */
.toc {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 8px;
    margin: 2em 0;
}

.toc ul {
    list-style-type: none;
    padding-left: 0;
}

.toc li {
    margin: 0.8em 0;
    padding-left: 1em;
}

.toc a {
    font-weight: 500;
    color: #2c3e50;
}

/* Responsive design */
@media screen and (max-width: 768px) {
    body {
        padding: 10px;
        font-size: 14px;
    }
    
    h1 {
        font-size: 2em;
    }
    
    h2 {
        font-size: 1.5em;
    }
    
    pre {
        font-size: 12px;
        padding: 15px;
    }
}

/* Print styles */
@media print {
    body {
        font-size: 12pt;
        color: #000000;
    }
    
    pre {
        background-color: #f8f9fa !important;
        color: #000000 !important;
        border: 1px solid #dee2e6;
    }
    
    .page-break {
        page-break-before: always;
    }
}

/* Emoji and icon styling */
.emoji {
    font-style: normal;
    font-size: 1.2em;
    margin-right: 0.3em;
}

/* ASCII art preservation */
.ascii-art {
    font-family: 'Roboto Mono', monospace;
    white-space: pre;
    font-size: 12px;
    line-height: 1.2;
    background-color: #f8f9fa;
    padding: 15px;
    border-radius: 4px;
    overflow-x: auto;
}
'''
        
        css_path = self.temp_dir / "OEBPS" / "styles" / "main.css"
        with open(css_path, 'w', encoding='utf-8') as f:
            f.write(css_content)
            
    def process_markdown_content(self):
        """Process markdown content with enhanced formatting"""
        print("📝 Processing markdown content...")
        
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Configure markdown with extensions
        md = markdown.Markdown(extensions=[
            'toc',
            'fenced_code',
            'codehilite',
            'attr_list',
            'tables',
            'nl2br'
        ], extension_configs={
            'toc': {
                'title': 'Table of Contents',
                'anchorlink': True
            },
            'codehilite': {
                'css_class': 'highlight',
                'use_pygments': True
            }
        })
        
        # Process content
        html_content = md.convert(content)
        
        # Extract TOC
        toc_html = md.toc
        
        # Split into chapters
        chapters = self.split_into_chapters(html_content)
        
        return chapters, toc_html
        
    def split_into_chapters(self, html_content):
        """Split content into chapters based on h2 headers"""
        print("📚 Splitting content into chapters...")
        
        # Split by h2 headers (chapters)
        chapter_pattern = r'<h2[^>]*>(.*?)</h2>'
        chapters = []
        
        # Find all chapter headers
        chapter_matches = list(re.finditer(chapter_pattern, html_content, re.IGNORECASE))
        
        if not chapter_matches:
            # If no chapters found, treat as single chapter
            return [("Complete Guide", html_content)]
            
        for i, match in enumerate(chapter_matches):
            start_pos = match.start()
            end_pos = chapter_matches[i + 1].start() if i + 1 < len(chapter_matches) else len(html_content)
            
            chapter_title = re.sub(r'<[^>]+>', '', match.group(1)).strip()
            chapter_content = html_content[start_pos:end_pos]
            
            # Clean chapter title for filename
            clean_title = re.sub(r'[^\w\s-]', '', chapter_title).strip()
            clean_title = re.sub(r'[-\s]+', '_', clean_title)
            
            chapters.append((clean_title, chapter_content))
            
        return chapters
        
    def create_chapter_files(self, chapters):
        """Create individual chapter HTML files"""
        print("📄 Creating chapter files...")
        
        chapter_files = []
        
        for i, (title, content) in enumerate(chapters):
            filename = f"chapter_{i+1:02d}_{title[:30]}.xhtml"
            filepath = self.temp_dir / "OEBPS" / "content" / filename
            
            # Create complete HTML document
            html_doc = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body>
    <div class="chapter">
        {content}
    </div>
</body>
</html>'''
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_doc)
                
            chapter_files.append((filename, title))
            
        return chapter_files
        
    def create_title_page(self):
        """Create title page"""
        title_html = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Title Page</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body>
    <div style="text-align: center; margin-top: 20%;">
        <h1 style="font-size: 3em; margin-bottom: 0.5em; color: #e74c3c;">
            📖 {self.title}
        </h1>
        <h2 style="font-size: 1.5em; color: #3498db; margin-bottom: 2em;">
            🐬 {self.subtitle}
        </h2>
        <h3 style="font-size: 1.2em; color: #27ae60;">
            🎓 Professional Training Course
        </h3>
        <p style="font-size: 1.1em; margin-top: 3em; color: #7f8c8d;">
            by {self.author}
        </p>
        <p style="font-size: 0.9em; color: #95a5a6;">
            {self.publisher}
        </p>
    </div>
</body>
</html>'''
        
        title_path = self.temp_dir / "OEBPS" / "content" / "title.xhtml"
        with open(title_path, 'w', encoding='utf-8') as f:
            f.write(title_html)
            
        return "title.xhtml"
        
    def create_toc_page(self, toc_html):
        """Create table of contents page"""
        toc_page = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>Table of Contents</title>
    <link rel="stylesheet" type="text/css" href="../styles/main.css"/>
    <meta charset="UTF-8"/>
</head>
<body>
    <div class="toc">
        <h1>📋 Table of Contents</h1>
        {toc_html}
    </div>
</body>
</html>'''
        
        toc_path = self.temp_dir / "OEBPS" / "content" / "toc.xhtml"
        with open(toc_path, 'w', encoding='utf-8') as f:
            f.write(toc_page)
            
        return "toc.xhtml"
        
    def create_content_opf(self, chapter_files, title_file, toc_file):
        """Create content.opf manifest"""
        print("📋 Creating content manifest...")
        
        # Generate manifest items
        manifest_items = [
            f'<item id="title" href="content/{title_file}" media-type="application/xhtml+xml"/>',
            f'<item id="toc" href="content/{toc_file}" media-type="application/xhtml+xml"/>',
            '<item id="css" href="styles/main.css" media-type="text/css"/>'
        ]
        
        # Add chapter items
        for i, (filename, title) in enumerate(chapter_files):
            item_id = f"chapter_{i+1:02d}"
            manifest_items.append(
                f'<item id="{item_id}" href="content/{filename}" media-type="application/xhtml+xml"/>'
            )
            
        # Generate spine items
        spine_items = [
            '<itemref idref="title"/>',
            '<itemref idref="toc"/>'
        ]
        
        for i in range(len(chapter_files)):
            spine_items.append(f'<itemref idref="chapter_{i+1:02d}"/>')
            
        content_opf = f'''<?xml version="1.0" encoding="UTF-8"?>
<package xmlns="http://www.idpf.org/2007/opf" unique-identifier="bookid" version="2.0">
    <metadata xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:opf="http://www.idpf.org/2007/opf">
        <dc:title>{self.title}: {self.subtitle}</dc:title>
        <dc:creator opf:role="aut">{self.author}</dc:creator>
        <dc:publisher>{self.publisher}</dc:publisher>
        <dc:language>{self.language}</dc:language>
        <dc:identifier id="bookid" opf:scheme="UUID">{self.uuid}</dc:identifier>
        <dc:identifier opf:scheme="ISBN">{self.isbn}</dc:identifier>
        <dc:date opf:event="creation">{self.creation_date}</dc:date>
        <dc:subject>Cybersecurity</dc:subject>
        <dc:subject>Penetration Testing</dc:subject>
        <dc:subject>Red Team</dc:subject>
        <dc:subject>Blue Team</dc:subject>
        <dc:subject>Flipper Zero</dc:subject>
        <dc:subject>Security Testing</dc:subject>
        <dc:description>
            Complete professional guide for Red Team and Blue Team cybersecurity operations using Flipper Zero with Predator module. 
            Includes practical scenarios, detection strategies, and hands-on examples for security professionals.
        </dc:description>
        <dc:rights>© 2024 Cybersecurity Training Institute. All rights reserved.</dc:rights>
        <meta name="cover" content="cover-image"/>
    </metadata>
    
    <manifest>
        {chr(10).join(manifest_items)}
    </manifest>
    
    <spine toc="ncx">
        {chr(10).join(spine_items)}
    </spine>
    
    <guide>
        <reference type="cover" title="Cover" href="content/{title_file}"/>
        <reference type="toc" title="Table of Contents" href="content/{toc_file}"/>
    </guide>
</package>'''
        
        opf_path = self.temp_dir / "OEBPS" / "content.opf"
        with open(opf_path, 'w', encoding='utf-8') as f:
            f.write(content_opf)
            
    def create_toc_ncx(self, chapter_files):
        """Create toc.ncx navigation file"""
        print("🧭 Creating navigation file...")
        
        nav_points = []
        play_order = 1
        
        # Add title and TOC
        nav_points.append(f'''
        <navPoint id="title" playOrder="{play_order}">
            <navLabel><text>Title Page</text></navLabel>
            <content src="content/title.xhtml"/>
        </navPoint>''')
        play_order += 1
        
        nav_points.append(f'''
        <navPoint id="toc" playOrder="{play_order}">
            <navLabel><text>Table of Contents</text></navLabel>
            <content src="content/toc.xhtml"/>
        </navPoint>''')
        play_order += 1
        
        # Add chapters
        for i, (filename, title) in enumerate(chapter_files):
            nav_points.append(f'''
        <navPoint id="chapter_{i+1:02d}" playOrder="{play_order}">
            <navLabel><text>{title}</text></navLabel>
            <content src="content/{filename}"/>
        </navPoint>''')
            play_order += 1
            
        toc_ncx = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE ncx PUBLIC "-//NISO//DTD ncx 2005-1//EN" "http://www.daisy.org/z3986/2005/ncx-2005-1.dtd">
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
    <head>
        <meta name="dtb:uid" content="{self.uuid}"/>
        <meta name="dtb:depth" content="2"/>
        <meta name="dtb:totalPageCount" content="0"/>
        <meta name="dtb:maxPageNumber" content="0"/>
    </head>
    
    <docTitle>
        <text>{self.title}: {self.subtitle}</text>
    </docTitle>
    
    <navMap>
        {''.join(nav_points)}
    </navMap>
</ncx>'''
        
        ncx_path = self.temp_dir / "OEBPS" / "toc.ncx"
        with open(ncx_path, 'w', encoding='utf-8') as f:
            f.write(toc_ncx)
            
    def create_epub_file(self):
        """Create final EPUB file"""
        print("📦 Creating EPUB file...")
        
        # Remove existing EPUB file
        if self.epub_file.exists():
            self.epub_file.unlink()
            
        # Create EPUB (ZIP) file
        with zipfile.ZipFile(self.epub_file, 'w', zipfile.ZIP_DEFLATED) as epub_zip:
            # Add mimetype first (uncompressed)
            epub_zip.write(
                self.temp_dir / "mimetype", 
                "mimetype", 
                compress_type=zipfile.ZIP_STORED
            )
            
            # Add all other files
            for root, dirs, files in os.walk(self.temp_dir):
                for file in files:
                    if file == "mimetype":
                        continue
                        
                    file_path = Path(root) / file
                    arc_path = file_path.relative_to(self.temp_dir)
                    epub_zip.write(file_path, arc_path)
                    
        print(f"✅ EPUB created: {self.epub_file}")
        
        # Cleanup temp directory
        import shutil
        shutil.rmtree(self.temp_dir)
        
        return self.epub_file
        
    def generate_epub(self):
        """Main method to generate EPUB"""
        print("🚀 Starting EPUB generation...")
        print(f"📖 Input: {self.input_file}")
        print(f"📁 Output: {self.epub_file}")
        
        try:
            # Create EPUB structure
            self.create_epub_structure()
            
            # Create required files
            self.create_mimetype()
            self.create_container_xml()
            self.create_css_styles()
            
            # Process content
            chapters, toc_html = self.process_markdown_content()
            
            # Create content files
            title_file = self.create_title_page()
            toc_file = self.create_toc_page(toc_html)
            chapter_files = self.create_chapter_files(chapters)
            
            # Create manifest and navigation
            self.create_content_opf(chapter_files, title_file, toc_file)
            self.create_toc_ncx(chapter_files)
            
            # Create final EPUB
            epub_path = self.create_epub_file()
            
            # Display results
            file_size = epub_path.stat().st_size / (1024 * 1024)
            print(f"\n🎉 EPUB Generation Complete!")
            print(f"📁 File: {epub_path}")
            print(f"📊 Size: {file_size:.2f} MB")
            print(f"📚 Chapters: {len(chapters)}")
            print(f"🏷️ Title: {self.title}")
            print(f"👤 Author: {self.author}")
            
            # Create command for re-execution
            command = f'python enhanced_epub_generator.py'
            print(f"\n🔄 Re-execution command:")
            print(f"   {command}")
            
            return epub_path
            
        except Exception as e:
            print(f"❌ Error generating EPUB: {e}")
            raise

def main():
    """Main function"""
    input_file = "red_team_blue_team_guide_english.md"
    output_dir = "epub"
    
    if not os.path.exists(input_file):
        print(f"❌ Input file not found: {input_file}")
        return
        
    generator = AmazonKDPEpubGenerator(input_file, output_dir)
    generator.generate_epub()

if __name__ == "__main__":
    main()
