import csv
import json

reward_tank_ids = [58369, 46849, 15617, 57937]
meta_tank_ids = [6193, 16897, 22017, 15697, 19009, 2929, 5265]
situational_tank_ids = [3681, 14609, 4737, 9489, 3473, 13857, 13089]

with open("2021-11-19.json", 'r') as json_file:
    player_data = json.load(json_file)

total_marks = []
for member in player_data:
    for tank in member['overallStats']['tankWN8']:
        count = 0
        tank_player_dict = {}
        if tank['moe'] != 0 and tank['id'] in reward_tank_ids + meta_tank_ids + situational_tank_ids:
            if tank['id'] in reward_tank_ids:
                tank_player_dict['type'] = "reward"
            elif tank['id'] in meta_tank_ids:
                tank_player_dict['type'] = "meta"
            elif tank['id'] in situational_tank_ids:
                tank_player_dict['type'] = "situational"
            else:
                print('fuck')
            tank_player_dict['name'] = member['summary']['nickname']
            tank_player_dict['tank'] = tank['name']
            tank_player_dict['mark_value'] = tank['moe']
            tank_player_dict['position'] = member['clanData']['role']
            count += 1
        if count !=0:
            total_marks.append(tank_player_dict)

csv_columns = ['name', 'tank', 'mark_value', 'type', 'position']
csv_file = 'raw.csv'

try:
    with open(csv_file, "w") as csvFile:
        writer = csv.DictWriter(csvFile, fieldnames=csv_columns)
        writer.writeheader()
        for data in total_marks:
            writer.writerow(data)
except Exception as e:
    print('something fucked you idiot'.join(str(e)))
