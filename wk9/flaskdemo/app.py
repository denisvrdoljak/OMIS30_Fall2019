# import the Flask class from the flask module
from flask import Flask,request

deck = list()
hand  =list()
for suit in ['S','H','C','D']:
    for face in [str(f) for f in range(2,10)]+['X','J','Q','K','A']:
        deck.append(suit+face)

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "Hello World"

@app.route('/enterargs')
def game():
    #arg1=None):
    arg1 = request.args.get('arg1')
    return "Arg 1 is: {}".format(arg1)
    #use as (assuming port 5000is used for flask app)
    # http://127.0.0.1:5000/enterargs?arg1=messageabc123
    # examples here:
    # https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url

@app.route('/dealcard')
def dealcard():
    global hand
    global deck
    card = deck.pop()
    hand.append(card)
    cardsleft = len(deck)
    return "You were dealth a {}.\nThere are {} cards left in the deck.\n Your hand now contains: {}".format(card,cardsleft,hand)

@app.route('/showdeck')
def showdeck():
    global deck
    return str(deck)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
