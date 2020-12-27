def handshake(subject, loopsize):
    value = 1
    for _ in range(loopsize): # _ is an ignored value. Neat!
        value = (value * subject) % 20201227
    return value

def pubkey(loopsize):
    return handshake(7, loopsize)

#print(pubkey(5764801))