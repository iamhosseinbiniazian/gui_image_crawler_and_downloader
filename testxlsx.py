import xlrd
workbook = xlrd.open_workbook('tanzim.xlsx')
worksheet = workbook.sheet_by_index(0)
lastcol1=worksheet.cell_value(1,0)
lastcol2=worksheet.cell_value(1,1)
lastcol3=worksheet.cell_value(1,2)
firstcol=''
secoundcol=''
tirdcolumn=''
m=[]
all=[]
dic={}
import json
for i in range(1,worksheet.nrows):
    m=[]
    firstcol=worksheet.cell_value(i,0)
    secoundcol=worksheet.cell_value(i,1)
    tirdcolumn=worksheet.cell_value(i,2)

    if firstcol=='':
        firstcol=lastcol1
    else:
        lastcol1=firstcol
    if secoundcol=='':
        secoundcol=lastcol2
    else:
        lastcol2=secoundcol
    if tirdcolumn=='':
        tirdcolumn=lastcol3
    else:
        lastcol3=tirdcolumn
    if firstcol not in dic.keys():
        dic[firstcol]={}
    if secoundcol not in dic[firstcol].keys():
        dic[firstcol][secoundcol]={}
    if tirdcolumn not in dic[firstcol][secoundcol].keys():
        dic[firstcol][secoundcol][tirdcolumn] ={}

    m.append(firstcol)
    m.append(secoundcol)
    m.append(tirdcolumn)
    if m not in all:
        all.append(m)
    # print(firstcol,'*',secoundcol,'*',tirdcolumn)
print(dic)
# import io
# with io.open('data.json', 'w',encoding='utf-8') as fp:
#     json.dump(dic, fp)





