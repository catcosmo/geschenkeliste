# coding=utf-8
import csv
import re
newRow = ['gift', 'Auswärtiges Amt','2013', 'n.a.', 'n.a.', 'AA', 'n.a.']
aa13 =  open('aa15.csv', 'w')



with open('data/csvTxtPreprocess/2015AA.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        #for AA 15 layout
        if len(row) == 3:
            row.insert(1,'')
            row.insert(3,'')
        elif len(row) == 4:
            row.insert(1, '')
        if len(row) >3:
            if row[2] != '': #filters out empty rows
                #get date
                if row[0] == '':
                    newRow[2] = tempdate
                else:
                    datetemp = row[0]
                    datelist = datetemp.split('.')
                    datelist.reverse()
                    newRow[2] = '/'.join(datelist)
                    tempdate = newRow[2]
                #get gift
                newRow[0] = row[2]
                if row[1] not in ['',  'Zentrale']:
                    given = ' An: ' + row[1]
                    newRow[0] += given
                    newRow[0] += given
                #get fate + success
                if row[4] != '':
                    newRow[4] = row[4]
                    newRow[6] = 'fail'
                    if 'BM' in row[4]:
                        newRow[6] = 'success'

                #get price
                newRow[3] = row[3]

                #print newRow
                aa13.write(', '.join(newRow) + 'xxx')
