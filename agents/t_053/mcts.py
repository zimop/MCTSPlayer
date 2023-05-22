from template import Agent 
from utils import *
from copy import deepcopy 
from Azul.azul_model import AzulGameRule as GameRule

NUM_PLAYERS = 2
####### MCTS #########
class myAgent(Agent):

    #initialise 
    def __init__(self, _id):
        super().__init__(_id)
        self.game_rule = GameRule(NUM_PLAYERS)
        self.id = _id
        self.weights = {"complete": [1], "not-complete": [1]}
        self.discount =  0.8 
        self.alpha = 0.3  
        self.epsilon = 1

    def SelectAction(self, actions, game_state):
        action_list = dict()
        maxQ = float("-inf")
        current_maximum = None
        


        for action in actions:
            q_value = 0.0
            features_list = []

            game_state_copy = deepcopy(game_state)
            next_state = self.game_rule.generateSuccessor(game_state_copy, action, self.id)
            if next_state.agents[self.id].GetCompletedRows() > 0:
                key = "complete"
            else:
                key = "not-complete"

            current_expected_score, current_bonus = self.CalculateExpectedScore(game_state)
            next_expected_score, next_bonus = self.CalculateExpectedScore(next_state)
            
            expectedGain = next_expected_score + next_bonus - current_expected_score - current_bonus
            features_list.append(expectedGain)

            features = {key : features_list}
            
            if "complete" in features:
                key = "complete"

            else:
                key = "not-complete"

            for x in range(len(self.weights[key])):
                q_value = q_value + (self.weights[key][x] * features[key][x])
            
            action_list[action] = q_value


        for key in action_list.keys():
            if action_list[key] > maxQ:
                current_maximum = key
                maxQ = action_list[key]

        return current_maximum
    
    def CalculateExpectedScore(self, state):
        current_state = state.agents[self.id]
        expected_score, expected_used_tiles = current_state.ScoreRound()
        bonus_points = current_state.EndOfGameScore()
        return expected_score, bonus_points
    
    