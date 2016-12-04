__author__ = 'krawallmietze'
# -*- coding: utf-8 -*-

import codecs

with codecs.open('data/done/BMU.txt', 'r', 'utf-8') as data:
    csv = codecs.open('BMU.csv', 'w', 'utf-8')
    csv.write('Geschenk; Ministerium; Datum; Wert; Verbleib\n')
    oldRow = ['gift', '\'Bundesministerium fuer Umwelt, Naturschutz, Bau und Reaktorsicherheit\'','seit 2009', 'n.a.', 'fate', 'BMU', 'n.a.']
    for row in data:
        newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'BMU']

        #get fate
        if row.split(' ', 1)[0] == 'Verwendung':
            newRow[4] = row.rstrip()
        elif row.split(' ', 1)[0] == 'als':
            newRow[4] = row.rstrip()
        else:
            row = row[:-1]
            if ',' in row:
                newRow[0] = '\''+ row + '\''
            else:
                newRow[0] = row
        if newRow[0] != 'gift' and newRow[4] != 'fate':
            str = ', '.join(newRow)
            csv.write(str + '\n')
            newRow = ['gift', 'Bundesministerium fuer Umwelt, Naturschutz, Bau und Reaktorsicherheit','seit 2009', 'n.a.', 'fate', 'BMU', 'n.a.']



