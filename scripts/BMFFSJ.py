# coding: utf-8
import re
file = open('data/csvTxtPreprocess/BMFSFJ.csv', 'r+')
data = file.read()
csv = open('BMFSFJ-done.csv', 'w')
data = re.sub('[,]{2,}', ',,', data)
data = re.sub('[,]{2}[ ][,]{2}', ',,', data)
print data
list =  re.split('[,]{2}', data)
for item in list:
    csv.write(item + '\n')