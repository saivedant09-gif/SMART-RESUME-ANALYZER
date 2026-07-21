import fitz

def extract_pdf_text(file_path):
    """
    Extract text from a PDF file.
    """

    text = ""

    pdf = fitz.open(file_path)

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text

from docx import Document

def extract_docx_text(file_path):
    """
    Extract text from a DOCX file.
    """

    document = Document(file_path)

    text = ""

    for paragraph in document.paragraphs:
        text += paragraph.text + "\n"

    return text