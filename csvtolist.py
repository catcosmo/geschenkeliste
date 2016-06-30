__author__ = 'krawallmieze'

import csv

#open csv file
data = open(irgendein.csv)
try:
    csvTable = csv.reader(data)
finally:
    data.close()

#create list and write csv lines as dicts into list
giftlist = []
for row in csvTable:
    gift = {}
    gift['gift'] = row[0]
    gift['ministry'] = row[1]
    gift['date'] = row[2]
    gift['value'] = row[3]
    gift['fate'] = row[4]

    giftlist.append(gift)

#create txt and write dict giftlist in file
f = open("bmxy.txt","w")
f.write(giftlist)
f.close()
