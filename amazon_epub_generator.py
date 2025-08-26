#!/usr/bin/env python3
"""
Amazon EPUB Generator for Red Team & Blue Team Guide
Converts the enhanced markdown guide to a professional EPUB format suitable for Amazon publishing.
"""

import os
import re
import uuid
from datetime import datetime
from ebooklib import epub
import markdown
from markdown.extensions import codehilite, toc, tables, fenced_code

class AmazonEpubGenerator:
    def __init__(self, input_file, output_dir="output2"):
        self.input_file = input_file
        self.output_dir = output_dir
        self.book_title = "Red Team & Blue Team Guide: Professional Cybersecurity Testing with Flipper Zero"
        self.author = "Cybersecurity Professional"
        self.book_id = str(uuid.uuid4())
        self.language = "en"
        self.publisher = "Independent"
        
        # Ensure output directory exists
        os.makedirs(output_dir, exist_ok=True)
        
        # Initialize markdown processor with extensions
        self.md = markdown.Markdown(extensions=[
            'codehilite',
            'toc',
            'tables',
            'fenced_code',
            'attr_list'
        ])
    
    def read_markdown_content(self):
        """Read and preprocess the markdown content."""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Clean up any remaining formatting issues
        content = self._clean_content(content)
        return content
    
    def _clean_content(self, content):
        """Clean and prepare content for EPUB conversion."""
        # Remove any remaining emoji headers that might cause issues
        content = re.sub(r'#{1,6}\s*[🔴🔵🟡⚫⚪🟢🟠🟣🔶🔷🔸🔹💻📱🌐🔒🔓📊📈📉💡⚡🛡️🎯📝📚💼🚨]\s*', '', content)
        
        # Ensure proper chapter numbering
        content = re.sub(r'^## (Chapter \d+:)', r'# \1', content, flags=re.MULTILINE)
        
        # Fix code blocks for better EPUB rendering
        content = re.sub(r'```(\w+)?\n', r'```\1\n', content)
        
        # Ensure proper spacing around headers
        content = re.sub(r'\n(#{1,6})', r'\n\n\1', content)
        content = re.sub(r'(#{1,6}.*)\n([^#\n])', r'\1\n\n\2', content)
        
        return content
    
    def split_into_chapters(self, content):
        """Split content into chapters for better EPUB structure."""
        # Split by main chapters (# Chapter X:)
        chapters = re.split(r'\n(?=# Chapter \d+:)', content)
        
        # Handle introduction and appendix
        if not chapters[0].startswith('# Chapter'):
            intro = chapters.pop(0)
            chapters.insert(0, intro)
        
        processed_chapters = []
        for i, chapter in enumerate(chapters):
            if chapter.strip():
                if i == 0 and not chapter.startswith('# Chapter'):
                    # This is the introduction
                    chapter_title = "Introduction"
                    chapter_content = f"# Introduction\n\n{chapter}"
                else:
                    # Extract chapter title
                    title_match = re.match(r'# (Chapter \d+: .+)', chapter)
                    if title_match:
                        chapter_title = title_match.group(1)
                    else:
                        chapter_title = f"Chapter {i}"
                    chapter_content = chapter
                
                processed_chapters.append((chapter_title, chapter_content))
        
        return processed_chapters
    
    def create_epub(self):
        """Create the EPUB file."""
        print(f"Creating EPUB: {self.book_title}")
        
        # Create EPUB book
        book = epub.EpubBook()
        
        # Set metadata
        book.set_identifier(self.book_id)
        book.set_title(self.book_title)
        book.set_language(self.language)
        book.add_author(self.author)
        book.add_metadata('DC', 'publisher', self.publisher)
        book.add_metadata('DC', 'description', 
                         'Comprehensive guide for Red Team and Blue Team cybersecurity operations using Flipper Zero with Predator module. Covers advanced RF and WiFi attack techniques, detection strategies, forensic analysis, and defensive countermeasures.')
        book.add_metadata('DC', 'subject', 'Cybersecurity')
        book.add_metadata('DC', 'subject', 'Penetration Testing')
        book.add_metadata('DC', 'subject', 'Red Team')
        book.add_metadata('DC', 'subject', 'Blue Team')
        book.add_metadata('DC', 'subject', 'Flipper Zero')
        book.add_metadata('DC', 'rights', 'All rights reserved')
        book.add_metadata('DC', 'date', datetime.now().strftime('%Y-%m-%d'))
        
        # Read and process content
        content = self.read_markdown_content()
        chapters = self.split_into_chapters(content)
        
        # Create CSS for better formatting
        css_content = self._create_css()
        nav_css = epub.EpubItem(uid="nav_css", 
                               file_name="style/nav.css", 
                               media_type="text/css", 
                               content=css_content)
        book.add_item(nav_css)
        
        # Create chapters
        epub_chapters = []
        toc_entries = []
        
        for i, (title, chapter_content) in enumerate(chapters):
            # Convert markdown to HTML
            html_content = self.md.convert(chapter_content)
            
            # Create chapter
            chapter_file = f"chapter_{i+1}.xhtml"
            chapter = epub.EpubHtml(title=title, 
                                  file_name=chapter_file, 
                                  lang=self.language)
            
            # Wrap in proper HTML structure
            chapter.content = f'''<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="style/nav.css"/>
</head>
<body>
{html_content}
</body>
</html>'''
            
            book.add_item(chapter)
            epub_chapters.append(chapter)
            toc_entries.append(chapter)
        
        # Create table of contents
        book.toc = toc_entries
        
        # Add navigation files
        book.add_item(epub.EpubNcx())
        book.add_item(epub.EpubNav())
        
        # Create spine
        book.spine = ['nav'] + epub_chapters
        
        # Generate EPUB file
        output_file = os.path.join(self.output_dir, "Red_Team_Blue_Team_Guide_Professional.epub")
        epub.write_epub(output_file, book, {})
        
        print(f"EPUB created successfully: {output_file}")
        return output_file
    
    def _create_css(self):
        """Create CSS for professional EPUB formatting."""
        return '''
/* Professional EPUB Styling for Amazon */
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

blockquote {
    border-left: 4px solid #3498db;
    margin: 1em 0;
    padding-left: 1em;
    font-style: italic;
    color: #555;
}

table {
    border-collapse: collapse;
    width: 100%;
    margin: 1em 0;
}

th, td {
    border: 1px solid #ddd;
    padding: 0.5em;
    text-align: left;
}

th {
    background-color: #f2f2f2;
    font-weight: bold;
}

strong {
    font-weight: bold;
    color: #2c3e50;
}

em {
    font-style: italic;
}

.chapter-title {
    text-align: center;
    margin-bottom: 2em;
}

.code-block {
    page-break-inside: avoid;
}

/* Amazon-specific optimizations */
@media amzn-mobi {
    body {
        font-size: 1em;
    }
    
    pre {
        font-size: 0.8em;
    }
}

@media amzn-kf8 {
    body {
        font-size: 1em;
    }
}
'''

def main():
    """Main function to generate EPUB."""
    input_file = "enhanced_guide.md"
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found!")
        return
    
    generator = AmazonEpubGenerator(input_file)
    
    try:
        output_file = generator.create_epub()
        
        # Create publishing info
        info_content = f"""EPUB Generation Complete
========================

File: {output_file}
Title: {generator.book_title}
Author: {generator.author}
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

File size: {os.path.getsize(output_file) / 1024:.1f} KB
"""
        
        with open(os.path.join(generator.output_dir, "publishing_info.txt"), 'w', encoding='utf-8') as f:
            f.write(info_content)
        
        print("\n" + "="*50)
        print("EPUB GENERATION SUCCESSFUL!")
        print("="*50)
        print(info_content)
        
    except Exception as e:
        print(f"Error generating EPUB: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
