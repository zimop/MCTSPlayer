import copy
import time
import random
from Azul.azul_model import AzulGameRule as GameRule
from copy import deepcopy
from collections import deque
from template import Agent
import random

THINKTIME = 0.3
NUM_PLAYERS = 2


class myAgent(Agent):
    def __init__(self, _id):
        super().__init__(_id)
        self.game_rule = GameRule(NUM_PLAYERS)

    ## Check for all the actions that are legal for a specific state
    def GetActions(self, state, opponentId):
        return self.game_rule.getLegalActions(state, opponentId)

    def SelectAction(self, actions, game_state):
        startTime = time.time()
        max_reward = 0
        ##Initialise a random best action
        currBestAction = random.choice(actions)
    
        
        for action in actions:
            inTime = time.time()
            next_state = copy.deepcopy(game_state)

            self.game_rule.generateSuccessor(next_state, action, self.id)

            # The reward is the bonus that you receive at the end of the game + the score that you get with the current state
            scoreChange = next_state.agents[self.id].ScoreRound()[0]
            bonus = next_state.agents[self.id].EndOfGameScore()
            reward = scoreChange + bonus

            future_reward = 0
            counter = 0
            gamma = 0.2
            
            # this is the counter to go from player 1, player 2, then back to player 1 and so forth
            i = abs(self.id - 1)
            
            # This indicates that it is the last round
            lastRound = False

            #run the simulations until there are no more tiles remaining
            while (not next_state.TilesRemaining()):
                counter = counter + 1
                result = self.simulate(next_state, i)
                i = abs(i - 1)
                lastRound = result[2]
                if (lastRound):
                    break
                # if it is the current player, then add the future rewards from the simulation to the reward, with the discount
                if (i == self.id):
                    future_reward = result[1]
                    reward = reward + future_reward * (gamma**counter)
                next_state = result[0]

            # find the maximum reward action and return the best action out of all that can be applied in this state
            if reward > max_reward:
                currBestAction = action
                max_reward = reward

        return currBestAction

    # This function simulates the best move from the state for the given player. The best move is determined by the reward.
    def simulate(self, next_state, opponentId):
        opponentActions = self.GetActions(next_state, opponentId)
        max_reward = 0
        best_move = None

        for action in opponentActions:
            opp_next_state = copy.deepcopy(next_state)
            self.game_rule.generateSuccessor(
                opp_next_state, action, opponentId)

            oppScore = opp_next_state.agents[opponentId].ScoreRound()[0]
            oppBonus = opp_next_state.agents[opponentId].EndOfGameScore()
            reward = oppScore + oppBonus

            if (reward >= max_reward):
                best_move = action
                max_reward = reward
        if (best_move == None):
            return (None, None, True)
        self.game_rule.generateSuccessor(next_state, best_move, opponentId)
        return (next_state, max_reward, False)
