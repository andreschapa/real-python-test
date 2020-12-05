from PyPDF2 import PdfFileReader, PdfFileWriter
from pathlib import Path

class PdfFileSplitter:
    
    def __init__(self,doc):
        
        self.input_pdf=PdfFileReader('C:/Users/andres.chapa/'+doc)
        self.writer1=PdfFileWriter()
        self.writer2=PdfFileWriter()
        self.path1= None
        self.path2= None
        #

    def split(self,breakpoint):
        
        for n in self.input_pdf.pages[:breakpoint]:
            self.writer1.addPage(n)
        for n in self.input_pdf.pages[breakpoint:]:
            self.writer2.addPage(n)

    def writer(self,newdocname):
        self.path1=Path.home()/(newdocname +'_1.pdf')
        self.path2=Path.home()/(newdocname +'_2.pdf')
       #
        with self.path1.open(mode='wb') as outputfile1:
            self.writer1.write(outputfile1)

        with self.path2.open(mode='wb') as outputfile2:
            self.writer2.write(outputfile2)
        

pdf_splitter=PdfFileSplitter('Pride_and_Prejudice.pdf')
pdf_splitter.split(50)
pdf_splitter.writer('cunt')


            
    
        




    