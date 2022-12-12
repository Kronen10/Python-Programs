from PyPDF2 import PdFileWriter, PdFileReader

pdfwriter = PdFileWriter()
pdf = PdFileReader('pdf.pdf')

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page])

password = getpass(prompt='Enter Password: ')
pdfwriter.encrypt(password)

with open('protected.pdf','wb') as file:
    pdfwriter.write(file)