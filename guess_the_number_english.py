from random import randint
from time import sleep

num_bot = randint(0, 10)
num_usr = -1
count = 0

print('Hi! I will think in a number between 0 and 10...')
sleep(1.0)

while num_bot != num_usr:
    num_usr = int(input('Which number you think it is? ').strip())
    count += 1

    if num_bot > num_usr:
        print('\033[0;31mGreater... Try again\033[m')

    elif num_bot < num_usr:
        print('\033[0;31mSmaller... Try again\033[m')

    elif num_bot == num_usr:
        print('\033[0;32mYou won!')
        print('You needed {} attempts. \033[m'.format(count))
