from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello World"


@app.route('/test')
def testendpoint():
    return """<html><body>Player has: KH, AS
    <br><br>
    dealer has: 2H, 3H</body></html>
    <br><br>
    PLAYER WINS!
    """

if __name__ == '__main__':
    app.run(debug=True)
