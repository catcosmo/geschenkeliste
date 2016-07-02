# coding=utf-8
import csv

newRow = ['gift', 'Bundesministerium für Familie, Senioren, Frauen und Jugend','seit 10/2009', 'n.a.', 'fate', 'BMFSFJ', 'fail']
bmf = open('bmfsfjFinal.csv', 'w')

with open('data/csvTxtPreprocess/BMFSFJ.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')
    for row in data:
        # get gift
        newRow[0] = row[0].lstrip()
        # get price
        if row[1] != '':
            newRow[3] = row[1]
        # get fate
        newRow[4] = row[2]
        # get success
        if 'Verbleib' in row[2]:
            newRow[6] = 'success'
        bmf.write(', '.join(newRow) + '\n')