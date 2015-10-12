import random

playerNum = 0

def less_chairs():
    a = random.randint(0, playerNum)
    b = players[a]
    print('Bye, ' + b)
    players.remove(b)
    print('And the music plays. Who still has a chair?')
    for name in players:
        print(' ' + name)

print ('Welcome! A new game of musical chairs is starting.')

players = []
print('Enter the players or enter nothing to stop.):')
while True:
    name = input()
    playerNum += 1
    players = players + [name]
    if name == '':
        break
    
print('The player\'s names are:')
for name in players:
    print('  ' + name)

while playerNum >= 2:
    b = less_chairs()
    playerNum -= 1
    print('You are the winner.')
