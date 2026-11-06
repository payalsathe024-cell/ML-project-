import flask
from flask import Flask
app = Flask(__name__)
@app.route('/')
def greet():
    return "Hello , welcome to Flask"
@app.route('/addition',)
def addition():
    A=10
    B=20
    return A+B
if __name__ == "__main__":
   app.run(debug=True)