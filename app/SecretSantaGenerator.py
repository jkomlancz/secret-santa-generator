import random
import os
import time

def number_player():
    os.system("clear")
    try:
        player_num = int(input("How many player wanna play? (Max 3)"))
    except ValueError:
        print("Szamot adjal meg teso")
        time.sleep(2)
        number_player()

    cup = []
    for i in range(player_num):
        os.system("clear")
        print(" Write the name of player No.", i+1)
        name = input()
        cup.append(name)

    if len(cup) == 1:
        print("vicces vagy :D")

    if len(cup) == 2:
        print("vicces vagy, egymast huztatok :D")

    if len(cup) > 3:
        print("Max 3 vaksikam")
        names_input()
    
    if len(cup) == 3:
        
        p1 = random.choice(cup)
        p2 = random.choice(cup)
        p3 = random.choice(cup)

        while p1 == p2 or p2 == p3 or p1 == p3:
            p1 = random.choice(cup)
            p2 = random.choice(cup)
            p3 = random.choice(cup)

        g1 = random.choice(cup)
        g2 = random.choice(cup)
        g3 = random.choice(cup)

        while g1 == g2 or g1 == g3 or g2 == g3 or p1 == g1 or p2 == g2 or p3 == g3:
            g1 = random.choice(cup)
            g2 = random.choice(cup)
            g3 = random.choice(cup)
        os.system("clear")
        print("\nSECRET SANTA GENERATOR:\n")
        print(p1, "paros", g1, "parost huzta\n")
        print(p2, "paros", g2, "parost huzta\n")
        print(p3, "paros", g3, "parost huzta\n")

        if g1 == "Krisz":
            print("Aztan fasza ajandek legyen", p1, "\n")
        elif g2 == "Krisz":
            print("Aztan fasza ajandek legyen", p2, "\n")
        elif g3 == "Krisz":
            print("Aztan fasza ajandek legyen", p3, "\n")

        print("BOLDOG KARACSONYT!")


def main():
    number_player()


if __name__ == "__main__":
    main()
