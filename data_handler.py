import csv
import random

MEMBERS = [
    ["운영", "Acker, Becky, EL, Jane, Kevin"],
    ["마케팅", "Joy, Roxy"],
    ["기획", "Angie, Otis, Susie, Tami"],
    ["디자인", "Ann, Ken"],
    ["서버", "Dale, Ethan, Jake, Jeus, Leo"],
    ["클라이언트", "Ed, Lego, Mason, Matthew"],
]

MEMBERS_NAME_DICT = {
    "acker": "Acker", "angie": "Angie", "ann": "Ann", "becky": "Becky",
    "dale": "Dale", "ed": "Ed", "el": "EL", "ethan": "Ethan", "jake": "Jake",
    "jane": "Jane", "jeus": "Jeus", "joy": "Joy", "ken": "Ken",
    "kevin": "Kevin", "lego": "Lego", "leo": "Leo", "mason": "Mason",
    "matthew": "Matthew", "otis": "Otis", "roxy": "Roxy", "susie": "Susie", "tami": "Tami"
}


class DataLoader:
    def __init__(
        self,
        prev_data_file_path="data.csv",
        total_team_number=5,
        round_number=1,
    ):
        self.prev_data_file_path = prev_data_file_path
        self.total_team_number = total_team_number
        self.round_number = round_number

    def load_prev_data(self):
        if self.round_number == 1:
            prev_team_list_dict = {
                i+1: list() for i in range(self.total_team_number)
            }
            prev_leader_list = list()
            with open(self.prev_data_file_path, "r") as f:
                reader = csv.reader(f)
                titles = next(reader)
                total_data_len = len(titles)
                for idx, line in enumerate(reader):
                    prev_team_list_dict[idx + 1] = line[total_data_len - 2]
                    prev_leader_list.append(line[total_data_len - 1])
            return prev_team_list_dict, prev_leader_list
        elif self.round_number == 2:
            pass


class DataProcessor:
    def __init__(
        self,
        prev_data_file_path=None,
        member_data_file_path=None,
        prev_leader_list=None,
        prev_team_list_dict=None,
        total_team_number=5
    ):
        self.total_team_number = total_team_number
        self.member_data_file_path = member_data_file_path
        self.prev_leader_list = [
            member.lower() for member in prev_leader_list
        ] if prev_leader_list != None else None
        self.prev_team_list_dict = {
            idx: [member.lower() for member in members]
            for idx, members in prev_team_list_dict.items()
        } if prev_team_list_dict != None else None
        self.team_list = dict()
        self.leader_list = list()

    def process(self):
        for i in range(1, self.total_team_number+1):
            self.team_list[i] = list()

        team_org = list()
        team_org_members = dict()
        team_members = list()
        if self.member_data_file_path:
            with open(self.member_data_file_path, 'r') as f:
                reader = csv.reader(f)
                for line in reader:
                    org_name = line[0]
                    org_members = [
                        member.lower().strip()
                        for member in line[1].split(",")
                    ]
                    team_org.append(org_name)
                    team_org_members[org_name] = org_members
                    team_members += org_members
        else:
            for line in MEMBERS:
                org_name = line[0]
                org_members = [
                    member.lower().strip()
                    for member in line[1].split(",")
                ]
                team_org.append(org_name)
                team_org_members[org_name] = org_members
                team_members += org_members

        group_num = random.randint(1, self.total_team_number)
        random.shuffle(team_org)
        for _ in range(len(team_org)):
            org = team_org.pop()
            members = team_org_members[org]
            random.shuffle(members)
            for _ in range(len(members)):
                member = members.pop()
                group_members = self.team_list[group_num]
                group_members.append(member)
                self.team_list[group_num] = group_members
                group_num += 1
                if group_num > self.total_team_number:
                    group_num = 1

        for team_num in self.team_list.keys():
            people = self.team_list[team_num]
            random.shuffle(people)
            if self.prev_leader_list is not None and len(self.prev_leader_list) > 1:
                for person in people:
                    if person not in self.prev_leader_list:
                        self.leader_list.append(person)
                        break
            else:
                self.leader_list.append(people[0])

        self.change_team_member_name_to_origin_name_and_str()
        self.change_leader_name_to_origin_name()

    def change_team_member_name_to_origin_name_and_str(self):
        lower_name = self.team_list
        self.team_list = dict()
        for idx, group in lower_name.items():
            lower_name = list()
            for name in group:
                origin_name = MEMBERS_NAME_DICT[name]
                lower_name.append(origin_name)
            self.team_list[idx] = self.list_to_str(lower_name)

    def list_to_str(self, target_list):
        return_str = ", ".join(target_list)
        return return_str

    def change_leader_name_to_origin_name(self):
        lower_name = self.leader_list
        self.leader_list = list()
        for name in lower_name:
            try:
                origin_name = MEMBERS_NAME_DICT[name]
                self.leader_list.append(origin_name)
            except KeyError:
                origin_name = name[0].upper()+name[1:]
                self.leader_list.append(origin_name)
