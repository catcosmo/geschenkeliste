__author__ = 'krawallmieze'



#gets data in csv form and turns it into a list of dicts
def csvtolist(data):
    giftlist = list()
    for row in csvTable:
        gift = {}
        gift['gift'] = row[0]
        gift['ministry'] = row[1]
        gift['date'] = row[2]
        gift['value'] = row[3]
        gift['fate'] = row[4]

        giftlist.append(gift)

