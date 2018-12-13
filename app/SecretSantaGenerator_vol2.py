import random


def get_input():

    return input('Hányan vesztek rész a sorsolásban? (Min. 2) ')


def raffle(player_list):
    print()
    print('Az eredmény: ')
    print('-----------------------------------------------')

    drawn = []
    for x in player_list:

        actual = player_list[random.randint(0, len(player_list)-1)]

        while actual == x or actual in drawn:
            actual = player_list[random.randint(0, len(player_list) - 1)]

        print(x, 'ajándékozza ----> ', actual)
        drawn.append(actual)


def get_names(num_of_members, players):
    for x in range(1, int(num_of_members) + 1):
        print()
        print(x, '. Játékos neve: ')
        current_player = input()
        players.append(current_player)


def get_players():
    players = []
    num_of_members = 0
    isnumeric = False

    while not isnumeric or int(num_of_members) <= 1:
        print('-------------------------------------')
        print('Kérlek 1-nél nagyobb számot adj meg!')
        print('-------------------------------------')

        num_of_members = get_input()
        isnumeric = num_of_members.isnumeric()
        print()

    get_names(num_of_members, players)

    return players


def run():
    players = get_players()
    raffle(players)

run()
