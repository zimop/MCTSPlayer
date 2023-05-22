# AI Method 3 - Monte-Carlo Tree Search

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

As a more complex extension of BFS, Monte-Carlo Search Tree (MCTS) has multiple reasons to be considered:
1. Azul Board Game is a board game with high complexity. MCTS has an asymmetric tree as it does not traverse all of state space, only the relevant parts. Thus, this is much more computationally efficient compared to algorithm such as minimax.
2. MCTS is an anytime algorithm. Meaning its returning the best possible estimation of optimal solution with limited time, which is useful due to the fact that an agent has limited thinking time.
3. Has sufficient history of being used as algorithm in other board games.
4. MCTS Simulation takes less time per decision than value iteration. Instead of doing multiple runs of the entire state space, we simulate monte carlo for every action.

### Application  

Gamma value  = 0.2
This is the discount value for the future rewards that we receive, after attempting multiple different gamma values, the value which produces the best results by far was the value of 0.2. It out performed all the other gamma values, which we incremented by 0.1 for each test. The tests were run against value iteration

![gamma](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/80197186/481e95f5-3f93-4aae-9946-b0454e006120)

We applied MCTS with simple approach, divided into 4 main parts: Selection, Expansion, Simulation, and Backpropagation.
1. Selection: The selection occurs by selecting the state that the Select Algorithm is given
2. Expansion: Expand this node, by going through all its legal actions, and exploring one of these actions. It explores the action by applying the current state, with the action in generateSuccessor, which will produce a new state
3. Simulation: We use a monte carlo simulation from this new state until it is the end of the round, or if there are no more tiles remaining. Then we add up all the accumulative rewards and return that reward to the original state. We simulate monte carlo by playing a game between the player and the opponent, and add up the rewards that you receive, and return it to the original state
4. Backpropagation: We unfortunately did not implement backpropagation, as we found it difficult to add to states that have previously been explored. Since there is no way of going back to the original state after you run generate successor besides creating a deepcopy. Creating this deepcopy of the state also does not work because the deepcopy of the state does not equal to the state itself, so there would be no way to compare for equality.

### Results
![winrate](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/80197186/2c2bab45-a330-4f8d-b932-0841b989f0ec)

400 games were ran against random algorithm, Greedy BFS, and Value Iteration. It always won against random, and has 95% win rate against Greedy BFS. and a 61% win rate vs value_iteration.

Solved Challenges:
1. Understanding how to implement the simulation. Initially we tried to simulate the game by only running the successors of our own player state, not moving the opponent. However this did not produce the most favorable result, and simulating with the opponent moves seemed to be the best possible solution.

2. Understanding the mutability of the state. Difficult to code initially because once the state has generated its successor, you cannot go back to the original state. However you can make deepcopys and preserve the original state.

3. Reward finding: Making the reward attached to every state, the score of the round and the end of score bonus points that you get.

### Trade-offs  
#### *Advantages*
  
1. As anytime algorithm, MCTS provides sufficiently more optimal solutions within limited time frames compared to other algorithms.
2. MCTS had the advantage that it is an online planning algorithm, meaning it does not need to reach every state, it only needs to plan for the states that we visit. This is especially good for this case, as value iteration is seen to take long, and even has timeouts. MCTS mitigates this problem, since it does not need to reach every state.
3. The tree builds up information that allows us to guide the early parts of our simulations, by only choosing the more likely actions that occur in the future.
4. Fairly simple intuition to understand this algorithm. They way we define the simulation, is to find the maximum reward you can receive through one iteration of the algorithm. Then find the action which has the maximum reward.
5. MCTS finds a solution much faster than value iteration, especially for this case, since you only need to extract the next best action from the root state (this is only the case because we decided to not use backpropagation)

#### *Disadvantages*

1. Can be difficult to implement the actual solution. The simulation includes simulating the opponents moves aswell, this can be a tricky task, taking into consideration which state should you start the opponent moves from, and dealing with mutable objects.
2. We may need to explore unfavourable actions, which wastes resources and time.
3. We defined the simulate moves function too simply. We run a simulation with the opponent, but we never take into consideration better moves to make so that the opponent will make a worse move. Instead we look to only maximize our own reward, without thinking about minimizing the opponents reward.

### Future improvements 
 
1. Try move ordering (alpha-beta pruning) as heuristic for simulation policy
2. Take into account how to minimize the opponents rewards as well.
3. Figure out a way to store the search tree so that no redundant nodes need to be re-searched.
4. Implement backpropagation in order to update the future rewards of a state

### Ideas tried:
1. Instead of populating a q table, we tried to use linear Q-function approximation, which worked, but did not perform better than the q table implementation. It was also quite hard to define the features that were important and the weights. We did eventually give it a try, but we were unsure how to evaluate our performance well.
