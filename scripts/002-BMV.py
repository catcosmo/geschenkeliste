# coding=utf-8
import csv
import re

newRow = ['gift', 'Bundesministerium der Verteidigung','seit 10/2009', 'n.a.', 'n.a.', 'BMV', 'fail']
sheet =  open('bmv.csv', 'w')



with open('data/csvTxtPreprocess/bmvPre.csv', 'r+') as file:
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
        if ('Bezahlung' in row[2]) | ('kostenfreie' in row[2]):
            newRow[6] = 'success'

        sheet.write(', '.join(newRow) + '\n')
