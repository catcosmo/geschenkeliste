# coding=utf-8
import csv
import re

oldRow = ['gift', 'Bundesministerium für Familie, Senioren, Frauen und Jugend','seit 10/2009', 'n.a.', 'fate', 'BMFSFJ', 'fail']
newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'AA']

bmf = open('bmfsfjFinal.csv', 'w')

with open('/Users/krawallmietze/code/python/geschenkeliste/scripts/BMFSFJ-done.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        # get gift
        newRow[0] = row[0].lstrip()
        # get price
        if row[1] != '':
            # get 25er bools
            if 'unter 25' in row[1]:
                newRow[5] = 'True'
                newRow[4] =  '00.00'
            else:
                newRow[5] = 'False'
                newRow[4] = re.sub('[A-Za-z.€\s()$>?-]', '', row[1])
                newRow[4] = re.sub('\,', '.', newRow[4])
                if newRow[4] == '':
                    newRow[4] = '00.00'

        # get fate
        newRow[7] = row[2]
        # get success
        if 'Verbleib' in row[2]:
            newRow[8] = 'success'
        else:
            newRow[8] = 'fail'

        bmf.write(', '.join(newRow) + '\n')