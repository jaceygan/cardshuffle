from flask import Flask, render_template, request, redirect, url_for
from cardshuffle import *

app = Flask(__name__)

@app.route("/")
def index():
    return redirect(url_for("cardshuffle"))

@app.route("/cardshuffle")
def cardshuffle():
    deck = newDeckOrder()
    return render_template("cardshuffle.html", isNDO = isNDO(deck),displayDeck=formatDeck(deck))

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

            if (shuffleType == "Out Faro"): #TODO: Refactor this monstrosity. move to cardshuffle.py
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