# import the Flask class from the flask module
from flask import Flask,request

htmltemplate_DEALCARD = """
<html>
<body>
Card Dealt: {}\n
Number of Cards left in Deck: {}
<br>
Cards in Hand: {}
<br><br>
<a href="/dealcard">Deal another Card</a>
<br><br>
<a href="/showdeck">See Deck</a>
</body>
</html>
""".strip()

basic_html_SEEDECK = """
<html>

<body>
The deck contains:
<br>
{}
<br><br>
<a href="/dealcard">Deal another Card</a>
<br><br>
<a href="/showdeck">See Deck</a>
</body>
</html>
""".strip()

# the correct way to do this is with the jinja2 library, 
# but we'll just use strings and the .format() method 
# as a shortcut for this example

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
def enterargs():
    #use as (assuming port 5000is used for flask app)
    # http://127.0.0.1:5000/enterargs?arg1=messageabc123
    # examples here:
    # https://stackoverflow.com/questions/24892035/python-flask-how-to-get-parameters-from-a-url
    arg1 = request.args.get('arg1')
    return "Arg 1 is: {}".format(arg1)

@app.route('/deal')
def deal():

global deck
global hand
deck = list()
hand  =list()

for suit in ['S','H','C','D']:
    for face in [str(f) for f in range(2,10)]+['X','J','Q','K','A']:
        deck.append(suit+face)


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
    return basic_html_SEEDECK.format(deck)

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)
