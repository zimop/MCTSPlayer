from collections import deque
from copy import deepcopy
import time
from template import Agent, GameRule
import random
import heapq
from Azul.azul_model import AzulGameRule as GameRule
from Azul.azul_model import AzulState as GameState
from itertools import count

THINKTIME   = 0.7
NUM_PLAYERS = 2
Q_REWARDS = dict()

class myAgent(Agent):
    def __init__(self,_id):
        super().__init__(_id)
        self.game_rule = GameRule(NUM_PLAYERS)
    
    def GetActions(self, state):
        return self.game_rule.getLegalActions(state, self.id)
    
    def SelectAction(self,actions,root_state):
        # making sure the algorithm does not time out
        start_time = time.time()
        # Discount value
        gamma = 0.9
        start = deepcopy(root_state)
        count = 0
        while time.time()-start_time < THINKTIME:
            count += 1
            openList = [start]
            while len(openList) and time.time()-start_time < THINKTIME:
                state = openList.pop(0)
                new_actions = self.GetActions(state)
                
                
                firstAction = new_actions[0]
                firstState = deepcopy(state)
                
                self.game_rule.generateSuccessor(firstState, firstAction, self.id)
                
                first_futureScore = firstState.agents[self.id].ScoreRound()[0]
                first_futureBonus = firstState.agents[self.id].EndOfGameScore()
                first_future_reward = first_futureScore + first_futureBonus
                
                # initializing the first action as the action with the maximum reward
                max_state = firstState
                max_action = firstAction
                max_future_reward = first_future_reward 
                
                
                #future_reward = 0
                
                # this loop checks all the possible actions and explores all the immediate states to find the future reward
                for a in new_actions[1:]:
                    
                    
                    future_reward = 0
                    next_state = deepcopy(state)
                    
                    self.game_rule.generateSuccessor(next_state, a, self.id)
                    openList.append(next_state)
                    # if the state is already in the Q table, then take that reward as the future reward.
                    if (next_state in Q_REWARDS.keys()):
                        future_reward, _, _ = Q_REWARDS[next_state]
                       
                    # else, compute the reward of the state as the current state reward
                    else:
                        futureScore = next_state.agents[self.id].ScoreRound()[0]
                        futureBonus = next_state.agents[self.id].EndOfGameScore()
                        future_reward = futureScore + futureBonus
                      
                    if (future_reward > max_future_reward):
                        max_future_reward = future_reward
                        max_state = next_state
                        max_action = a
                
                currState = deepcopy(state)        
                scoreChange = currState.agents[self.id].ScoreRound()[0]
                bonus = currState.agents[self.id].EndOfGameScore()
                reward = scoreChange + bonus
                
                
                #Opponent
                
                # update the value of the state in the q table, with its reward
                Q_REWARDS[state] = ((reward + gamma*max_future_reward), max_state, max_action)
              
        return Q_REWARDS[start][2]
