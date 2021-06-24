rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper


paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

import random

A = 0
B = 0
i = 1


# rules

# r v s = r wins   1 v 3  1
# s v p = s wins   3 v 2  3
# p v r = p wins   2 v 1  2


def inputs():
    t = ['rock', 'paper', 'scissors']
    h = int(input())
    c = random.randint(1, 2)
    return t[h - 1], t[int(c)]


def function(val):
    if val == 'rock':
        print(rock)
    elif val == 'paper':
        print(paper)
    elif val == 'scissors':
        print(scissors)


while True:

    print("GAME ", i - 1)
    print('''
Enter 1 -- ROCK
Enter 2 --- paper
Enter 3 --- scissor
    ''')
    h, c = inputs()

    if h == 'rock' and c == 'scissors':
        A = A + 1
    elif h == 'scissors' and c == 'paper':
        A = A + 1
    elif h == 'paper' and c == 'rock':
        A = A + 1

    elif h == c:
        A = A
        B = B
    else:
        B = B + 1

    function(h)
    function(c)
    print([A, B])
    print('--' * 40)

    print("""


  """
          )

    i = i + 1

    if int(A) == 3:
        print("human wins")
        break
    elif int(B) == 3:
        print("Computer wins")
        break