# Othello-AI
An AI system that is capable of playing the board game of Othello

Q-Learning is a kind of unsupervised learning algorithm. It makes use of a Q-Table. The Q-Table consists of all the possible state spaces for the player and maps different actions to each and every state in the table. The table is initially set to 0 and then as the machine goes through a set of training data, it begins to update this table with new Q-values that are a reflection of the current state that the machine is in, and also adding in a factor of future rewards.

The future reward is essential for the AI system to learn how to maximize rewards. The absence of future rewards would mean that the AI system only wants to know how to maximize the current reward, even if there is a chance that it may lead to bigger penalties in the near future. The system also cannot be expected to always hold out for a future reward, as this would hamper its ability to get to a point where it can compete for the best reward.

The Q-Learning with a Q-Table is a method that is used when there is a finite number of state spaces and these states are easily definable. In the case of Othello, the state space (10^28) is too big to be defined in a table as state-->action. In such situations where the state space cannot be defined, a different method known as Deep Q-Networks are used. These are artificial neural networks that are used as function approximators to evaluate the equation in Fig. 2 and thereby get the updated Q-values. Since Othello is a two player game and the next state or action of the player depends on the opponent, a different approach has been taken towards this problem. From extensive research and gameplay, it can be understood that certain positions on the game board have some positional advantage and that it is better to occupy these positions, whereas, other positions may have disadvantages similarly. In this attempt, the game board of Othello is being considered as the Q-Table and the values updated in the table correspond to the Q-value for playing a stone in that specific square. In such a game where the next state belongs to the opponent, it is difficult to calculate a future reward. To overcome this barrier, the Q-value of the previous state is being updated with the discounted value of the total rewards received in the current state. In this way, the next time the AI comes to the same state, it will have a better understanding of the game situation.

Once the AI system was developed, it was first tested against its own AI system for 20000 episodes. During this time, both the players kept their own Q-Tables. After 20000 episodes, it was found that 779 games ended in a tie. Black won 9603 games and White won 9618 games. The Q-Table that the AI had accumulated was then loaded back into the program and was trained against a random AI player for 10000 episodes. After 10000 episodes, it was found that 389 games ended in a tie. Black won 4284 game and White won 5327 games. Here Black was the random AI. It is seen that the AI system can perform better than a random player. The Q-Table that the AI had accumulated was then loaded back into the program and was trained against an AI using Minimax algorithm for 10000 episodes. After 10000 episodes, it was found that 278 games ended in a tie. Black won 6767 games where as White only won 2955 games. This shows that the AI was not good enough to beat a Minimax algorithm with the amount of training it has gotten. Through more training, the AI can have a better Q-Table to refer to and eventually become better at the game.