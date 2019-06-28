import random

numbers = ['1', '2', '3']
symbols = ["DIAMOND", "SQUIGGLE", "OVAL"]
shadings = ["STRIPPED", "SOLID", "OPEN"]
colors = ["RED", "GREEN", "PURPLE"]

y = []
n = 0
while n <3:
    n += 1

    a = []
    i = 0
    while i < 1:
        i += 1

        index1 = random.randrange(0,len(numbers))
        number = str(numbers[index1])
        a.append(number)

        index2 = random.randrange(0, len(symbols))
        symbol = str(symbols[index2])
        a.append(symbol)

        index3 = random.randrange(0, len(shadings))
        shading = str(shadings[index3])
        a.append(shading)

        index4 = random.randrange(0, len(colors))
        color = str(colors[index4])
        a.append(color)

    y.append(a)
cards = y

namber_n = []
namber_s = []
namber_sh =[]
namber_c = []

def check_set(cards):
    for card in cards:
        if card[0] not in namber_n:
            namber_n.append(card[0])
        if card[1] not in namber_s:
            namber_s.append(card[1])
        if card[2] not in namber_sh:
            namber_sh.append(card[2])
        if card[3] not in namber_c:
            namber_c.append(card[3])
    if (len(namber_n)==1 or len(namber_s)==1 or len(namber_sh)==1 or len(namber_c) == 1) \
            or (len(namber_n)==3 and len(namber_s)==3 and len(namber_sh)==3 and len(namber_c) == 3):
        return True
    else:
        return False

print(check_set(cards))
