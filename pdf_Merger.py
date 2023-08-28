import PyPDF2
import os

def merge_pdfs(pdf1, pdf2):
  """Merges two PDF files.

  Args:
    pdf1: The path to the first PDF file.
    pdf2: The path to the second PDF file.

  Returns:
    None.
  """

  pdf1_reader = PyPDF2.PdfReader(open(pdf1, "rb"))
  pdf2_reader = PyPDF2.PdfReader(open(pdf2, "rb"))

  merger = PyPDF2.PdfMerger()
  merger.append(pdf1_reader)
  merger.append(pdf2_reader)

  with open("merged2.pdf", "wb") as f:
    merger.write(f)

if __name__ == "__main__":
  pdf1 = "F:\python projects\pdf merger\chem sci project.pdf"
  pdf2 = "F:\python projects\pdf merger\iology sci project.pdf"

  merge_pdfs(pdf1, pdf2)
