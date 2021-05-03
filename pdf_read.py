# https://gtts.readthedocs.io/en/latest/module.html#examples

# need gTTS and mpg123
# pip install gTTS
# apt install mpg123

from gtts import gTTS
import os
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
txt=pageObj.extractText()
# print(pageObj.extractText())

# closing the pdf file object
pdfFileObj.close()




# define variables
# s = "escape with plane"
file = "text.mp3"

# initialize tts, create mp3 and play
tts = gTTS(txt, lang='en')
tts.save(file)
os.system("mpg123 " + file)#play mp3
