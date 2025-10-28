import random
from logging import NullHandler

random_int = random.randint(0, 1)

#random_number = random.random()


if random_int == 0:
    print('Heads')
if random_int == 1:
   print('Tails')