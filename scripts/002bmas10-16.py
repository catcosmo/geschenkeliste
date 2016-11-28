# coding=utf-8
import codecs
import shlex

data = codecs.open('../data/csvTxtPreprocess/BMAS2010-16.csv', 'r+', encoding='utf-8')
newRow = ['gift', 'year', 'month', 'day', '00,00', 'false', 'false', 'fate', 'n.a.', 'BMAS']
csv = codecs.open('bmas.csv', 'w', encoding='utf-8')

for row in data:
    temp = shlex.split(row)
    #get gift
    newRow[0] = ''.join(temp[1].rstrip())
    #get date
    datetemp = temp[0].split('/')
    if len(datetemp)== 3:
        newRow[1] = datetemp[2]
        newRow[2] = datetemp[1]
        newRow[3] = datetemp[0]
    else:
        print datetemp
        print temp
    #get price
    if temp[2] == 'x':
        newRow[5] = 'true'
    if temp[3] == 'x':
        newRow[6] = 'true'

    #get fate
    for i in range(4, 8):
        options = {
            4: 'Behalten',
            5: 'Behalten (Dienstgebrauch)',
            6: 'Abgabe Dienstherr',
            7: 'Rueckgabe'
        }
        if temp[i] == 'x':
            newRow[7] = options[i]
            #get success
            if i in range(4,6):
                newRow[8] = 'success'
            else:
                newRow[8] = 'fail'


    csv.write(', '.join(newRow) + '\n')