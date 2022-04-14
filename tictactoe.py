import os
os.system('cls' or 'clear')

class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'
import random
import datetime


def show_game_board():
    for i in range(3):
      for j in range(3):
        if game[i][j]=='x':
          print(game[i][j],end=' ')
        elif game[i][j]=='o':
          print(game[i][j] , end=' ')
        else:
          print(game[i][j] , end=' ')
        print( end=' ')
      print()

def exit_play():
    finish=datetime.datetime.now()
    start=datetime.datetime.now()
    time = finish - start
    print(int(time.total_seconds()*1000))
    exit()

def check():
  for i in range(3):
    if game[i][0]=='x' and game[i][1]=='x' and game[i][2]=='x':
      print( 'player 1 wins')
      exit_play()
    if game[i][0]=='o' and game[i][1]=='o' and game[i][2]=='o':
       print('player 2 win')
       exit_play()
  for j in range(3):
    if game[0][j]=='x' and game[1][j]=='x' and game[2][j]=='x':
       print('player 1 win')
       exit_play()
    if game[0][j]=='o' and game[1][j]=='o' and game[2][j]=='o':
       print('player 2 win')
       exit_play()
  if game[0][0]==game[1][1]==game[2][2]:
    if game[0][0]=='x':
       print('player 1 win')
       exit_play()
    if game[0][0]=='o':
       print('player 2 win')
       exit_play()
  if game[0][2]=='x' and game[1][1]=='x' and game[2][0]=='x':
       print('player 1 win')
       exit_play()
  if game[0][2]=='o' and game[1][1]=='o' and game[2][0]=='o':
       print('player2 win')
       exit_play()
  if rand == 9:
        print('no win')
        exit_play()



def check_player1():
  #player 1
  while True:
    print('player 1')
    row=int(input('row: '))#satr
    col=int(input('col: '))#soton

    #validation
    if 0<=row<=2 and 0<=col<=2:
      if game[row][col]=='_':
        game[row][col]='x'
        break
      else:
        print('this cell is not empty')
    else:
      print('invalid input,row and col must be between 0 and 2')
 

def check_player2():
  #player 2
  while True:
    print('player 2')
    row=int(input('row: '))
    col=int(input('col: '))

    if 0<=row<=2 and 0<=col<=2:
      if game[row][col]=='_':
        game[row][col]='o'
        break
      else:
        print('this cell is not empty')
    else:
      print('invalid input,row and col must be between 0 and 2')
    
   
def check_system():
  while True:
    row=random.randint(0,2)
    col=random.randint(0,2)
    if 0<= row <=2 and 0<= col <=2:
      if game[row][col]=='_':
        game[row][col]='o'
        break
      else:
        print('this cell is not empty')
    else:
      print('invalid input,row and col must be between 0 and 2')

game = [['_','_','_'],
        ['_','_','_'],
        ['_','_','_']]

show_game_board()

while True:
  print('choose:')
  print(color.RED+'1.player1 and player2')
  print(color.GREEN+'2.player1 and system')
  n=int(input(color.WHITE+ 'ure choose: '))
  rand=0
  if n==1:
    start=datetime.datetime.now()
    while True:
      print(color.RED+'player 1:')
      check_player1()
      rand+=1
      show_game_board()
      check()
      print(color.GREEN+'player 2:')
      check_player2()
      rand+=1
      show_game_board()
      check()
  if n==2:
    start=datetime.datetime.now()
    while True:
      print('player 1:')
      check_player1()
      rand+=1
      show_game_board()
      check()
      print('system:')
      check_system()
      rand+=1
      show_game_board()
      check()
      


