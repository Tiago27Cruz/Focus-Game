from model.Player import Player
from controller.SelectMenuController import SelectMenuController
from view.SelectMenuView import SelectMenuView
from config import *

class SelectMenuState:
    def __init__(self, state_manager):
        self.state_manager = state_manager
        self.player_types = ["Player", "Easy Bot", "Medium Bot", "Hard Bot", "MCTS Bot"]
        self.selected_orange = 0    # Index of the currently selected player 1 (orange)
        self.selected_blue = 0      # Index of the currently selected player 2 (blue)
        self.selected_size = 1
        self.controller = SelectMenuController(self)
        self.view = SelectMenuView(self)

    # Start the game with the selected players and board size
    def start_game(self):
        self.state_manager.start_game(BOARD_SIZES[self.selected_size], Player('Orange', self.player_types[self.selected_orange]), Player('Blue', self.player_types[self.selected_blue]))

    # Update the selected player 1
    def update_selected_orange(self, player):
        match player:
            case "Player":
                self.selected_orange = 0
            case "Easy Bot":
                self.selected_orange = 1
            case "Medium Bot":
                self.selected_orange = 2
            case "Hard Bot":
                self.selected_orange = 3
            case "MCTS Bot":
                self.selected_orange = 4
    
    # Update the selected player 2
    def update_selected_blue(self, player):
        match player:
            case "Player":
                self.selected_blue = 0
            case "Easy Bot":
                self.selected_blue = 1
            case "Medium Bot":
                self.selected_blue = 2
            case "Hard Bot":
                self.selected_blue = 3
            case "MCTS Bot":
                self.selected_blue = 4
    
    # Update the selected board size
    def update_selected_size(self, size):
        self.selected_size = size

    def to_quit(self):
        self.state_manager.to_quit()

    def run(self, window):
        self.controller.handle_event()
        self.view.draw(window)