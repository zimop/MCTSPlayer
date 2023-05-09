# INFORMATION ------------------------------------------------------------------------------------------------------- #


# Purpose: Implement Blind Heuristic Search Algorithm
# Algorithm: A* algorithm


# IMPORTS AND CONSTANTS ----------------------------------------------------------------------------------------------#


import time, random
from Azul.azul_model import AzulGameRule as GameRule
from copy import deepcopy
from collections import deque
from queue import PriorityQueue
import utils
from template import Agent
import heapq


THINKTIME   = 0.9
NUM_PLAYERS = 2

# FUNCTIONS ----------------------------------------------------------------------------------------------------------#

class myAgent(Agent):
    def __init__(self,_id):
        super().__init__(_id)
        self.game_rule = GameRule(NUM_PLAYERS) # Agent stores an instance of GameRule, from which to obtain functions.
        
    # Generates actions from this state.
    def GetActions(self, state):
        return self.game_rule.getLegalActions(state, self.id)
    
    # Carry out a given action on this state and return True if goal is reached received.
    def DoAction(self, state, action):
        score = state.agents[self.id].score
        state = self.game_rule.generateSuccessor(state, action, self.id)
        
        # Check if whether it reached goal or not TODO:

        # Temporary make a self where it is in the next state
        temp_self = deepcopy(self)
        temp_state = deepcopy(state)
        temp_self.current_game_state = temp_state
        temp_self.current_agent_index = temp_self.getNextAgentIndex()
        temp_self.action_counter += 1

        # Check if a row is completed
        row_completed = temp_self.game_rule.gameEnds()
        goal_reached = row_completed
       
        return goal_reached
    
    # Take a list of actions and an initial state, and perform A* search within a time limit. TODO:
    # Return the first action that leads to goal, if any was found.
    def SelectAction(self, actions, rootstate):
        start_time = time.time()

        pqueue = PriorityQueue()
        startState = deepcopy(rootstate)
        startNode = (startState, '',0, [])
        pqueue.put((self.Heuristic(startState), startNode)) # Initialise priority queue. First node = root state and an empty path.

        visited = set()
        best_g = dict()
        
        # Conduct A* search starting from rootstate.
        while not pqueue.empty() and time.time()-start_time < THINKTIME:
            state, action, cost, path = pqueue.get() # Pop the next node (state, action, cost, path) in the priority queue with the best value.
            new_actions = self.GetActions(state) # Obtain new actions available to the agent in this state.

            # Clear priority queue to avoid illegal move
            pqueue.queue.clear()

            best_g[state] = cost
            
            for a in new_actions: # Then, for each of these actions...
                next_state = deepcopy(state)              # Copy the state.
                next_path  = path + [a]                   # Add this action to the path.
                next_action = a                           # Copy the action

                goal     = self.DoAction(next_state, a) # Carry out this action on the state, and check for goal
                if goal:
                    print(f'Move {self.turn_count}, path found:', next_path)
                    return next_path[0] # If the current action reached the goal, return the initial action that led there.
                else:
                    new_node = (next_state, next_action, cost, next_path) # New node for next search (cost change?)
                    pqueue.put((self.Heuristic(next_state)+cost, new_node)) # Else, simply add this state and its path to the queue.
        
        return random.choice(actions) # If no goal was found in the time limit, return a random action.
    
    def Heuristic(self, state):

        value = self.game_rule.calScore(state, self.id)
        
        # Highest value comes first
        value = -value

        return value
    
    


# END FILE -----------------------------------------------------------------------------------------------------------#