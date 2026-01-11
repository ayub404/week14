teams = {
    "Alpha": [101, 102, 103],
    "Beta":  [103, 104, 105], # 103 is a duplicate (Alpha & Beta)
    "Gamma": [106, 107],      # Clean
    "Delta": [102, 108]       # 102 is a duplicate (Alpha & Delta)
}

seen = set()
disqualified = set()
for team in teams.values():
    for student in team:
        if student in seen:
            disqualified.add(student)
        else:
            seen.add(student)
    
valid_teams = []
for team, students in teams.items():
    if set(students) - disqualified == set(students):
        valid_teams.append(team)
print(valid_teams)