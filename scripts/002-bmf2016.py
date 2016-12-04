# coding=utf-8

import codecs
import csv

with open('../data/csvTxtPreprocess/bmf2016.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

    result = []

    for index, row in enumerate(reader):
        print(index, row)

        day, month, year = '00', '00', '2016'
        gift = row[1].strip()

        value = row[0].split(' €', 1)[0]
        value = value.replace(',', '.')
        if value.startswith('ca'):
            print('does', value)
            value = value.split(' ', 1)[1]

        if value.startswith('<'):
            value = '00.00'

        if 'nicht' in value:
            value = '00.00'
            under25euro = False
            over25euro = False
        else:
            under25euro = False
            try:
                under25euro = float(value) < 25
            except Exception as e:
                under25euro = (row[0][0] == '<')
                pass

            over25euro = False
            try:
                over25euro = float(value) > 25
            except Exception as e:
                pass


        if row[3] != '':
            fate = row[3].strip()
        else:
            fate = "Eigenbehalt"
        print fate

        success = 'ja' in row[2]
        ministryabbreviation = 'BMF'

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

    with open('bmf-2016.csv', 'wb') as f:
        writer = csv.writer(f)
        writer.writerows(result)
