from random import randint
from time import sleep

numero_sorte = randint(0, 10)
numero_usuario = -1
cont = 0

print('Olá, vou pensar em um número entre 0 a 10...')
sleep(1.0)

while numero_sorte != numero_usuario:
    numero_usuario = int(input('Qual número você acha que é? ').strip())
    cont += 1

    if numero_sorte > numero_usuario:
        print('\033[0;31mÉ maior... Tente novamente\033[m')

    elif numero_sorte < numero_usuario:
        print('\033[0;31mÉ menor... Tente novamente\033[m')

    elif numero_sorte == numero_usuario:
        print('\033[0;32mVocê venceu!')
        print('Precisou de {} tentativas. \033[m'.format(cont))
