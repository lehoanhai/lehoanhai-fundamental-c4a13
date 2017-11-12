# statuses = [
# """
#  |---------
#  |        |
#  |        0
#  |       -|-
# _|_      / \
# """,
# """
#  |---------
#  |        |
#  |        0
#  |       -|-
# _|_      /
# """,
# """
#  |---------
#  |        |
#  |        0
#  |       -|-
# _|_
# """,
# """
#  |---------
#  |        |
#  |        0
#  |       -|
# _|_
# """,
# """
#  |---------
#  |        |
#  |        0
#  |        |
# _|_
# """,
# """
#  |---------
#  |        |
#  |        0
#  |
# _|_
# """
# ]
words = ["gamer","random","evolution"]
import random
word = random.choice(words)
gword = list(word)
display_text = "_" * len(gword)
dt = list(display_text)
#
# for i in enumerate(gword):
#     print('_',end=" ")
# n = input('Guess? ')
# if n in gword:
#     print('Correct')
