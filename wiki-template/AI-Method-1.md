# AI Method 1 - Greedy Best-First Search   

# Table of Contents
- [Governing Strategy Tree](#governing-strategy-tree)
  * [Motivation](#motivation)
  * [Application](#application)
  * [Solved challenges](#solved-challenges)
  * [Trade-offs](#trade-offs)     
     - [Advantages](#advantages)
     - [Disadvantages](#disadvantages)
  * [Future improvements](#future-improvements)

## Governing Strategy Tree  

### Motivation  
Greedy Best-First Search is chosen as one of the consideration for the AI is mainly due to
Simplicity: BFS is very intuitive and easy to understand and therefore is easy to implement
Efficiency: Efficient because it uses very little memory, as it doesnt need to keep information on previous states, only the path to the goal state.
Speed: Fast since state action evaluation is simple and quick.

### Application  

In our implementation of Greedy Best-First Search for Azul Board Game, we use a simple heuristic method which count how many tiles are on the floor within a state. A state in this algorithm refers to positions and numbers of tiles within player's grid. The BFS prioritizes to the state with the lowest heuristic value in the priority queue. The goal state of the Greedy BFS algorithm is when the next state produces more number of completed rows.

### Solved Challenges

One challenge that we faced, was learning how the azul model worked. We figured out that there are certain functions which permanently change the state of the variables. Before knowing this, we ran into a lot of bugs trying to fix assertion errors, but finally we were able to get our  algorithm working

Another challenge was figuring out the goal state. Since we do not know the specific range of points that will beat the opponent, it is pretty difficult to figure out the goal state. We had to figure out a strategy for getting more points, by defining a relevant goal state. We finally did find a goal state, where we fill up the rows of the grid from top to bottom. If the next row > current row, then a goal state is reached. This must be true for every state to reach a goal, so in the end, it fills up the grid row by row.

### Results

![Picture2](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/104483559/ec83d624-2657-4b5f-92f7-22792afff466)

We measured BFS in 100 games against random algorithm, value iteration, and Monte-Carlo Search Tree (MCTS) algorithm. Within the 100 games, Greedy BFS always won against random, but only barely won 5% of the time against Value-Iteration. It does slightly better against MCTS with 13% win rate.

### Trade-offs  
#### *Advantages*  
1. Simple and Easy to Implement: BFS by nature is easy and straightforward to implement compared to other algorithms. 
2. Fast and Efficient: the greatest advantage of BFS over any other AI agent is that it is a fast algorithm. It is essential for Azul due to limited time to think.

#### *Disadvantages*

1. Not Optimal: BFS does not consider all the game data, and does not always take the optimal path. Compared to more complex algorithm, Greedy BFS is completely outmatched.
2. Heuristic function and goal state definition: The Heuristic function is something that we have to define ourselves which is difficult due to there being no clear definition of being closer to beating an opponent without knowing the opponents moves. We have a similar issue when trying to define a goal state for the problem.
3. Although it seemed to do well against the random agent, it performed very poorly against value iteration. This is because our implementation only considers the heuristic and goal state when choosing actions. It does not take into account the rewards that it could receive in every state, instead it plays according to reach our goal state which is completing more rows than the previous state. There is no explicit searching for maximum point attainment.

### Future improvements  

1. In the future iteration, a combination of MCTS and Greedy Best-First Search would help with finding the BFS optimal path.
2. Heuristic function can be the negative rewards that you get for reaching a state. We ended up not trying this idea, since it might've changed the way the goal state is reached, so we decided not to take the risk.
3. Include the opponents moves so that we can define a heuristic more appropriately, and define the goal state in terms of beating the opponent instead of attaining a higher number of points.