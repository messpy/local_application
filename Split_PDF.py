try:
    import PyPDF2
    import os
    from tkinter import filedialog


        
    org_fileName = filedialog.askopenfilename()  # 分割したいファイルのファイル名
    pdf = r"C:\Users\910143\Desktop\PDF"
    new_fileName = pdf+ "\\あ" + os.path.splitext(os.path.basename(org_fileName))[0] # 分割後のファイル名


    def splitPDF(src_path, new_basepath):
        org_pdf = PyPDF2.PdfFileReader(src_path)
        for i in range(org_pdf.numPages):
            new_pdf = PyPDF2.PdfFileWriter()
            new_pdf.addPage(org_pdf.getPage(i))
            i = '{0:02}'.format(i)
            with open('{}_{}.pdf'.format(new_basepath, i), 'wb') as f:
                new_pdf.write(f)

    splitPDF(org_fileName, new_fileName)
except Exception as e:
    print(e)
    input("")
