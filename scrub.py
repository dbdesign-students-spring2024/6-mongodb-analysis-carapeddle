import csv



f = open("listings.csv", 'r')
csvfile = open('data/listings_clean.csv', 'w', encoding='utf_8')

data = list(csv.DictReader(f))
csvfile.write(','.join(data[0].keys()) + '\n')    
writer = csv.writer(csvfile)
count = -1
for line in data:
    count += 1
    keys = line.keys()
    for key, value in line.items():
        if 'è' in value:
            newvar = value.replace('è', 'e')
            data[count][key] = newvar
    for key, value in line.items():
        if 'ë' in value:
            newvar = value.replace('ë', 'e')
            data[count][key] = newvar
    for key, value in line.items():
        if '·' in value:
            newvar = value.replace('·', '/')
            data[count][key] = newvar
    for key, value in line.items():
        if '★' in value:
            newvar = value.replace('★', '*')
            data[count][key] = newvar
    for key, value in line.items():
        if value.isascii() == False or 'N/A' in value or '[]' in value:
            data[count][key] = ''
    for key, value in line.items():   
        data[count][key] = value.replace('\n', ' ').replace('\t', ' ').replace('<br />', '').replace('\r', '').strip()
    
        
    newlist = []
    for value in line.values():
        newlist.append(value)
    writer.writerow(line.values())

csvfile.close()




