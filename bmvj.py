# coding=utf-8
import csv
import re

newRow = ['gift', 'Bundesministerium der Justiz und für Verbraucherschutz','seit 10/2009', 'n.a.', 'n.a.', 'BMJV', 'fail']
sheet =  open('bmjv.csv', 'w')



with open('data/csvTxtPreprocess/BMJVPre.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')

    for row in data:
        if len(row) < 3:
            print row
        # get gift
        newRow[0] = row[0]
        # get value
        newRow[3] = row[1]
        # get fate
        newRow[4] = row[2]
        # get success
        if ('Mitarbeiter' in row[2]) | ('Mitarbeiterinpython bmvj.py' in row[2]):
            newRow[6] = 'success'

        sheet.write(', '.join(newRow) + '\n')
