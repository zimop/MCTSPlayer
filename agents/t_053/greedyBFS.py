from collections import deque
from copy import deepcopy
import time
from template import Agent, GameRule
import random
import heapq
from Azul.azul_model import AzulGameRule as GameRule
from Azul.azul_model import AzulState as GameState
from itertools import count

THINKTIME   = 0.95
NUM_PLAYERS = 2

class myAgent(Agent):
    def __init__(self,_id):
        super().__init__(_id)
        self.game_rule = GameRule(NUM_PLAYERS)
        self.game_state = GameState(NUM_PLAYERS)
    
    def isGoal(self, state, action):
        numRowsCompleted = 0
        numRowsCompletedSucc = 0
        for i in range(state.agents[self.id].GRID_SIZE):
            if (state.agents[self.id].lines_number[i] == i+1):
                numRowsCompleted += 1
                
        state = self.game_rule.generateSuccessor(state, action, self.id)
        
        for j in range(state.agents[self.id].GRID_SIZE):
            if (state.agents[self.id].lines_number[j] == j+1):
                numRowsCompletedSucc += 1
                
        return numRowsCompletedSucc > numRowsCompleted
    
    def GetActions(self, state):
        return self.game_rule.getLegalActions(state, self.id)
    
    def heuristic(self, state):
        arrayOnFloor = state.agents[self.id].floor
        numOnFloor = 0
        for val in arrayOnFloor:
            if val == 1:
                numOnFloor += 1
        return -numOnFloor
    
    def SelectAction(self,actions,root_state):
        unique = count()
        start_time = time.time()
        myPQ = []
        node = (deepcopy(root_state), [])
        hValue = self.heuristic(root_state)
        heapq.heappush(myPQ, (hValue, next(unique),  node))
        ##myPQ = deque([node])
        closedStates = []
        while len(myPQ) and time.time()-start_time < THINKTIME:
            whole = heapq.heappop(myPQ)
            _,_, currNode = whole
            state, path = currNode
            newActions = self.GetActions(state)
            if (state not in closedStates):
                closedStates = closedStates + [state]
                for a in newActions:
                    next_path = path + [a]
                    next_state = deepcopy(state)
                    if(self.isGoal(next_state, a)):
                        return next_path[0]
                    else:
                        hValue = self.heuristic(root_state)
                        newNode = (next_state, next_path)
                        heapq.heappush(myPQ, (hValue, next(unique), newNode))
                        ##myPQ.append(newNode)
        return random.choice(actions)