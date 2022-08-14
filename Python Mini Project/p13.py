# Extract Text From PDF with Python

import PyPDF2
pdf = open("umesh.pdf", "rb")
reader = PyPDF2.PdfFileReader(pdf)
page = reader.getPage(1)
print(page.extractText())