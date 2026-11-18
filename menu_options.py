import sys
import utilities.save_load_game as saves
import maps.map_generator as map
from enums.game_states import GameState
from game_menu import game_menu

#from game_state_strings import options, state

def menu_choice(stdscr, selection):
    if selection == "Exit":
        sys.exit()
    elif selection == "Restart":
        return GameState.RESTART
    elif selection in ("Resume", "Start Game"):
        return GameState.PLAYING
    elif selection == "Save Game":
        return GameState.SAVING
    elif selection == "Load Game":
        return GameState.PLAYING
    elif selection == "Select Map":
        choice = game_menu(stdscr, GameState.MAP_SELECTION)
        map.MAP_CHOICE =  map.MAP_OPTIONS[choice]
    elif selection == "Save Score":
        pass
    return GameState.START    