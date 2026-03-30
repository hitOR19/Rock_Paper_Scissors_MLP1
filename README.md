# Rock Paper Scissors AI Bot

## Overview

This project implements an intelligent Rock–Paper–Scissors agent in Python. The system analyzes opponent behavior using sequence pattern recognition and adaptive frequency-based strategies to make informed decisions.

The objective is to consistently outperform multiple predefined opponents by achieving a win rate of at least 60%.

## Key Features

* Sequence-based pattern recognition for opponent prediction
* Adaptive strategy using recent move frequency
* Deterministic decision-making for consistent performance
* Optimized to handle multiple opponent strategies

## Project Structure

rps-ai-bot/
│
├── RPS.py          # Core AI logic
├── RPS_game.py     # Game engine (provided)
├── main.py         # Testing script
├── README.md       # Documentation
└── .gitignore


## How It Works

The bot follows a hybrid decision model:

1. **Pattern Recognition**
   Identifies recurring sequences in opponent moves and predicts the next action.

2. **Recent Behavior Analysis**
   Uses a sliding window of recent moves to adapt to short-term strategy changes.

3. **Decision Optimization**
   Combines predictions and selects the most effective counter-move.

## How to Run

1. Clone the repository:

git clone https://github.com/your-username/rps-ai-bot.git
cd rps-ai-bot

2. Execute the program:

python main.py

## Performance Goal

The bot is designed to achieve:

* ≥ 60% win rate against all predefined opponents

## Technologies Used

* Python
* Algorithmic decision-making
* Pattern recognition techniques



Name : Rohit Chauhan
