from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

redD = u'/U+2666'

newDeckOrder = ["A♠", "2♠", "3♠", "4♠", "5♠", "6♠", "7♠", "8♠", "9♠", "10♠", "J♠", "Q♠", "K♠",
        "A♦️", "2♦️", "3♦️", "4♦️", "5♦️", "6♦️", "7♦️", "8♦️", "9♦️", "10♦️", "J♦️", "Q♦️", "K♦️",
        'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣', 'A♣',
        'K❤️', 'Q❤️', 'J❤️', '10❤️', '9❤️', '8❤️', '7❤️', '6❤️', '5❤️', '4❤️', '3❤️', '2❤️', 'A❤️']

def formatDeck(d):
    linesize = int((len(d))/4)
    start = 0
    end = linesize

    output = ""
    for x in range(1,5):
        end = linesize * x
        output += str(d[start:end])[1:-1]+",<br>"
        start = end

    output = output[:-5] # remove the last comma and line break
    return (output.replace("'",""))


def isNDO(d):
    return d==newDeckOrder

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

@app.route("/cardshuffle")
def cardshuffle():
    deck = newDeckOrder
    return render_template("index.html", isNDO = (deck==newDeckOrder),displayDeck=formatDeck(deck))


@app.route("/")
def index():
    return redirect(url_for("cardshuffle"))

@app.route("/deckOrder", methods=["POST"])
def deckOrder():
    shuffleType = request.form["shuffleType"]
    
    shuffleCount = request.form.get("shuffleCount")
    print(shuffleCount,shuffleType)
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
                if (isNDO(deck)): output+= "*New Deck Order*"+"<br>"
                output += formatDeck(deck) + "<br><br>"
        else: #in faro
            if shuffleCount >52: 
                shuffleCount = shuffleCount % 52
                notes = "52 in-faros results in original deck order. Displaying the last " + str(shuffleCount) + " shuffles."
            for x in range(shuffleCount):
                output += "In Faro "+ str(x+1) + ":" + "<br>"
                deck = inFaro(deck)
                if (isNDO(deck)): output+= "*New Deck Order*"+"<br>"
                output += formatDeck(deck) + "<br><br>"
        
        return render_template("deckOrder.html", shuffleCount=shuffleCount, shuffleType=shuffleType, output=output, notes=notes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)