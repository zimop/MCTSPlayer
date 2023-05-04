from template import Agent, GameRule
import random
from queue import PriorityQueue
from Azul.azul_model import AzulGameRule as GameRule
from Azul.azul_model import AzulState as GameState


NUM_PLAYERS = 2

class myAgent(Agent):
    def __init__(self,_id):
        super().__init__(_id)
        self.game_rule = GameRule(NUM_PLAYERS)
        self.game_state = GameState(NUM_PLAYERS)
    
    def isGoal(state):
        return False
    
    def GetActions(self, state):
        return self.game_rule.getLegalActions(state, self.id)
    
    def SelectAction(self,actions,root_state):
        myPQ = PriorityQueue()
        hValue = self.game_state.ExecuteEndOfRound()
        node = (root_state, [])
        myPQ.put(root_state, hValue)
        closedStates = []
        while not myPQ.empty:
            node = myPQ.get()
            state, path = node
            actions = self.GetActions(state)
            for a in actions:
                next_path = path + [a]
                succState = self.game_rule.generateSuccessor(state, a, self.id)
                if(self.isGoal(succState)):
                    return next_path[0]
                else:
                    hValue = self.game_state.ExecuteEndOfRound()
                    new_node = (succState, next_path)
                    newNode = (new_node, hValue)
                    myPQ.put(newNode)
            
        return random.choice(actions)
