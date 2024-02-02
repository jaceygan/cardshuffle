from flask import Flask, render_template, request, redirect, url_for
from cardshuffle import *
from koboupdates import *
import glob
import os
import datetime

app = Flask(__name__)

def getLastModDate():
    fileList=glob.glob("**/*") #get all files in current and sub directories 
    latestFile = max(lf, key=os.path.getmtime)
    timestamp = os.path.getmtime(latestFile)
    return str(datetime.datetime.fromtimestamp(timestamp))[:16]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/koboupdates", methods=["GET","POST"])
def koboupdates():
    if request.method == "GET":
        return render_template("koboupdates.html", addedmessage=False)
    else: #POST
        koboemail=request.form["koboemail"].strip()
        if (koboemail != "") and (subcribeToSNS(koboemail)):
            return render_template("koboupdates.html", addedmessage=True, koboemail=koboemail)
        else:
            return render_template("koboupdates.html", addedmessage=False)

@app.route("/cardshuffle",methods=["GET","POST"])
def cardshuffle():
    deck = newDeckOrder()

    if request.method == "GET":
        return render_template("cardshuffle.html", isNDO = isNDO(deck),displayDeck=formatDeck(deck))
    else: #POST

        shuffleType = request.form["shuffleType"]
        shuffleCount = request.form.get("shuffleCount")

        if (shuffleCount.isdigit()):
            print(shuffleCount,shuffleType)
            shuffleCount = int(shuffleCount)
            if shuffleCount > 0 :
                output = ""
                notes= ""

                if (shuffleType == "Out Faro"): #TODO: Refactor this monstrosity. move to cardshuffle.py
                    if shuffleCount > 8: 
                        shuffleCount = shuffleCount % 8
                        if shuffleCount == 0: 
                            shuffleCount = 8
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
        return render_template("cardshuffle.html", isNDO = isNDO(deck),displayDeck=formatDeck(deck)) #just return to original page if user provided rubbish

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)