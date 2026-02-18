from random import randint
from time import sleep
itens=('rock', 'paper', 'scissors')
c=randint(0,2)
print('''your choices
[0] rock
[1] paper
[2] scissors''')
print('-='*15)
j=int(input('what is your choice ?'))
if 0<=j<=2:
    for i in range(1, 4):
        if i == 3:
            print("3!!!!")
            break
        print(i)
        sleep(1)
    print('computer: {}'.format(itens[c]))
    print('player: {}'.format(itens[j]))
    print('-='*15)
    if c == j:
        print('draw')
    elif c < j:
        print("You won!")
    elif c > j:
        print("You lose...")
else:
    print('its not valid')
