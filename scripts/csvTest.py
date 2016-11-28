# coding=utf-8

import csv
import datetime

with open('../data/csvFinal/bmz.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',')
    rowCount = 0
    for row in data:
        rowCount++
        #alle geschenkartikel in row[0] zusammenfassen
        ministry = row[1].split()[0]
        if((ministry!='Bundesministerium')&(ministry!='Auswärtiges')):
            newRow = []
            newRow.append('\'' + row[0] + ',' + row[1])
            n = 2
            while ((row[n].split()[0]!='Bundesministerium')&(row[n].split()[0]!='Auswärtiges')):
                newRow[0] += ',' + row[n]
                n += 1
            newRow[0] += '\''
            del row[0:n]
            newRow.extend(row)
            row = newRow
        #check correct date form
        if(not(row[1].isdigit()) | len(row[1]) != 4):
            print 'wrong year format:' + row[1], rowCount
        if(row[2] not in range(1, 13) | len(row[2]) != 2):
            print 'wrong month format:' + row[2], rowCount
        if(row[3] not in range(1, 32) | len(row[3]) != 2):
                print 'wrong day format:' + row[3], rowCount
        #check correct value form format(x, '.2f')

        #check fate

        #check correct success value
        if(row[6] != ("TRUE" | "FALSE")):
            print 'wrong success format:' + row[6], rowCount
















