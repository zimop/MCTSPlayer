# INFORMATION ------------------------------------------------------------------------------------------------------- #


# Purpose: Implement Heuristic Search Algorithm


# IMPORTS AND CONSTANTS ----------------------------------------------------------------------------------------------#


import time, random
from Azul.azul_model import AzulGameRule as GameRule
from copy import deepcopy
from template import Agent
from copy import deepcopy
from agents.t_053 import priorityQueue


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

    # Take a list of actions and an initial state, and perform breadth-first search within a time limit.
    # Return the first action that leads to goal, if any was found.
    def SelectAction(self, actions, rootstate):
        start_time = time.time()
        queue = priorityQueue.PriorityQueue()
        node = (deepcopy(rootstate), [])
        queue.push(node, 0)

        base_heuristic = 0
        
        # Conduct simple heuristic starting from rootstate.
        while (not queue.isEmpty()) and time.time()-start_time < THINKTIME:

            node = queue.pop()
            state, path = node
            new_actions = self.GetActions(state) # Obtain new actions available to the agent in this state.
            
            for a in new_actions: # Then, for each of these actions...
                next_state = deepcopy(state)              # Copy the state.
                next_path  = path + [a]                   # Add this action to the path.
                cost = self.Heuristic(next_state)

                if (cost <= base_heuristic):
                    base_heuristic = cost
                    return next_path[0] # If the current action reached the goal, return the initial action that led there.
                else:
                    next_node = (next_state, next_path)
                    queue.push(next_node, cost) # Else, simply add this state and its path to the queue.
        
        if (not queue.isEmpty()):
            return next_path[0] # If the current action reached the goal, return the initial action that led there.
        return random.choice(actions) # If no goal was found in the time limit, return a random action.
    
    def Heuristic(self, state):

        value = state.agents[self.id].score
        value = -value

        return value
        
    
# END FILE -----------------------------------------------------------------------------------------------------------#