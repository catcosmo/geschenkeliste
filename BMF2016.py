# coding=utf-8
__author__ = 'krawallmieze'

import codecs
import re

newRow = ['gift', 'Bundesfinanzministerium','2015', 'n.a.', 'fate', 'BMF', 'success']

# following writes txt lines in csv and deletes preceding running no.
#with codecs.open('data/csvTxtPreprocess/BMF2016.txt', mode='r+', encoding='utf-8') as data:
    #dump = codecs.open('bmf2016.csv', mode='w', encoding='utf-8')
    #for line in data:
        #line = re.sub("([0-9]{1,3}\s?\|)", r"", line)
        #dump.write(line)

#sorts single entries and writes in final dict
csv = codecs.open('BMF16.csv', 'w', encoding='utf-8')

with codecs.open('bmf2016.csv', 'r+', encoding='utf-8') as data:
    fatefail = []
    i = 0
    for line in data:
        i+=1
        #get price
        temp = line.split()
        if temp[0] == "nicht":
            newRow[3] = 'n.a.'
            rest = ' '.join(temp[2:]).lstrip()
        else:
            line = re.sub(u'έ|ε|£', u'€', line)
            dump = re.split(u'€', line, 1, flags=re.IGNORECASE)
            newRow[3] = ''.join(dump[0])
            #rest = dump[1].rstrip().lstrip()

        #getfate
        if 'ja' in rest:
            newRow[4] = 'Behalten'
            newRow[6] = 'success'
            rest = ''.join(rest.split('ja')[0]).rstrip()
        elif 'nein' in rest:
            newRow[4] = ''.join(rest.split('nein')[1])
            newRow[6] = 'fail'
            rest = ''.join(rest.split('nein')[0]).rstrip()
        else:
            fatefail.append(i)
            newRow[4] = 'n.a.'

        #get gift name
        # gift = re.split('ja|nein', rest, 1, flags=re.IGNORECASE)
        if ',' in rest:
            newRow[0] = '\'' + rest + '\''
        else:
            newRow[0] = rest


        #write to csv
        str = ', '.join(newRow)
        csv.write(str+'\n')
