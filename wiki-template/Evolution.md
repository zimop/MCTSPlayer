# Evolution of the approach

You can include screenshots of precompetition results and animated gifs, to showcase the evolution of your agents.

## My First Agent - Value Iteration
----
The first agent was created and tested multiple times on our local machines, before we submitted it. It had quite a lot of bugs and exceptions including "None exception, assertion exception and key errors" They were all dealt with through making deepcopies. the first implementation only took into account the score of the round, but the 2nd implementation took into account the bonus scores as well, which gave us a lot more points.

The first agent that we submitted for the tournament is the Value iteration algorithm. We expected it to do quite well since it was a reinforcement learning algorithm, which is known to do well in tasks like these. It performed decently well, with an ELO score of 11191. It won more than a majority of the matches but was placing somewhere around the 30th position, which we thought we could do a lot better than. We had our criticisms that value iteration is more likely to timeout, so there may be games where it is taking huge losses due to this fact.

Our value iteration algorithm strategy was to attain the highest expected reward states, so there are a small number of floor tiles, and large number of consecutive tiles: In this video our value iteration is agent 1 and MCTS is agent 0

![Untitled](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/80197186/4d894e03-2410-44f9-8299-7ce8856e128c)


#### Competition results: Position - 31/101 

![Screenshot 2023-05-19 153435](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/104483559/83a832d5-495e-4617-a712-210610d3e4d6)

The first agent that we submitted for the tournament is the Value iteration algorithm. We expected it to do quite well since it was a reinforcement learning algorithm, which is known to do well in tasks like these. It performed decently well, with an ELO score of 11191. It won more than a majority of the matches. But it was still early in the competition so we did not get our hopes up. We also had our criticisms that value iteration is more likely to timeout, so there may be games where it is taking huge losses due to this fact.

After a while as more agents started coming in, our elo score started to drop significantly, and it was taking too long to play the games, and we ended up placing in the 40th or so spot. We decided that we needed a better algorithm to play against the staff teams.

----
## My Second Agent - Monte-Carlo Search Tree (last submission)
----

During our extensive testing of MCTS (Monte-Carlo Tree Search), we have discovered that this algorithm presents a higher level of complexity compared to our previous approaches. As a result, we have encountered several challenges and bugs along the way. In addition to resolving these issues, we need to make informed decisions regarding the selection, simulation policy, and reward components of MCTS.

Initially, during the tournament, our algorithm's performance seemed to align with that of the Value Iteration approach, securing rank around 30th place. However, as time progressed, we noticed a decline in its ranking, eventually settling around the 40th position. This is when we tried the linear q-approximation approach.

This is its performance against value iteration: Where agent 1 is the mcts approximation algorithm

<img width="486" alt="Screenshot 2023-05-22 at 12 25 34 PM" src="https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/128003981/b26a524c-eb4b-429c-8120-429f8f3063a7">

![val it v mcts](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/80197186/e4515aa5-ed0d-49ca-9ee8-807f822af48c)

it ended up with an elo score of 10480 in the competition, but we still believed it performed better than val iteration even though it had a lower elo score. This lower ELO score could be due to the decreasing function, as more games are played, everyones elo scores start decreasing.

We ended up improving our MCTS algorithm, by just using normal Q function finding. We found the optimal gamma value is 0.2 through testing. And we found out that it does perform better than our other MCTS algorithm. It beats value iteration by a much larger margin, and beats the Linear Approximation Q learning MCTS majority of the time. 

![Screenshot 2023-05-21 131414](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/80197186/9162e8eb-6b32-46cf-9420-36bba087e214)

![lplpl](https://github.com/COMP90054-2023S1/assignment3-azul--team_53/assets/80197186/bff002d5-fff3-4d13-adeb-d48c0a67c5d5)

This was our final submission agent, which does present a lower elo score, but through  time we do believe it will increase its elo score by alot more

## My Third Agent - Greedy Best first search (not submitted for pre-competition)
----

We did not submit our greedy best first search algorithm to the competition mainly cause we believe that it is quite inferior to any other planning algorithm that we could come up with. The way we tested it was to play it against the random player and see how much it wins by on average to measure if there are improvements.
