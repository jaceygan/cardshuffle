from flask import Flask, render_template, request

app = Flask(__name__)

redD = u'/U+2666'

newDeckOrder = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
        "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
        'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣', 'A♣',
        'K❤️', 'Q❤️', 'J❤️', '10❤️', '9❤️', '8❤️', '7❤️', '6❤️', '5❤️', '4❤️', '3❤️', '2❤️', 'A❤️']

def formatDeck(d):
    linesize = int((len(d))/4)

    output = str(d[:linesize])[1:-1]+",<br>"

    for x in range(3):
        output += str(d[linesize:linesize+13])[1:-1]+",<br>"
        linesize+=13

    output = output[:-5] # remove the last comma and line break
    return (output.replace("'",""))


def isNDO(d):
    return d==newDeckOrder()

def outFaro(d):
    if len(d) == 52 :
        p1 = d[:26]
        p2 = d[26:]

        newD = []

        for i in range(26):
            newD.append(p1[i])
            newD.append(p2[i])
        
        return newD

def inFaro(d):
    if len(d) ==52:
        p1 = d[:26]
        p2 = d[26:]

        newD = []

        for i in range(26):
            newD.append(p2[i])
            newD.append(p1[i])
        
        return newD





@app.route("/")
def index():
    deck = newDeckOrder
    return render_template("index.html", isNDO = (deck==newDeckOrder),displayDeck=formatDeck(deck))

@app.route("/deckOrder", methods=["POST"])
def deckOrder():
    shuffleType = request.form["shuffleType"]
    print(shuffleType)
    shuffleCount = request.form.get("shuffleCount")
    output = ""
    notes= ""
    if (shuffleCount):
        shuffleCount = int(shuffleCount)
        deck = newDeckOrder
        if (shuffleType == "Out Faro"):
            if shuffleCount > 8: 
                shuffleCount = shuffleCount % 8
                notes = "8 out-faros results in original deck order. Displaying the last "+ str(shuffleCount) + " shuffles."
            for x in range(shuffleCount):
                output += "Out Faro "+ str(x+1) + ":" + "<br>"
                deck = outFaro(deck)
                output += formatDeck(deck) + "<br><br>"
        else: #in faro
            if shuffleCount >52: 
                shuffleCount = shuffleCount % 52
                notes = "52 in-faros results in original deck order. Displaying the last " + str(shuffleCount) + " shuffles."
            for x in range(shuffleCount):
                output += "In Faro "+ str(x+1) + ":" + "<br>"
                deck = inFaro(deck)
                output += formatDeck(deck) + "<br><br>"
        
        return render_template("deckOrder.html", shuffleCount=shuffleCount, shuffleType=shuffleType, output=output, notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)