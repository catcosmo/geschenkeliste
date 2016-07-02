# coding=utf-8
import csv
import re

newRow = ['gift', 'Bundesministerium des Innern','2009-20011', 'n.a.', 'fate', 'BMI', 'fail']
bmi = open('bmi.csv', 'w')

with open('data/csvTxtPreprocess/BMI2009-11Pre.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        if len(row) == 1:
            row.append('')
            row.append('n.a.')
        elif len(row) == 2:
            row.append('n.a.')
        print row
        # get gift
        re.sub(r'\n', '', row[0])
        newRow[0] = row[0]
        # get price
        if row[1] != '':
            newRow[3] = row[1]
        # get fate
        newRow[4] = row[2]
        # get success
        if 'Selbstbehalt' in row[2]:
            newRow[6] = 'success'
        bmi.write(', '.join(newRow) + '\n')



