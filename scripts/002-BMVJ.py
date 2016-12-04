# coding=utf-8
import csv
import re

oldRow = ['gift', 'Bundesministerium der Justiz und für Verbraucherschutz','seit 10/2009', 'n.a.', 'n.a.', 'BMJV', 'fail']

sheet =  open('bmjv.csv', 'w')



with open('../data/csvTxtPreprocess/BMJVPre.csv', 'r+') as file:
    newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'BMVJ']

    data = csv.reader(file, delimiter=',')

    for row in data:
        if len(row) < 3:
            print row
        # get gift
        newRow[0] = row[0].strip()

        # get value
        newRow[4] = re.sub('[A-Za-z€\s\"()$>?.]', '', row[1])
        newRow[4] = re.sub('\,', '.', newRow[4])

        # get 25er bools
        if float(newRow[4]) > 25:
            newRow[6] = 'True'
            newRow[5] = "False"
        elif float(newRow[4]) <= 25:
            newRow[5] = 'True'
            newRow[6] = "False"

        # get fate
        newRow[7] = row[2]
        # get success
        if ('Mitarbeiter' in row[2]) | ('Mitarbeiterinpython bmvj.py' in row[2]):
            newRow[8] = 'success'
        else:
            newRow[8] = 'fail'

        sheet.write(', '.join(newRow) + '\n')
