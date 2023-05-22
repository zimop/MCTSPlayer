# AI Method 2 - Value Iteration Approach

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

There are several reasons we considered Value Iteration:
1. The intuition behind Value iteration is very simple to understand. All you need to do is calculate the average reward per state, even though it may take long
2. It would be a great starting point for seeing how well the Q function works, since it is simple to implement, and takes into account current and future rewards.
3. Q values will converge towards optimal values, which means we will be choosing the best path.
4. Since there actions are deterministic, (they have no probability of going to another state that is not the intended state), There will be less iterations to converge to optimal values, and a policy can be found by just picking the greatest reward state.

### Application  

For Value Iteration, we set the Gamma Value to be 0.9

We do this because we want to discount the future rewards. We value the current reward more than the future reward, but since it is 0.9, the future reward is still relatively important. We chose this value because the future reward is almost just as important as the current reward since the opponents moves' are very important to the how our agent performs. Also there are no probabilities, so there is no reason to believe that long-term solutions will be that much less optimal than the current solution. These are some different variations when playing against the MCTS algorithm

![gammaVVI](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/80197186/cc1b7c93-d387-439c-9a1c-9d3bb53fe916)

### Results

![Picture4](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/104483559/e1f93e58-fac4-489a-87c2-c736b6ab44c8)


In 100 games, Value Iteration always won against random algorithm, and won for 95% of the time against Greedy Best-First Search. But it only won 46% of the time against MCTS.
It also placed 30th after a couple thousand iterations in the preliminary competition.

### Trade-offs  
#### *Advantages*  
1. Value iteration is a reinforcement learning algorithm, it finds the policy or set of actions which gives the best cumulative reward. This is suited to the case given, as it is much easier to define a reward for every state, then to define a goal state to reach. We can easily define the rewards of a state as the score of the round, the bonus scores attained, or any other action you see as a reward, while determining a specific or set of goal states is more difficult to find.

2. Simple intuition for implementation. Value iteration is an algorithm with a simple goal, find the average reward for every state, where the average reward is the action which provides the maximum current + future rewards out of all available actions from that state. Once you populate this table, to find a policy is simple, as you just follow the maximum reward path from every state.


#### *Disadvantages*
1. Computationally expensive. While running our value iteration algorithm against the random agent, or any other agent, the time it takes to make a decision is very long, and occasionally runs into a timeout. It also needs to keep a dictionary of all the states in any decision that it makes (Q-TABLE), along with their average rewards from that state, which takes a lot of memory to maintain.

2. Selecting an appropriate gamma value. This is a difficult task, because you do not know which gamma value will produce the best outcome for you, unless you run it with all the different gamma values, and multiple times for each. Value iteration is a very slow algorithm, so testing for the best gamma value can be tedious.

[Back to top](#table-of-contents)

### Future improvements  
1. Decrease the threshold of the number of repeats of populating the Q-table. Since value iteration takes long to converge, we would rather run it for less iterations and produce a faster answer per decision. There is a trade off between making faster decisions, or waiting longer and then making a more accurate decision. But the time taken to make a more accurate decision seems to not be worth the risk of a potential timeout, facing a larger risk

2. More Testing of gamma values. Run the algorithm with different gamma values and see which one produces the best result. Even though it is tedious, it may be worth the effort to maximize the efficiency of the algorithm.

3. Inclusion of Opponent negative rewards: The moves that opponents make, affect the moves that we make. We need to take into account the reward of the consequence of an opponents move. A future improvement may be: the Q value of each state = average reward of player - average reward of opponent. This was attempted but no successful solution was found.

### Ideas Tried

1. Negative reward for opponent gains
2. include reward for filling the rows in order, from top to bottom, since this can lead to more optimal reward states by default. However we were not able to implement it in time.

[Back to top](#table-of-contents)