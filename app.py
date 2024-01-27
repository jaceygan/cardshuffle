from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

newDeckOrder = ["A♠️", "2♠️", "3♠️", "4♠️", "5♠️", "6♠️", "7♠️", "8♠️", "9♠️", "10♠️", "J♠️", "Q♠️", "K♠️",
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

    if (shuffleCount.isdigit()):
        print(shuffleCount,shuffleType)
        shuffleCount = int(shuffleCount)
        if shuffleCount > 0 :
            output = ""
            notes= ""
            
            deck = newDeckOrder
            if (shuffleType == "Out Faro"):
                if shuffleCount > 8: 
                    shuffleCount = shuffleCount % 8
                    notes = "8 out faros results in original deck order. Displaying the last "+ str(shuffleCount) + " shuffles."
                for x in range(shuffleCount):
                    output += "Out Faro "+ str(x+1) + ":" + "<br>"
                    deck = faroShuffle(deck, "out")
                    if (isNDO(deck)): output+= "*New Deck Order*"+"<br>"
                    output += formatDeck(deck) + "<br><br>"
            else: #in faro
                if shuffleCount >52: 
                    shuffleCount = shuffleCount % 52
                    notes = "52 in faros results in original deck order. Displaying the last " + str(shuffleCount) + " shuffles."
                for x in range(shuffleCount):
                    output += "In Faro "+ str(x+1) + ":" + "<br>"
                    deck = faroShuffle(deck, "in")
                    if (isNDO(deck)): output+= "*New Deck Order*"+"<br>"
                    output += formatDeck(deck) + "<br><br>"
            
            return render_template("deckOrder.html", shuffleCount=shuffleCount, shuffleType=shuffleType, output=output, notes=notes)
    
    return redirect(url_for("cardshuffle")) #just return to original page if user provided rubbish

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)