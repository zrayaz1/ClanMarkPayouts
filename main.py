import requests
from typing import List
import json
from datetime import datetime

clan_id = 1000002659
tomato_clan_url = "https://tomatobackend.herokuapp.com/api/clan/com/{}"
tomato_player_url = 'https://tomatobackend.herokuapp.com/api/player/com/{}?cache=false'


def get_player_list(id_clan: int) -> List[int]:
    output = requests.get(tomato_clan_url.format(id_clan)).json()
    player_ids = [i['account_id'] for i in output['members']]
    return player_ids


def get_player_stats(player_ids: List[int]):
    player_data = []
    for player_id in player_ids:
        output = requests.get(tomato_player_url.format(player_id))
        try:
            json_output = output.json()
            player_data.append(json_output)
            print(json_output['summary']['nickname'])
        except Exception:
            print("something fucked")
            pass
    return player_data


output_data = get_player_stats(get_player_list(clan_id))
json_str = json.dumps(output_data)
with open(f"{datetime.today().strftime('%Y-%m-%d')}.json", 'w') as outfile:
    outfile.write(json_str)
