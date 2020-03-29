#处理pdf文件的工具集
from PyPDF2 import PdfFileReader, PdfFileMerger
merger = PdfFileMerger()
input1 = open("doc1.pdf","rb")
input2 = open("doc2.pdf","rb")
merger.append(fileobj = input1, pages = (1,39))
merger.merge(position = 2, fileobj = input2, pages = (0,37))
output = open("doc3.pdf","wb")
merger.write(output)
