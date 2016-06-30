__author__ = 'krawallmietze'
import HTML

#getdict
gifts = open(giftlist.txt)

#convert to HTML
#turn list of dict into list of lists
#to turn dict to list use: gifts.values() or gifts.keys()

table_data = []
for gift in gifts:
    table_data.append(gift.values()) #need to order list

htmlcode = HTML.table(table_data,
    header_row=gifts[0].keys())
print htmlcode