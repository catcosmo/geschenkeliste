import csv
import re

aa13 = open('../data/csvNewModel/aa13QK.csv', 'w')
with open('bmf-2016.csv', 'wb') as f:
    writer = csv.writer(f)


with open('../data/csvNewModel/aa13.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'AA']
        row[0] = re.sub('"', '\'', row[0])
        newRow[0] = '"' + row[0] + '"'

        #newRow.append(row[1:])
        for i in range(1,10):
            newRow[i] = row[i]

        print newRow

        aa13.write(newRow + '\n')