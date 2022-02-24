import io
from tkinter import *
from tkinter import  ttk
from tkinter import filedialog
from tkinter import messagebox
import xlrd
import collections
class engineFile:
    def __init__(self,path='./option.txt'):
        self.path=path
        self.data=collections.OrderedDict()
        self.dataXlsx={}
    def loadFile(self):
        self.data.clear()
        filePath = filedialog.askopenfilename(filetypes=(("txt File", "*.txt")
                                   , ("All files", "*.*")))
        with io.open(file=filePath,mode='r') as file:
            for line in file:
                words=line.strip().rstrip()
                if words!='':
                    print(words)
                    words=words.split(' ')
                    self.data[(words[0],words[1])]=int(words[2])
        self.path=filePath

    def saveFile(self):
        filePath = filedialog.asksaveasfilename(filetypes=(("txt File", "*.txt")
                                   , ("All files", "*.*")))
        with io.open(file=filePath,mode='w') as file:
            for key, value in self.data.items():
                file.write(key[0]+' '+key[1]+' '+str(value)+'\n')
    def saveAsFile(self):
        filePath = self.path
        with io.open(file=filePath,mode='w') as file:
            for key, value in self.data.items():
                file.write(key[0]+' '+key[1]+' '+str(value)+'\n')
        messagebox.showinfo(title="Save As Message Box",message="KeyWord File Save as "+self.path)

    def newFile(self):
        self.data = collections.OrderedDict()
        self.path='./option.txt'
    def loadXlsxFile(self):
        filePath = filedialog.askopenfilename(filetypes=(("Excel File", "*.xlsx")
                                   , ("All files", "*.*")))
        workbook = xlrd.open_workbook(filePath)
        worksheet = workbook.sheet_by_index(0)
        lastcol1 = worksheet.cell_value(1, 0)
        lastcol2 = worksheet.cell_value(1, 1)
        lastcol3 = worksheet.cell_value(1, 2)
        firstcol = ''
        secoundcol = ''
        tirdcolumn = ''
        for i in range(1, worksheet.nrows):
            firstcol = worksheet.cell_value(i, 0)
            secoundcol = worksheet.cell_value(i, 1)
            tirdcolumn = worksheet.cell_value(i, 2)
            if firstcol == '':
                firstcol = lastcol1
            else:
                lastcol1 = firstcol
            if secoundcol == '':
                secoundcol = lastcol2
            else:
                lastcol2 = secoundcol
            if tirdcolumn == '':
                tirdcolumn = lastcol3
            else:
                lastcol3 = tirdcolumn
            if firstcol not in self.dataXlsx.keys():
                self.dataXlsx[firstcol] = {}
            if secoundcol not in self.dataXlsx[firstcol].keys():
                self.dataXlsx[firstcol][secoundcol] = {}
            if tirdcolumn not in self.dataXlsx[firstcol][secoundcol].keys():
                self.dataXlsx[firstcol][secoundcol][tirdcolumn] = []
        print(self.dataXlsx)






