# coding=utf-8
import csv
import re

newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'BMWI']
sheet =  open('bmwi.csv', 'w')



with open('../data/csvTxtPreprocess/BMWi.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',', quotechar='"')
    for row in data:
        # get date
        if row[0] == '':
            datetemp = row[1].split(' ')
            newRow[3], newRow[2], newRow[1] = datetemp[1].split('.')


        else:
            # get gift
            newRow[0] = row[0]

            sheet.write(', '.join(newRow) + '\n')
