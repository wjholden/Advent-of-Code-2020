with open('input.txt') as f:
    players = f.read().split('\n\n')
    p1 = [int(i) for i in players[0].split()[2:]]
    p2 = [int(i) for i in players[1].split()[2:]]

def round():
    global p1
    global p2
    #print("Player 1's deck:", p1)
    #print("Player 2's deck:", p2)
    m1 = p1.pop(0)
    m2 = p2.pop(0)
    #print('Player 1 plays:', m1)
    #print('Player 2 plays:', m2)
    if m1 > m2:
        #print('Player 1 wins the round!')
        p1.append(m1)
        p1.append(m2)
    else:
        #print('Player 2 wins the round!')
        p2.append(m2)
        p2.append(m1)
    # There is no intersection of p1 and p2.

def play():
    global p1
    global p2
    games = 0
    while len(p1) > 0 and len(p2) > 0:
        round()
        games += 1
    score = 0
    if len(p1) == 0:
        winner = p2
    else:
        winner = p1
    #print('== Post-game results ==')
    #print("Player 1's deck:", p1)
    #print("Player 2's deck:", p2)
    for i in range(len(winner)):
        #print('Winning players score +=', winner[i], '*', len(winner) - i)
        score += winner[i] * (len(winner) - i)
    return score

print('Part 1:', play())
