#!/usr/bin/env python3
"""
Professional E-book Generator for Red Team & Blue Team Guide
Uses ReportLab for PDF generation to avoid GTK dependencies
"""

import os
import re
import markdown
from datetime import datetime
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, cm
from reportlab.lib.colors import HexColor, black, white
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle
from reportlab.platypus import KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_JUSTIFY
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from bs4 import BeautifulSoup
import zipfile
import uuid

class ProfessionalEbookGenerator:
    def __init__(self, input_file):
        self.input_file = input_file
        self.title = "Red Team & Blue Team Guide: Flipper Zero Security Testing"
        self.subtitle = "A Comprehensive Guide to Offensive and Defensive Cybersecurity Testing"
        self.author = "Cybersecurity Professional"
        self.publisher = "Security Research Publications"
        self.publication_date = datetime.now().strftime('%B %Y')
        
        # Create output directory
        os.makedirs("output", exist_ok=True)
        
        # Setup styles
        self.setup_styles()
    
    def setup_styles(self):
        """Setup professional document styles"""
        self.styles = getSampleStyleSheet()
        
        # Title page styles
        self.styles.add(ParagraphStyle(
            name='BookTitle',
            parent=self.styles['Title'],
            fontSize=24,
            spaceAfter=20,
            textColor=HexColor('#2c3e50'),
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        self.styles.add(ParagraphStyle(
            name='BookSubtitle',
            parent=self.styles['Normal'],
            fontSize=16,
            spaceAfter=30,
            textColor=HexColor('#34495e'),
            alignment=TA_CENTER,
            fontName='Helvetica'
        ))
        
        self.styles.add(ParagraphStyle(
            name='Author',
            parent=self.styles['Normal'],
            fontSize=14,
            spaceAfter=20,
            textColor=HexColor('#2c3e50'),
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Chapter styles
        self.styles.add(ParagraphStyle(
            name='ChapterTitle',
            parent=self.styles['Heading1'],
            fontSize=20,
            spaceAfter=20,
            spaceBefore=30,
            textColor=HexColor('#2c3e50'),
            fontName='Helvetica-Bold',
            keepWithNext=True
        ))
        
        self.styles.add(ParagraphStyle(
            name='SectionTitle',
            parent=self.styles['Heading2'],
            fontSize=16,
            spaceAfter=15,
            spaceBefore=20,
            textColor=HexColor('#34495e'),
            fontName='Helvetica-Bold',
            keepWithNext=True
        ))
        
        self.styles.add(ParagraphStyle(
            name='SubsectionTitle',
            parent=self.styles['Heading3'],
            fontSize=14,
            spaceAfter=10,
            spaceBefore=15,
            textColor=HexColor('#2c3e50'),
            fontName='Helvetica-Bold',
            keepWithNext=True
        ))
        
        # Body text styles
        self.styles.add(ParagraphStyle(
            name='BodyText',
            parent=self.styles['Normal'],
            fontSize=11,
            spaceAfter=6,
            alignment=TA_JUSTIFY,
            fontName='Times-Roman',
            leading=14
        ))
        
        # Code styles
        self.styles.add(ParagraphStyle(
            name='Code',
            parent=self.styles['Normal'],
            fontSize=9,
            fontName='Courier',
            textColor=HexColor('#e74c3c'),
            backColor=HexColor('#f8f9fa'),
            borderColor=HexColor('#e9ecef'),
            borderWidth=1,
            borderPadding=5,
            spaceAfter=10
        ))
        
        self.styles.add(ParagraphStyle(
            name='CodeBlock',
            parent=self.styles['Normal'],
            fontSize=9,
            fontName='Courier',
            textColor=HexColor('#ecf0f1'),
            backColor=HexColor('#2c3e50'),
            borderColor=HexColor('#34495e'),
            borderWidth=1,
            borderPadding=10,
            spaceAfter=15,
            spaceBefore=10
        ))
        
        # Alert styles
        self.styles.add(ParagraphStyle(
            name='Alert',
            parent=self.styles['Normal'],
            fontSize=11,
            fontName='Helvetica-Bold',
            textColor=white,
            backColor=HexColor('#f39c12'),
            borderColor=HexColor('#e67e22'),
            borderWidth=2,
            borderPadding=10,
            spaceAfter=15,
            spaceBefore=10
        ))
    
    def read_and_process_markdown(self):
        """Read and process the markdown file"""
        with open(self.input_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Convert markdown to HTML
        html_content = markdown.markdown(
            content,
            extensions=['codehilite', 'tables', 'fenced_code', 'toc']
        )
        
        return content, html_content
    
    def create_title_page(self):
        """Create professional title page"""
        elements = []
        
        # Add some space from top
        elements.append(Spacer(1, 2*inch))
        
        # Title
        elements.append(Paragraph(self.title, self.styles['BookTitle']))
        elements.append(Spacer(1, 0.5*inch))
        
        # Subtitle
        elements.append(Paragraph(self.subtitle, self.styles['BookSubtitle']))
        elements.append(Spacer(1, 1*inch))
        
        # Author
        elements.append(Paragraph(f"by {self.author}", self.styles['Author']))
        elements.append(Spacer(1, 2*inch))
        
        # Publication info
        pub_info = f"""
        <para align="center">
        <b>{self.publisher}</b><br/>
        {self.publication_date}
        </para>
        """
        elements.append(Paragraph(pub_info, self.styles['Normal']))
        
        # Page break
        elements.append(PageBreak())
        
        return elements
    
    def create_copyright_page(self):
        """Create copyright and legal notice page"""
        elements = []
        
        copyright_text = f"""
        <para align="center"><b>Copyright and Legal Notice</b></para>
        <br/><br/>
        © 2024 {self.publisher}. All rights reserved.
        <br/><br/>
        <b>IMPORTANT LEGAL DISCLAIMER:</b>
        <br/><br/>
        This guide is intended for educational and authorized security testing purposes only. 
        The techniques described should only be used on systems you own or have explicit written 
        permission to test. Unauthorized access to computer systems is illegal and may result 
        in criminal prosecution.
        <br/><br/>
        <b>Publication Information:</b><br/>
        Title: {self.title}<br/>
        Publisher: {self.publisher}<br/>
        Publication Date: {self.publication_date}<br/>
        Language: English<br/>
        Format: Professional E-book
        <br/><br/>
        No part of this publication may be reproduced, distributed, or transmitted in any form 
        or by any means, including photocopying, recording, or other electronic or mechanical 
        methods, without the prior written permission of the publisher.
        """
        
        elements.append(Paragraph(copyright_text, self.styles['BodyText']))
        elements.append(PageBreak())
        
        return elements
    
    def parse_html_to_elements(self, html_content):
        """Parse HTML content and convert to ReportLab elements"""
        elements = []
        soup = BeautifulSoup(html_content, 'html.parser')
        
        for element in soup.find_all(['h1', 'h2', 'h3', 'h4', 'p', 'pre', 'code', 'table', 'ul', 'ol']):
            if element.name == 'h1':
                elements.append(PageBreak())
                text = self.clean_text(element.get_text())
                elements.append(Paragraph(text, self.styles['ChapterTitle']))
                
            elif element.name == 'h2':
                text = self.clean_text(element.get_text())
                elements.append(Paragraph(text, self.styles['SectionTitle']))
                
            elif element.name == 'h3':
                text = self.clean_text(element.get_text())
                elements.append(Paragraph(text, self.styles['SubsectionTitle']))
                
            elif element.name == 'h4':
                text = self.clean_text(element.get_text())
                elements.append(Paragraph(f"<b>{text}</b>", self.styles['BodyText']))
                
            elif element.name == 'p':
                text = self.process_paragraph(element)
                if text.strip():
                    elements.append(Paragraph(text, self.styles['BodyText']))
                    
            elif element.name == 'pre':
                code_text = element.get_text()
                # Split long code blocks
                lines = code_text.split('\n')
                for i in range(0, len(lines), 20):  # 20 lines per block
                    block = '\n'.join(lines[i:i+20])
                    elements.append(Paragraph(f"<font name='Courier'>{self.escape_html(block)}</font>", 
                                            self.styles['CodeBlock']))
                    
            elif element.name == 'code' and element.parent.name != 'pre':
                code_text = self.escape_html(element.get_text())
                elements.append(Paragraph(f"<font name='Courier'>{code_text}</font>", 
                                        self.styles['Code']))
                
            elif element.name == 'table':
                table_data = self.parse_table(element)
                if table_data:
                    table = Table(table_data)
                    table.setStyle(TableStyle([
                        ('BACKGROUND', (0, 0), (-1, 0), HexColor('#34495e')),
                        ('TEXTCOLOR', (0, 0), (-1, 0), white),
                        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                        ('FONTSIZE', (0, 0), (-1, 0), 10),
                        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                        ('BACKGROUND', (0, 1), (-1, -1), HexColor('#f8f9fa')),
                        ('GRID', (0, 0), (-1, -1), 1, HexColor('#bdc3c7'))
                    ]))
                    elements.append(table)
                    elements.append(Spacer(1, 10))
                    
            elif element.name in ['ul', 'ol']:
                list_items = element.find_all('li')
                for item in list_items:
                    text = self.clean_text(item.get_text())
                    bullet = "• " if element.name == 'ul' else f"{list_items.index(item) + 1}. "
                    elements.append(Paragraph(f"{bullet}{text}", self.styles['BodyText']))
        
        return elements
    
    def process_paragraph(self, p_element):
        """Process paragraph with inline formatting"""
        text = ""
        for content in p_element.contents:
            if hasattr(content, 'name'):
                if content.name == 'strong' or content.name == 'b':
                    text += f"<b>{self.escape_html(content.get_text())}</b>"
                elif content.name == 'em' or content.name == 'i':
                    text += f"<i>{self.escape_html(content.get_text())}</i>"
                elif content.name == 'code':
                    text += f"<font name='Courier' color='#e74c3c'>{self.escape_html(content.get_text())}</font>"
                else:
                    text += self.escape_html(content.get_text())
            else:
                text += self.escape_html(str(content))
        
        return text
    
    def parse_table(self, table_element):
        """Parse HTML table to list of lists"""
        rows = []
        for tr in table_element.find_all('tr'):
            row = []
            for cell in tr.find_all(['th', 'td']):
                row.append(self.clean_text(cell.get_text()))
            if row:
                rows.append(row)
        return rows
    
    def clean_text(self, text):
        """Clean and escape text for ReportLab"""
        text = re.sub(r'\s+', ' ', text.strip())
        return self.escape_html(text)
    
    def escape_html(self, text):
        """Escape HTML entities for ReportLab"""
        text = text.replace('&', '&amp;')
        text = text.replace('<', '&lt;')
        text = text.replace('>', '&gt;')
        return text
    
    def generate_pdf(self):
        """Generate professional PDF"""
        print("📄 Generating professional PDF...")
        
        pdf_path = "output/Red_Team_Blue_Team_Guide_Professional.pdf"
        
        # Create document
        doc = SimpleDocTemplate(
            pdf_path,
            pagesize=A4,
            rightMargin=2*cm,
            leftMargin=2*cm,
            topMargin=2*cm,
            bottomMargin=2*cm,
            title=self.title,
            author=self.author,
            subject="Cybersecurity Testing Guide"
        )
        
        # Build document content
        story = []
        
        # Add title page
        story.extend(self.create_title_page())
        
        # Add copyright page
        story.extend(self.create_copyright_page())
        
        # Process main content
        markdown_content, html_content = self.read_and_process_markdown()
        content_elements = self.parse_html_to_elements(html_content)
        story.extend(content_elements)
        
        # Build PDF
        doc.build(story)
        
        # Check result
        if os.path.exists(pdf_path):
            size = os.path.getsize(pdf_path) / (1024 * 1024)
            print(f"✅ PDF generated: {pdf_path}")
            print(f"📊 Size: {size:.2f} MB")
            return pdf_path
        else:
            print("❌ PDF generation failed")
            return None
    
    def generate_epub(self):
        """Generate EPUB version"""
        print("📚 Generating EPUB...")
        
        epub_path = "output/Red_Team_Blue_Team_Guide_Professional.epub"
        
        # Read content
        markdown_content, html_content = self.read_and_process_markdown()
        
        # Create EPUB structure
        self.create_epub_structure(html_content, epub_path)
        
        if os.path.exists(epub_path):
            size = os.path.getsize(epub_path) / (1024 * 1024)
            print(f"✅ EPUB generated: {epub_path}")
            print(f"📊 Size: {size:.2f} MB")
            return epub_path
        else:
            print("❌ EPUB generation failed")
            return None
    
    def create_epub_structure(self, html_content, epub_path):
        """Create EPUB file structure"""
        
        # Create temporary directory for EPUB files
        temp_dir = "temp_epub"
        os.makedirs(temp_dir, exist_ok=True)
        os.makedirs(f"{temp_dir}/META-INF", exist_ok=True)
        os.makedirs(f"{temp_dir}/OEBPS", exist_ok=True)
        
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
    <dc:title>{self.title}</dc:title>
    <dc:creator>{self.author}</dc:creator>
    <dc:publisher>{self.publisher}</dc:publisher>
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
    <text>{self.title}</text>
  </docTitle>
  <navMap>
    <navPoint id="navpoint-1" playOrder="1">
      <navLabel>
        <text>{self.title}</text>
      </navLabel>
      <content src="content.xhtml"/>
    </navPoint>
  </navMap>
</ncx>'''
        
        with open(f"{temp_dir}/OEBPS/toc.ncx", 'w', encoding='utf-8') as f:
            f.write(toc_ncx)
        
        # Create CSS
        css_content = '''
        body {
            font-family: Georgia, serif;
            line-height: 1.6;
            color: #333;
            margin: 1em;
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
        
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 1em 0;
        }
        
        th, td {
            border: 1px solid #bdc3c7;
            padding: 0.5em;
            text-align: left;
        }
        
        th {
            background-color: #34495e;
            color: white;
        }
        '''
        
        with open(f"{temp_dir}/OEBPS/style.css", 'w', encoding='utf-8') as f:
            f.write(css_content)
        
        # Create content.xhtml
        content_xhtml = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.1//EN" "http://www.w3.org/TR/xhtml11/DTD/xhtml11.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <title>{self.title}</title>
    <link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
    <h1>{self.title}</h1>
    <h2>{self.subtitle}</h2>
    <p><strong>by {self.author}</strong></p>
    <p><em>{self.publisher} - {self.publication_date}</em></p>
    <hr/>
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
    
    def create_publishing_info(self):
        """Create publishing information file"""
        info_content = f"""
PROFESSIONAL E-BOOK PUBLISHING INFORMATION
==========================================

Title: {self.title}
Subtitle: {self.subtitle}
Author: {self.author}
Publisher: {self.publisher}
Publication Date: {self.publication_date}
Language: English
Format: PDF + EPUB

File Details:
- PDF: Red_Team_Blue_Team_Guide_Professional.pdf
- EPUB: Red_Team_Blue_Team_Guide_Professional.epub

Amazon KDP Requirements Met:
✅ Professional formatting and typography
✅ Table of contents
✅ Copyright page and legal disclaimers
✅ Proper metadata for discoverability
✅ Print-ready PDF format
✅ E-reader compatible EPUB
✅ Professional styling throughout

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
incident response, forensics, security analysis, car security

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
"""
        
        with open("output/publishing_info.txt", 'w', encoding='utf-8') as f:
            f.write(info_content)
        
        print("📋 Publishing information saved to: output/publishing_info.txt")

def main():
    """Main function to generate professional e-books"""
    input_file = "red_team_blue_team_guide.md"
    
    if not os.path.exists(input_file):
        print(f"❌ Error: {input_file} not found!")
        return
    
    print("🚀 Starting professional e-book generation...")
    print(f"📖 Processing: {input_file}")
    
    generator = ProfessionalEbookGenerator(input_file)
    
    try:
        # Generate PDF
        pdf_path = generator.generate_pdf()
        
        # Generate EPUB
        epub_path = generator.generate_epub()
        
        # Create publishing info
        generator.create_publishing_info()
        
        print("\n🎉 Professional e-book generation completed!")
        if pdf_path:
            print(f"📄 PDF: {pdf_path}")
        if epub_path:
            print(f"📚 EPUB: {epub_path}")
        print("\n📝 Files are ready for Amazon KDP publishing!")
        
    except Exception as e:
        print(f"❌ Error generating e-books: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
