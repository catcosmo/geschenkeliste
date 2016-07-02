# coding: utf-8
import codecs

data = codecs.open('data/csvTxtPreprocess/BMAS2010-16.csv', 'r+', encoding='utf-8')
newRow = ['gift', 'Bundesministerium fuer Arbeit und Soziales','2015', 'n.a.', 'fate', 'BMAS', 'success' ]
csv = codecs.open('bmas.csv', 'w', encoding='utf-8')

for row in data:
    temp = row.split(',')
    print temp
    #get gift
    newRow[0] = ''.join(temp[1].rstrip())
    #get date
    datetemp = temp[0].split('/')
    newRow[3] = '/'.join(datetemp[::-1])
    #get fate
    for i in range(4, 7):
        options = {
            4: 'Behalten',
            5: 'Behalten (Dienstgebrauch)',
            6: 'Abgabe Dienstherr',
            7: 'Rückgabe'
        }
        if temp[i] == 'x':
            print options[i]
            newRow[4] = options[i]
            #get success
            if i == 4|5:
                newRow[6] == 'success'
            else:
                newRow[6] == 'fail'



    csv.write(', '.join(newRow) + '\n')
