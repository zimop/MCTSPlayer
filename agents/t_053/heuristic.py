# INFORMATION ------------------------------------------------------------------------------------------------------- #


# Purpose: Implements heuristic search agent for the COMP90054 competitive game environment.


# IMPORTS AND CONSTANTS ----------------------------------------------------------------------------------------------#


import time, random
from Azul.azul_model import AzulGameRule as GameRule
from copy import deepcopy
from agents.t_053 import priorityQueue
#from queue import PriorityQueue

THINKTIME   = 0.9
NUM_PLAYERS = 2


# FUNCTIONS ----------------------------------------------------------------------------------------------------------#


# Defines this agent.
class myAgent():
    def __init__(self, _id):
        self.id = _id # Agent needs to remember its own id.
        self.game_rule = GameRule(NUM_PLAYERS) # Agent stores an instance of GameRule, from which to obtain functions.
        # More advanced agents might find it useful to not be bound by the functions in GameRule, instead executing
        # their own custom functions under GetActions and DoAction.

    # Generates actions from this state.
    def GetActions(self, state):
        return self.game_rule.getLegalActions(state, self.id)
    
    # Carry out a given action on this state and return True if goal is reached received.
    def DoAction(self, state, action):
        score = state.agents[self.id].score
        state = self.game_rule.generateSuccessor(state, action, self.id)
        
       # Check if the next score is better than current score
        next_score = state.agents[self.id].score
        diff = next_score - score 
        if diff > 0:
            goal_reached = True
        else :
            goal_reached = False
        
        return goal_reached

    # Take a list of actions and an initial state, and perform breadth-first search within a time limit.
    # Return the first action that leads to goal, if any was found.
    # Error myAgent has no turnCount?
    def SelectAction(self, actions, rootstate):
        start_time = time.time()
        queue = priorityQueue.PriorityQueue()
        node = (deepcopy(rootstate), '', [])
        queue.push(node, 0)

        #base_heuristic = 0
        
        # Conduct simple heuristic starting from rootstate.
        while (not queue.isEmpty()) and time.time()-start_time < THINKTIME:
            #state, path = queue.popleft() # Pop the next node (state, path) in the queue.
            node = queue.pop()
            state, action, path = node
            new_actions = self.GetActions(state) # Obtain new actions available to the agent in this state.
            
            for a in new_actions: # Then, for each of these actions...
                next_state = deepcopy(state)              # Copy the state.
                next_path  = path + [a]                   # Add this action to the path.
                cost = self.Heuristic(next_state, a)

                goal     = self.DoAction(next_state, a) #cost - base_heuristic #self.DoAction(next_state, a) # Carry out this action on the state, and check for goal
                if goal:
                    #base_heuristic = goal
                    #print(f'Move {self.turn_count}, path found:', next_path) # In some cases, can cause error?
                    return next_path[0] # If the current action reached the goal, return the initial action that led there.
                else:
                    next_node = (next_state, a, next_path)
                    queue.push(next_node, cost) # Else, simply add this state and its path to the queue.
        
        if (not queue.isEmpty()):
        #    print(f'Move {self.turn_count}, path kinda found:', next_path)
            return next_path[0] # If the current action reached the goal, return the initial action that led there.
        return random.choice(actions) # If no goal was found in the time limit, return a random action.
    
    def Heuristic(self, state, action):

        if (action == ''):
            return 0

        ##state = self.game_rule.generateSuccessor(state, action, self.id) THIS CAUSE ERROR!!!!
        value = self.game_rule.calScore(state, self.id)
        ##value = state.agents[self.id].score
        value = -value

        return value
        
    
# END FILE -----------------------------------------------------------------------------------------------------------#