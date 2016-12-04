# coding=utf-8
import csv
import re

oldRow = ['gift', 'Bundesministerium des Innern','2009-20011', 'n.a.', 'fate', 'BMI', 'fail']

bmi = open('bmi.csv', 'w')

with open('../data/csvTxtPreprocess/BMI2009-11Pre.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',', quotechar='"')
    for row in data:
        newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'BMI']

        if len(row) == 1:
            row.append('')
            row.append('n.a.')
        elif len(row) == 2:
            row.append('n.a.')

        # get gift
        newRow[0] = re.sub(r'\n', '', row[0])

        # get price
        if row[1] != '':
            if 'unter 25' in row[1]:
                newRow[5] = 'True'
                newRow[4] = '00.00'
            else:
                newRow[5] = 'False'
                newRow[4] = re.sub('[A-Za-z€\s()$>?]', '', row[1])
                newRow[4] = re.sub('\,', '.', newRow[4])
                newRow[4] = '0' + newRow[4]
                # get 25er bools
                if float(newRow[4]) > 25:
                    newRow[6] = 'True'
                    newRow[5] = "False"
                elif float(newRow[4]) < 25:
                    newRow[5] = 'True'
                    newRow[6] = "False"

        else:
            newRow[4] = '00.00'
            newRow[5] = "False"
            newRow[6] = "False"


        print newRow[4:7]


        # get fate
        newRow[7] = row[2]
        # get success
        if 'Selbstbehalt' in row[2]:
            newRow[8] = 'success'
        bmi.write(', '.join(newRow) + '\n')



