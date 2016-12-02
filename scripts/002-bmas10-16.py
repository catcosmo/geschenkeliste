# coding=utf-8

import codecs
import csv

with open('../data/csvTxtPreprocess/BMAS2010-16.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')

    result = []

    for row in reader:
        day, month, year = row[0].split('/')
        gift = row[1]
        value = None
        under25euro = (row[2] == 'x')
        over25euro = (row[3] == 'x')
        fate = ''
        success = ''
        ministryabbreviation = 'bmas'

        for i in range(4, 8):
            options = {
                4: 'Behalten',
                5: 'Behalten (Dienstgebrauch)',
                6: 'Abgabe Dienstherr',
                7: 'Rueckgabe'
            }

            if row[i] == 'x':
                fate = options[i]
                #get success
                success = 'success' if i == 4 or i == 5 else 'fail'

        result.append([
            gift,
            day,
            month,
            year,
            value,
            under25euro,
            over25euro,
            fate,
            success,
            ministryabbreviation
        ])

    with open('bmas10-16.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(result)
