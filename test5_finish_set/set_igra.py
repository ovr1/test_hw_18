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
        if card[3] not in namber_sh:
            namber_c.append(card[3])
    print(namber_n)
    print(namber_s)
    print(namber_sh)
    print(namber_c)
    if (len(namber_n) or len(namber_s) or len(namber_sh) or len(namber_c)) == 1 \
            or (len(namber_n)==3 and len(namber_s)==3 and len(namber_sh)==3 and len(namber_c) == 3):
        return True
    else:
        return False



cards = [['2', 'OVAL', 'OPEN', 'RED'], ['3', 'SQUIGGLE', 'OPEN', 'PURPLE'], ['3', 'OVAL', 'STRIPPED', 'RED']]
print(check_set(cards))