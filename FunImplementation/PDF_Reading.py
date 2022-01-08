import PyPDF2
import slate3k

def read_PDF():
    path = 'C:\\Users\\tankh\\Downloads\\Are you ready 17-....pdf'
    docs = open(path, 'rb')
    print(slate3k.PDF(docs))
    docs.close()


read_PDF()