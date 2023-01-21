import csv


class DataLoader:
    def __init__(self, csv_path="data.csv", team_len=5):
        self.csv_path = csv_path
        self.team_len = team_len
        # self.this_round = None
        # self.last_round = None
        # self.required_check_round = 1
        # self.required_check_leader = 1

    def load_prev_data(self):
        prev_team = {i+1: list() for i in range(self.team_len)}
        with open(self.csv_path, "r") as f:
            reader = csv.reader(f)
            titles = next(reader)
            total_data_len = len(titles)
            for idx, line in enumerate(reader):
                prev_team[idx+1] = line[total_data_len-2]
        return prev_team


class Test:
    def logic(self):
        with open('data.csv', 'r') as f:
            reader = csv.reader(f)
            titles = next(reader)
            for idx, info_set in enumerate(titles):
                print(idx, info_set)
                if idx == 0:
                    continue
                num, info = info_set.split("-")[:2]
                if "team" in info:
                    team = num
                elif "round" in info:
                    rnd = num
            for member in reader:
                name = member[0]

    def test(self):
        with open('sample_data.csv', 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                print(line)


if __name__ == '__main__':
    app = Test()
    mode = None
    while mode not in ["q", "exit"]:
        mode = input()
        if mode in ["logic", "l", "run"]:
            app.logic()
        elif mode in ["test", "t"]:
            app.test()
        else:
            a = DataLoader()
            a.load_prev_data()
