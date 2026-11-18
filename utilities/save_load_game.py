import json
import os
from entities.tower import Tower

SAVE_FOLDER = os.path.join(
	os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "saved_games")
MAX_SAVES = 5

loading_game = None
chosen_save = 1
chosen_name = ""
def save_path(save):
	return os.path.join(SAVE_FOLDER, f"save{save}.json")


def build_save(save_name, map_choice, level, wave,  player, towers):
	save_data = {
		"name": save_name,
		"map": map_choice,
		"level": level,
		"wave": wave,
		"hp": player.hp,
		"money": player.money,
		"towers": [{
			"type": tower.nick_what_to_put_here,
			"position": list(tower.position)}
				for tower in towers],
	}


def save_game(save, data):
	os.makedirs(SAVE_FOLDER, exist_ok=True)
	with open(save_path(save), "w") as file:
		json.dump(data, file)


def load_game(save):
	try:
		with open(save_path(save)) as save_file:
			return json.load(save_file)
	except:
		return None


