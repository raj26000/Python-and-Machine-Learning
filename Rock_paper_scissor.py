from time import sleep
import random

class Rock_Paper_Scissors:
  def __init__(self, score=0):
    self.score = score

  def Greeting(self):
    print('Hello! Get Ready to play...\n')
    print('Rules: +5 for win, -3 for loss, 0 for tie.')

  def user_input(self):
    turn = input('Play your turn: ')
    return turn
  
  def computer_move(self):
    moves = ['Rock', 'Paper', 'Scissor']
    return random.choice(moves)

  def update_score(self, round_score):
    self.score = self.score + round_score
    print('Your current score: ', self.score)

  def result(self, user_move, comp_move):
    if user_move == comp_move:
      print("That's a tie!")
      self.update_score(0)
    elif (user_move=='rock' and comp_move=='paper') or (user_move=='paper' and comp_move=='scissor') or (user_move=='scissor' and comp_move=='rock'):
      print('Computer Won. Better Luck Next time :(')
      self.update_score(-3)
    elif (user_move=='paper' and comp_move=='rock') or (user_move=='rock' and comp_move=='scissor') or (user_move=='scissor' and comp_move=='paper'):
      print('Yay you won! GG :)')
      self.update_score(5)
    
  def play_sequence(self):
    self.Greeting()
    print('Playing in 3:')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    sleep(1)
    user_move = self.user_input().lower()
    comp_move = self.computer_move().lower()
    print("Your Move:", user_move)
    sleep(1)
    print("Computer Move:", comp_move)
    sleep(3)
    print('\n')
    self.result(user_move, comp_move)
    new_game = input("Do you want to continue playing? [yes/no]")
    if new_game.lower() == 'yes':
      print("------------------------------") 
      self.play_sequence()
    else:
      print("Okay, goodbye :)")

game1 = Rock_Paper_Scissors()
game1.play_sequence()
