import csv
import random

TEAM_NUM = 5
TEAM = dict()
LEADERS = list()
PREV_LEADERS = ["Angie", "Susie", "Tami", "Otis", "Ken"]
PREV_LEADERS = [member.lower() for member in PREV_LEADERS]
PREV_TEAMS = {
    1: ["Acker", "Angie", "Ann", "Dale", "Ed"],
    2: ["Joy", "Kevin", "Leo", "Susie"],
    3: ["EL", "Mason", "Roxy", "Tami"],
    4: ["Jane", "Jeus", "Lego", "Otis"],
    5: ["Becky", "Jake", "Ken", "Matthew"]
}
PREV_TEAMS = {
    idx: [member.lower() for member in members]
    for idx, members in PREV_TEAMS.items()
}


for i in range(1, TEAM_NUM+1):
    TEAM[i] = list()

team_org = list()
team_org_members = dict()
team_members = list()

with open('members.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        org_name = line[0]
        org_members = [member.lower().strip() for member in line[1].split(",")]
        team_org.append(org_name)
        team_org_members[org_name] = org_members
        team_members += org_members

group_num = random.randint(1, TEAM_NUM)
random.shuffle(team_org)
for _ in range(len(team_org)):
    org = team_org.pop()
    members = team_org_members[org]
    random.shuffle(members)
    for _ in range(len(members)):
        member = members.pop()
        group_members = TEAM[group_num]
        group_members.append(member)
        TEAM[group_num] = group_members
        group_num += 1
        if group_num > TEAM_NUM:
            group_num = 1

print(TEAM)
for team_num in TEAM.keys():
    people = TEAM[team_num]
    random.shuffle(people)
    for person in people:
        if person not in PREV_LEADERS:
            LEADERS.append(person)
            break

print(LEADERS)
