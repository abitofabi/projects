# Tic-Tac-Toe Reinforcement Learning Agent

## Project Overview

This project implements a Reinforcement Learning (RL) agent that learns to play Tic-Tac-Toe optimally using Q-learning. The agent learns by playing multiple games against itself, improving its strategy over time.

Tic-Tac-Toe is a classic 3x3 grid game where two players alternate placing their marks (X or O). The goal is to be the first to get three marks in a row horizontally, vertically, or diagonally.

## Features

- Q-learning based RL agent
- Epsilon-greedy policy for balancing exploration and exploitation
- Training loop with adjustable hyperparameters
- Interactive play mode to challenge the trained agent
- Clear state and action representations
## Usage
#### Training the Agent
 - Run the training script to train the RL agent:
```python
python train.py
```
This will run multiple episodes of self-play to allow the agent to learn an optimal policy.

laying Against the Agent
After training, play interactively against the trained agent:
```python
python play.py
```
Follow the prompts to make your moves and challenge the RL agent.

## Reinforcement Learning Details
 - Algorithm: Q-learning with epsilon-greedy policy
 - State Representation: Board states encoded as tuples/lists
 - Actions: Choosing an empty cell to place a mark
 - Rewards: +1 for winning, -1 for losing, 0 otherwise
 - Hyperparameters: Learning rate, discount factor, epsilon decay

## Results
The agent progressively learns to avoid losing and eventually achieves near-optimal play. 

## Possible Future Enhancements
 - Extend to Deep Q-Network (DQN) for larger state spaces
 - Add graphical user interface (GUI)
 - Experiment with other RL algorithms (SARSA, Monte Carlo methods)

*This project was completed as part of my PG Diploma in Machine Learning and AI program.*
