import random


def get_input():

    return input('Hányan vesztek rész a sorsolásban? ')


def draw(player_list):
    for x in player_list:
        actual = players[random.randint(0, len(players)-1)]
        if actual != x:
            print(x, 'ajándékozza ----> ', players.remove(actual))
        else:
            x -= 1

num_of_members = 0
isnumeric = False

while not isnumeric or int(num_of_members) <= 0:
    print('-------------------------------------')
    print('Kérlek 0-nál nagyobb számot adj meg!')
    print('-------------------------------------')

    num_of_members = get_input()
    isnumeric = num_of_members.isnumeric()
    print()
    print()

players = []
print_players = []

for x in range(1, int(num_of_members) + 1):
    print()
    print(x, '. Játékos neve: ')
    current_player = input()
    players.append(current_player)
    print_players.append(current_player)

print()
print('Az eredmény: ')
print('-----------------------------------------------')

draw(players)

