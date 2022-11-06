# Dynamic URL 
from flask import Flask, redirect, url_for

app = Flask(__name__)
@app.route('/')
def home():
    return "Hello all! Welcome to my Flask webpage."

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>RESULT </h1> <p>You passed and the score is " + str(score)+"</p>"

@app.route('/fail/<int:score>')
def fail(score):
    return "You failed and the score is...." + str(score)

@app.route('/results/<int:mark>')
def results(mark):
    result = ''
    if mark<50:
        result='fail'
    else:
        result='success'
    
    return redirect(url_for(result, score=mark))

if __name__=='__main__':
    app.run(debug=True)

