# Analysis of the problem

Azul Board game has several characteristics as Game Theory :

1. Non-Deterministic : each new game is started with random tiles (stochastic) within a factory
2. Discrete : like any other board game, each move in Azul is discrete.
3. Sequential : players do not make decisions simultaneously, and earlier decisions affect the current one
4. Perfect Information: all players know the history of the game, and the previous moves.

From these characteristics, our group create three AI agents to compare to each other:
1. BFS (Greedy Best-First Search)
* This was chosen due to its simplicity in implementation and understanding
2. Value Iteration
* This was chosen due to its simple intuition and improved way of playing with reward states, where we could find out the best move that optimizes the number of points
3. Monte-Carlo Tree Search
* This was chosen due to its well known properties in playing games where rewards are clearly defined, and its ability to use less time to make a decision than value iteration.


To determine which AI agent performs better in Azul, we consider the following factors: computational resources available, time constraints, the complexity of the game, the accuracy of the game model, and the desired level of optimality. Each algorithm has its trade-offs, and thus we are implementing and comparing the three algorithm to each other to see which fulfill the most of the aforementioned criteria.