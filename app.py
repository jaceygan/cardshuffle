from flask import Flask, render_template, request

app = Flask(__name__)

newDeckOrder = ['A♠', '2♠', '3♠', '4♠', '5♠', '6♠', '7♠', '8♠', '9♠', '10♠', 'J♠', 'Q♠', 'K♠',
        'A♦', '2♦', '3♦', '4♦', '5♦', '6♦', '7♦', '8♦', '9♦', '10♦', 'J♦', 'Q♦', 'K♦',
        'K♣', 'Q♣', 'J♣', '10♣', '9♣', '8♣', '7♣', '6♣', '5♣', '4♣', '3♣', '2♣', 'A♣',
        'K♥', 'Q♥', 'J♥', '10♥', '9♥', '8♥', '7♥', '6♥', '5♥', '4♥', '3♥', '2♥', 'A♥']

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
    return render_template("index.html", isNDO = (deck==newDeckOrder),displayDeck=str(deck)[1:-1].replace("'",''))

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
                output += str(deck)[1:-1].replace("'",'') + "<br><br>"
        else: #in faro
            if shuffleCount >52: 
                shuffleCount = shuffleCount % 52
                notes = "52 in-faros results in original deck order. Displaying the last " + str(shuffleCount) + " shuffles."
            for x in range(shuffleCount):
                output += "In Faro "+ str(x+1) + ":" + "<br>"
                deck = inFaro(deck)
                output += str(deck)[1:-1].replace("'",'') + "<br><br>"
        
        return render_template("deckOrder.html", shuffleCount=shuffleCount, shuffleType=shuffleType, output=output, notes=notes)

