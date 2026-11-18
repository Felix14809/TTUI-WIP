from enums.game_states import GameState
import maps.map_generator as map
import utilities.save_load_game as save

def options(game_state):
    if game_state == GameState.START:
        return ["Start Game", "Select Map", "Change Difficulty", "Load Game", "Exit"]
    elif game_state == GameState.PAUSED:
        return ["Resume", "Restart", "Save Game", "Load Game", "Exit"]
    elif game_state == GameState.MAP_SELECTION:
        return list(map.MAP_OPTIONS) + ["BACK"]
    elif game_state == GameState.SAVE_SELECTION:
        return save.save_name() + ["BACK"]
    else:
        return ["Restart", "Save Score", "Load Game", "Exit"]

#Returns the menu Selection
def state(game_state):
    if game_state == GameState.START:
        return "TTUI TOWER DEF"
    elif game_state == GameState.PAUSED:
        return "PAUSED"
    elif game_state == GameState.MAP_SELECTION: 
        return "PICK MAP"
    elif game_state == GameState.SAVE_SELECTION:
        return "PICK SAVE"
    else:
        return "GAME OVER"