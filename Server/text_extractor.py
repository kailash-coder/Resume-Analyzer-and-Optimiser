from PyPDF2 import PdfReader
from tabula.io import read_pdf
import tabula

def get_pdf_text(pdf_docs):
    pdf_data = {}
    
    # Extract text using PyPDF2
    for pdf in pdf_docs:
        reader = PdfReader(pdf)
        text = ''
        for page in reader.pages:
            text += page.extract_text()
        pdf_data['text'] = text
        
        # Extract tables using tabula
        tables = tabula.io.read_pdf(pdf, pages='all', multiple_tables=True)
        pdf_data['tables'] = tables
    
    return pdf_data


def convert_json_to_text(pdf_data):
    text = ''
    
    # Convert text content to text string
    if 'text' in pdf_data:
        text += pdf_data['text']
    
    # Convert table content to text string
    if 'tables' in pdf_data:
        tables = pdf_data['tables']
        for table in tables:
            text += '\n'.join([' '.join(map(str, row)) for row in table.values])
    
    return text