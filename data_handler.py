import csv

with open('sample_data.csv', 'r') as f:
    reader = csv.reader(f)
    for i, line in enumerate(reader):
        print(line)
        # if i == 0:
        #     last_round = len(line) // 2
        #     name = line[0]
        #     n = 0
        #     while 1 == last_round:
        #         pass
