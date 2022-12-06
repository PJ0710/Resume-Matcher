import pdfplumber

path = "./dependency/documents/resume.pdf"

with pdfplumber.open(rf'{path}') as pdf:
    print(pdf.pages)
    first_page = pdf.pages[1]
    print(first_page.extract_text())