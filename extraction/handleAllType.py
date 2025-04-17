import os
from docx import Document
from io import StringIO

# PDF support
from pdfminer.high_level import extract_text as extract_pdf_text

# Old Word (.doc) and general OCR fallback
import textract

# ODT (OpenDocument Text)
from odf.opendocument import load
from odf.text import P
from bs4 import BeautifulSoup


def extract_text_from_docx(path):
    try:
        document = Document(path)
        return "\n".join([para.text for para in document.paragraphs])
    except Exception as e:
        return f"[DOCX ERROR] {e}"


def extract_text_from_pdf(path):
    try:
        return extract_pdf_text(path)
    except Exception as e:
        return f"[PDF ERROR] {e}"


def extract_text_from_txt(path):
    try:
        with open(path, 'r', encoding='utf-8') as file:
            return file.read()
    except Exception as e:
        return f"[TXT ERROR] {e}"


def extract_text_from_doc(path):
    try:
        return textract.process(path).decode('utf-8')
    except Exception as e:
        return f"[DOC ERROR] {e}"


def extract_text_from_odt(path):
    try:
        textdoc = load(path)
        paragraphs = textdoc.getElementsByType(P)
        text = " ".join([str(p) for p in paragraphs])
        soup = BeautifulSoup(text, "html.parser")
        return soup.get_text()
    except Exception as e:
        return f"[ODT ERROR] {e}"


def extract_text_from_cv(path):
    ext = os.path.splitext(path)[1].lower()

    if ext == ".pdf":
        return extract_text_from_pdf(path)
    elif ext == ".docx":
        return extract_text_from_docx(path)
    elif ext == ".txt":
        return extract_text_from_txt(path)
    elif ext == ".doc":
        return extract_text_from_doc(path)
    elif ext == ".odt":
        return extract_text_from_odt(path)
    else:
        return f"[UNSUPPORTED FILE TYPE] {ext}"


file_path = "data/CVs/sample_resume.docx"
extracted_text = extract_text_from_cv(file_path)
print(extracted_text[:300])  # First 300 characters

# pip install python-docx pdfminer.six textract odfpy beautifulsoup4
