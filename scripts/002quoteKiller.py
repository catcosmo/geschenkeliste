import csv
import re
import os.path

folder = '../data/csvNewModel'
exit_folder = '../data/quoteKilled'
#aa13 = open('../data/csvNewModel/aa13QK.csv', 'w')

for filename in os.listdir(folder):
    file_path = str(folder) + '/' + str(filename)
    exit_file_path = str(exit_folder) + '/' + str(filename)
    exit_file = open(exit_file_path, 'w')
    with open(file_path) as current_file:
        reader = csv.reader(current_file, delimiter=',', quotechar='"')
        for row in reader:
            newRow = ['gift', '0000', '00', '00', '00.00', 'false', 'false', 'fate', 'n.a.', 'AA']
            row[0] = re.sub('"', '\'', row[0])
            newRow[0] = '"' + row[0] + '"'


            #newRow.append(row[1:])
            for i in range(1,10):
                newRow[i] = row[i]

            print newRow
            exit_file.write(','.join(newRow) + '\n')