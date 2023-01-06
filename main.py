import csv

f = open('random.csv', 'r')
reader = csv.reader(f)

for i, line in enumerate(reader):
    if i == 0:
        last_round = len(line) // 2
        name = line[0]
        n = 0
        while 1 == last_round:
            pass
    # print(line)
f.close()