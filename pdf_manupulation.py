# Extracting text from PDF file

# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('Morrie.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(1)

# extracting text from page
print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()
