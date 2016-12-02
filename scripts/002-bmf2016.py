# coding=utf-8

import codecs
import csv

with open('../data/csvTxtPreprocess/bmf2016.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')

    result = []

    for index, row in enumerate(reader):
        print(index, row)

        value = row[0].split(' €', 1)[0]
        value = value.replace(',', '.')
        if value.startswith('ca'):
            print('does', value)
            value = value.split(' ', 1)[1]

        if value.startswith('<'):
            value = None

        if 'nicht' in str(value):
            value = None

        day, month, year = None, None, None
        gift = row[1].strip()

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

        fate = row[3] if len(row) >= 4 else None
        success = 'ja' in row[2]
        ministryabbreviation = 'bmf'

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
