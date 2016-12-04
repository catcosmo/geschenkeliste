# coding=utf-8
import csv
import re

oldRow = ['gift', 'Bundesministerium der Verteidigung','seit 10/2009', 'n.a.', 'n.a.', 'BMV', 'fail']
newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'BMV']
sheet =  open('bmv.csv', 'w')



with open('../data/csvTxtPreprocess/bmvPre.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')

    for row in data:
        if len(row) < 3:
            print row
        # get gift
        newRow[0] = row[0]
        # get value
        if '< 25' in row[1]:
            newRow[5] = 'True'
            newRow[4] = '00.00'
        else:
            newRow[5] = 'False'
            newRow[4] = re.sub('[A-Za-z€\s\"()$>?.]', '', row[1])
            newRow[4] = re.sub('\,', '.', newRow[4])
            newRow[4] = '0' + newRow[4]

            # get 25er bools
            if float(newRow[4]) > 25:
                newRow[6] = 'True'
                newRow[5] = "False"
            elif float(newRow[4]) < 25:
                newRow[5] = 'True'
                newRow[6] = "False"
        # get fate
        newRow[7] = row[2]
        # get success
        if ('Bezahlung' in row[2]) | ('kostenfreie' in row[2]):
            newRow[8] = 'success'
        else:
            newRow[8] = 'fail'

        sheet.write(', '.join(newRow) + '\n')
