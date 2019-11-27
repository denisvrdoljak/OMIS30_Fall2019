from flask import Flask,request

from html_templates import calc_splashHTML, calc1HTML, calc1resultHTML

from html_templates import htmltemplate_DEALCARD, basic_html_SEEDECK, blackjack_homeHTML,htmltemplate_DEALCARD,basic_html_SEEDECK

from html_templates import homeHTML


app = Flask(__name__)
deck = list()
hand  =list()

@app.route('/')
def homepage():
    return homeHTML



@app.route('/calc_home')
def calculator_landing_page():
    return calc_splashHTML

@app.route('/calc1')
def calc1():
    return calc1HTML

@app.route('/calc1result')
def calc1result():
    lastname = request.args.get('lastname')
    firstname = request.args.get('firstname')
    return calc1resultHTML.format(firstname_field=firstname,lastname_field=lastname)



@app.route('/blackjack_home')
def blackjack_home():
    return blackjack_homeHTML

@app.route('/deal')
def deal():

    global deck
    global hand
    deck = list()
    hand  =list()

    for suit in ['S','H','C','D']:
        for face in [str(f) for f in range(2,10)]+['X','J','Q','K','A']:
            deck.append(suit+face)

    card = deck.pop()
    hand.append(card)
    cardsleft = len(deck)
    return htmltemplate_DEALCARD.format(card,cardsleft,hand)
    #return "You were dealth a {}.\nThere are {} cards left in the deck.\n Your hand now contains: {}".format(card,cardsleft,hand)



@app.route('/hit')
def hit():
        global hand
        global deck

        card = deck.pop()
        hand.append(card)
        cardsleft = len(deck)
        return htmltemplate_DEALCARD.format(card,cardsleft,hand)

@app.route('/stand')
def stand():
    global deck
    global hand
    return basic_html_SEEDECK.format(deck)




# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
