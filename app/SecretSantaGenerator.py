import random


def randomize():
    cup = ["Jani", "Máté", "Krisz"]

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
    print("\nSECRET SANTA GENERATOR:\n")
    print(p1, "paraszt", g1, "parasztot, és kedvesét húzta\n")
    print(p2, "paraszt", g2, "parasztot, és kedvesét húzta\n")
    print(p3, "paraszt", g3, "parasztot, és kedvesét húzta\n")

    if g1 == "Krisz":
        print("Aztán fasza ajándék legyen", p1, "\n")
    elif g2 == "Krisz":
        print("Aztán fasza ajándék legyen", p2, "\n")
    elif g3 == "Krisz":
        print("Aztán fasza ajándék legyen", p3, "\n")

    print("BOLDOG KARÁCSONYT!")


randomize()
