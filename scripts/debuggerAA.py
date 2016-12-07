import csv

with open('/Users/krawallmietze/code/python/geschenkeliste/data/quoteKilled/aa13.csv', 'r+') as file:
    data = csv.reader(file, delimiter=',', quotechar='"')
    for row in data:
        if row[-1] != 'AA':
            print row[-1], row[0]