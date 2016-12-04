# coding=utf-8
import re

oldRow = ['gift', 'Bundesministerium für wirtschaftliche Zusammenarbeit','2015', 'n.a.', 'fate', 'BMZ', 'false', '0']
#file = open('../data/csvTxtPreprocess/BMZ.pdf.txt', 'r+')
#data = file.read()
#temp = re.sub('(\d{2}\.){1}(\d{2}\.){1}', "\n\\1\\2", data)
bmzfinal =  open('bmz.csv', 'w')

with open('../data/csvTxtPreprocess/bmzordered.txt', 'r+') as orderedtxt:
    for row in orderedtxt:
        newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'BMZ']

        #get date
        datetemp = row.split(' ')[0]
        newRow[3], newRow[2], newRow[1] = datetemp.split('.')

        #get fate
        list = row.split(' ')
        list.pop(0)
        list = [x for x in list if x != ''] #deletes all ''
        if list[-3] == 'privat':
            newRow[7] = 'privat verwendet'
            newRow[8] = 'true'
            del list[-3:-2]
        elif list[-3] == 'dienstlich':
            newRow[7] = 'dienstlich verwendet'
            newRow[8] = 'true'
            del list[-3:-2]
        elif list[-2] == '(verderblich)':
            newRow[7] = 'wurde nach Rücksprache mit Mitarbeiterin entsorgt (verderblich)'
            newRow[8] = 'false'
            del list[-8:-2]
        elif list[-2] == 'mitgenommen':
            newRow[7] = 'nicht mitgenommen'
            newRow[8] = 'false'
            del list[-3:-2]
        else:
            newRow[7] = list[-2]
            newRow[8] = 'false'
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
            if '< 25' in temp[1]:
                newRow[5] = 'True'
                newRow[4] = '00.00'
            else:
                newRow[5] = 'False'
                newRow[4] = re.sub('[A-Za-z.€\s()$>?-]', '', temp[1])
                newRow[4] = re.sub('\,', '.', newRow[4])
                # get 25er bools
                if float(newRow[4]) > 25:
                    newRow[6] = 'True'
                    newRow[5] = "False"
                elif float(newRow[4]) < 25:
                    newRow[5] = 'True'
                    newRow[6] = "False"
        elif under.search(row) is not None:
            temp = re.split(under, row, maxsplit=1)
            newRow[0] = temp[0]
            if '< 25' in temp[1]:
                newRow[5] = 'True'
                newRow[4] = '00.00'
            else:
                newRow[5] = 'False'
                newRow[4] = re.sub('[A-Za-z.€\s()$<>?-]', '', temp[1])
                newRow[4] = re.sub('\,', '.', newRow[4])
                # get 25er bools
                if float(newRow[4]) > 25:
                    newRow[6] = 'True'
                    newRow[5] = "False"
                elif float(newRow[4]) < 25:
                    newRow[5] = 'True'
                    newRow[6] = "False"
        elif on.search(row) is not None:
            temp = re.split(on, row, maxsplit=1)
            newRow[0] = temp[0]
            if '< 25' in temp[1]:
                newRow[5] = 'True'
                newRow[4] = '00.00'
            else:
                newRow[5] = 'False'
                newRow[4] = re.sub('[A-Za-z.€\s()$>?-]', '', temp[1])
                newRow[4] = re.sub('\,', '.', newRow[4])
                # get 25er bools
                if float(newRow[4]) > 25:
                    newRow[6] = 'True'
                    newRow[5] = "False"
                elif float(newRow[4]) < 25:
                    newRow[5] = 'True'
                    newRow[6] = "False"
        else:
            newRow[4] = '00.00'
            templist = row.split()
            gift = []
            for word in templist:
                if word != 'keine':
                    gift.append(word)
                else:
                    break
            newRow[0] = ' '.join(gift)


        bmzfinal.write(', '.join(newRow) + '\n')











