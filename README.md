# Spam Detection Bot: 

Welcome to the my first-ever ML project Spamie - Spam Detection Bot! This bot is designed to automatically detect and remove spam messages in group chats or respond to text messages to determine whether they are spam or not.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Dataset](#dataset)
- [Installation](#installation)
- [Usage](#usage)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project aims to create a Telegram bot that can detect spam messages using a machine learning model. The bot can be added to group chats where it will automatically delete spam messages, or users can interact with the bot directly to check if a message is spam.

## Features

- **Automatic Spam Detection**: The bot can automatically delete spam messages in group chats.
- **User Interaction**: Users can send a message to the bot to check if it's spam or not.
- **Machine Learning Model**: Uses a Multinomial Naive classifier to detect spam, trained on a dataset of labeled messages.

## Dataset

The model was trained using the [SMS Spam Collection dataset](http://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection) from the UCI Machine Learning Repository.

**Citation:**
Almeida, T. A., Hidalgo, J. M. G., & Yamakami, A. (2011). SMS Spam Collection v.1 [Data set]. UCI Machine Learning Repository. http://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection

## Installation

To get started with the project, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spam-detection-bot.git
   cd spam-detection-bot
2. Create a virtual environment and install dependencies:
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
3. Obtain a Telegram bot token by creating a new bot with BotFather and set it in the main.py file.
4. Run the botbot
   python main.py

## Usage Demo of Spamie

## Model Training
The model is trained using a dataset of labeled spam and ham messages. The training script (train_model.py) uses techniques like SMOTE to handle class imbalance and vectorization to convert text into features suitable for machine learning.
