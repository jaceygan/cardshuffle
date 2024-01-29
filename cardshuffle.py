def newDeckOrder():
    return ["A♠️", "2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️",
            "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
            'K♣️', 'Q♣️', 'J♣️', '10♣️', '9♣️', '8♣️', '7♣️', '6♣️', '5♣️', '4♣️', '3♣️', '2♣️', 'A♣️',
            'K♥️', 'Q♥️', 'J♥️', '10♥️', '9♥️', '8♥️', '7♥️', '6♥️', '5♥️', '4♥️', '3♥️', '2♥️', 'A♥️']

def formatDeck(d):
    linesize = int((len(d))/4)
    start = 0
    
    output = ""
    for x in range(1,5):
        output += str(d[start:start+linesize])[1:-1]+",<br>"
        start +=linesize

    output = output[:-5] # remove the last comma and line break
    return (output.replace("'",""))

def isNDO(d):
    return d==newDeckOrder

def faroShuffle(d, type="in"):
    half = int(len(d)/2) #TODO: need to handle odd numbers
    p1 = d[:half]
    p2 = d[half:]
    newD = []

    if (type == "out"):
        for i in range(half):
            newD.append(p1[i])
            newD.append(p2[i])
    else: #in faro
        for i in range(half):
            newD.append(p2[i])
            newD.append(p1[i])
    return newD