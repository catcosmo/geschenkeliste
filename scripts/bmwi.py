# coding=utf-8
import csv
import re

newRow = ['gift', 'Bundesministerium für Wirtschaft und Energie','2013', 'n.a.', 'n.a.', 'BMWi', 'fail']
sheet =  open('bmwi.csv', 'w')



with open('data/csvTxtPreprocess/BMWi.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        # get date
        if row[0] == '':
            datetemp = row[1].split(' ')
            datelist = datetemp[1].split('.')
            datelist.reverse()
            tempdate = '/'.join(datelist)
        else:
            newRow[2] = tempdate
            # get gift
            newRow[0] = row[0]

            sheet.write(', '.join(newRow) + '\n')
