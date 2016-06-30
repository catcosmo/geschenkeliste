# coding=utf-8
__author__ = 'krawallmieze'

import codecs
import re

newRow = ['gift', 'Bundesfinanzministerium','2015', 'n.a.', 'fate', 'BMF', 'success']

# following writes txt lines in csv and deletes preceding running no.
with codecs.open('data/csvTxtPreprocess/BMF2016.txt', mode='r+', encoding='utf-8') as data:
    dump = codecs.open('bmf2016.csv', mode='w', encoding='utf-8')
    for line in data:
        line = re.sub("([0-9]{1,3}\s?\|)", r"", line)
        dump.write(line)
