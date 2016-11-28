# coding=utf-8
import re

newRow = ['gift', 'Bundesministerium für wirtschaftliche Zusammenarbeit','2015', 'n.a.', 'fate', 'BMZ', 'false', '0']
#file = open('../data/csvTxtPreprocess/BMZ.pdf.txt', 'r+')
#data = file.read()
#temp = re.sub('(\d{2}\.){1}(\d{2}\.){1}', "\n\\1\\2", data)
bmzfinal =  open('bmz.csv', 'w')

with open('../data/csvTxtPreprocess/bmzordered.txt', 'r+') as orderedtxt:
    for row in orderedtxt:
        #get date
        datetemp = row.split(' ')[0]
        datelist = datetemp.split('.')
        datelist.reverse()
        newRow[2] = '/'.join(datelist)
        #get fate
        list = row.split(' ')
        list.pop(0)
        list = [x for x in list if x != ''] #deletes all ''
        if list[-3] == 'privat':
            newRow[4] = 'privat verwendet'
            newRow[6] = 'true'
            del list[-3:-2]
        elif list[-3] == 'dienstlich':
            newRow[4] = 'dienstlich verwendet'
            newRow[6] = 'true'
            del list[-3:-2]
        elif list[-2] == '(verderblich)':
            newRow[4] = 'wurde nach Rücksprache mit Mitarbeiterin entsorgt (verderblich)'
            newRow[6] = 'false'
            del list[-8:-2]
        elif list[-2] == 'mitgenommen':
            newRow[4] = 'nicht mitgenommen'
            newRow[6] = 'false'
            del list[-3:-2]
        else:
            newRow[4] = list[-2]
            newRow[6] = 'false'
            list.pop(-2)
        #get gift and price
        list = [x for x in list if x != 'x']  # deletes all x
        row = ' '.join(list)
        range = re.compile(r'(\d{2}\,\d{2}\s\-\s\d{2}\,\d{2})')
        under = re.compile(r'(\<\s\d{2}\,\d{2})')
        on = re.compile(r'(\d{2}\,\d{2})')
        if range.search(row) is not None:
            temp = re.split(range, row, maxsplit=1)
            newRow[0] = temp[0]
            newRow[3] = temp[1]
        elif under.search(row) is not None:
            temp = re.split(under, row, maxsplit=1)
            newRow[0] = temp[0]
            newRow[3] = temp[1]
        elif on.search(row) is not None:
            temp = re.split(on, row, maxsplit=1)
            newRow[0] = temp[0]
            newRow[3] = temp[1]
        else:
            newRow[3] = 'n.a.'
            templist = row.split()
            gift = []
            for word in templist:
                if word != 'keine':
                    gift.append(word)
                else:
                    break
            newRow[0] = ' '.join(gift)

        bmzfinal.write(', '.join(newRow) + '\n')











