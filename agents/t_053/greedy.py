from template import Agent
from utils import *
from copy import deepcopy
from Azul.azul_model import AzulGameRule as GameRule

NUM_PLAYERS = 2

class myAgent(Agent):

    def __init__(self, _id):
        super().__init__(_id)
        self.game_rule = GameRule(NUM_PLAYERS)

    def SelectAction(self, moves, game_state):
        return self.heuristic_search(game_state, moves)

    def heuristic_search(self, game_state, available_actions):
        current_round_score = game_state.agents[self.id].ScoreRound()[0]
        # print(current_round_score)
        current_bonus_score = game_state.agents[self.id].EndOfGameScore()

        
        best_action = None
        highest_score = float('-inf')
        
        moves_cnt = len(available_actions)
        for i in range(moves_cnt):
            action = available_actions[i]

            game_state_copy = deepcopy(game_state)

            player = self.game_rule.generateSuccessor(game_state_copy, action, self.id)
            tiles_grab = action[2]

            if tiles_grab.pattern_line_dest == -1:
                round_score, used_tiles = player.agents[self.id].ScoreRound()
                h = round_score - current_round_score

            else:
                tiles_grabbed = player.agents[self.id].lines_number[tiles_grab.pattern_line_dest]
                tiles_needed = tiles_grab.pattern_line_dest + 1 - tiles_grabbed                
                player.agents[self.id].AddToPatternLine(tiles_grab.pattern_line_dest, tiles_needed, tiles_grab.tile_type)
                round_score, used_tiles = player.agents[self.id].ScoreRound()
                bonus_score = player.agents[self.id].EndOfGameScore()
                h = round_score + bonus_score - current_round_score - current_bonus_score - tiles_needed

            if h > highest_score:
                highest_score = h
                best_action = action
        return best_action