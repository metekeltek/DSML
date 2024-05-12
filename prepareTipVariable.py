import csv

def floatToBool(tip):
    if tip.lower() == 'no tip given':
        return False

    tip_float = float(tip)
    if tip_float > 0.0:
        return True
    else:
        return False


with open('../data/2019_03.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    header = next(reader)
    rows = list(reader)

for i in range(len(rows)):
    print(f'{i+1} from {len(rows)}')
    rows[i][13] = floatToBool(rows[i][13])

with open('preparedData.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header)
    writer.writerows(rows)
