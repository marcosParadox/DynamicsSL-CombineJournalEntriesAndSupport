#!/usr/bin/env python3
import re, PyPDF2, os
from PyPDF2 import PdfFileMerger, PdfFileReader
#Open the PDF
pdfFileObj = open('01AcctDi.pdf', 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj, strict=False)
NumPages = pdfReader.getNumPages()
#Regex to find batch number
batchRegex = re.compile('(GL)(\d\d\d\d\d\d)')
for i in range(0, NumPages):
        pageObj = pdfReader.getPage(i) 
        data = pageObj.extractText()
        text = ''.join(data.splitlines())
        text = text.replace(' ', '')
        batchMO = batchRegex.search(text)
        if batchMO == None:
                print('Batch number could not be read.')
                fileName = input('Enter the batch number: ')
        else:
                fileName = batchMO[2]
        break
pdfFileObj.close
os.mkdir(fileName)
#Merge the pdfs
merger = PdfFileMerger()
merger.append(PdfFileReader(open('01010.pdf', 'rb')))
merger.append(PdfFileReader(open('01AcctDi.pdf', 'rb')))
merger.write(fileName + '\\' + fileName + '.pdf')
