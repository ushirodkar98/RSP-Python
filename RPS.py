"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

import random

import time

#  Available game moves for users to choose from

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def __init__(self):
        self.moves = ['rock', 'paper', 'scissors']
        self.my_action = random.choice(moves)
        self.their_action = None
        self.current_move = 0
    def learn(self, my_action, their_action):
        self.my_action = my_action
        self.their_action = their_action
class randomPlayer(Player):
    def move(self):
        return random.choice(moves)
class reflectPlayer(Player):
    def move(self):
        return self.their_action
class cyclePlayer(Player):
    def move(self):
        if self.my_action == self.moves[0]:
            return self.moves[1]
        elif self.my_action == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]
class cyclePlayer(Player):
    def move(self):
        if self.current_move == len(moves):
            self.current_move = 0
        return moves[self.current_move]
class humanPlayer(Player):
    def move(self):
        while True:
            response = input("Rock, paper, scissors? > ").lower()
            if response.lower() in self.moves:
                return response.lower()
            elif response.lower() == "quit":
                exit()
            else:
                print("Please enter a valid move.")
class valid_input(Player):
    def move(self):
        while True:
            response = input("Rock, paper, scissors? > ").lower()
            if response.lower() in self.moves:
                return response.lower()
            elif response.lower() == "quit":
                exit()
            else:
                print("Please enter a valid move.")
class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score_p1 = 0
        self.score_p2 = 0
    def beats(self, one, two):
        return ((one == 'rock' and two == 'scissors') or
                (one == 'scissors' and two == 'paper') or
                (one == 'paper' and two == 'rock'))
    def rounds(self):
        while True:
            self.num_rounds = input("How many rounds would you like to play? >")
            if self.num_rounds.isdigit():
                return int(self.num_rounds)
            elif self.num_rounds.lower() == "quit":
                exit()
            elif self.num_rounds.lower() != "quit":
                print("Please enter a number.")
            else:
                return "Please enter a number."
    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        if self.beats(move1, move2):
            self.score_p1 += 1
            print("Player 1 wins!")
        elif self.beats(move2, move1):
            self.score_p2 += 1
            print("Player 2 wins!")
        else:
            print("Tie!")
        print(f"Score: Player 1: {self.score_p1} Player 2: {self.score_p2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
    def play_game(self):
        print("Game start!")
        self.rounds()
        for round in range(int(self.num_rounds)):
            print(f"Round {round + 1}:")
            self.play_round()
        if self.score_p1 == self.score_p2:
            return "It's a tie!"
        elif self.score_p1 > self.score_p2:
            return "Player 1 wins!"
        elif self.score_p1 < self.score_p2:
            return "Player 2 wins!"
        else:
            return "Game over!"
if __name__ == '__main__':
    game = Game(humanPlayer(), random.choice([randomPlayer(), reflectPlayer(), cyclePlayer()]))
    game.play_game()
