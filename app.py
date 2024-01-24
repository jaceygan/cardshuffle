from flask import Flask, render_template

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

deck = newDeckOrder



@app.route("/")
def index():
    return render_template("index.html", isNDO = (deck==newDeckOrder),
        line1=str(deck[:13]), line2=str(deck[13:26]), line3=str(deck[26:39]), line4=str(deck[39:]))
