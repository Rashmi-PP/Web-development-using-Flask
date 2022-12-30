# Dynamic URL 
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Render home page using index.html for inputting the scores of various subjects
@app.route('/')
def home():
    return render_template('index.html')

# Same as above with explicit /home in the URL
@app.route('/home')
def homepage():
    return render_template('index.html')

# Check result status (Pass/Fail) and render results.html page
@app.route('/success/<float:score>')
def success(score):
    res = ''
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
        return redirect(url_for(res, score=score))
    
    return render_template('results.html', result=[res, score])

# Page for fail scenario
@app.route('/FAIL/<float:score>')
def fail(score):
    return render_template('results.html', result=["FAIL", score])
    # return "You failed and the score is...." + str(score) + "%"


# This portion defines the action that happens on clicking 'Submit' button - first calculates the percent score and then redirects to the corresponding results page
@app.route('/submit', methods=['POST'])
def submit():
    percent_score = 0
    if request.method == 'POST':
        dbms_ = float(request.form['DBMS'])
        maths_ = float(request.form['Maths'])
        python_ = float(request.form['Python'])
        ml_ = float(request.form['ML'])
        total_score = dbms_+maths_+python_+ml_
        percent_score = total_score/400*100

    res = ''
    if percent_score>50:
        res= 'success'
    else:
        res = 'fail'
    return redirect(url_for(res,score=percent_score))

# Checks if this file is the main module to be executed
if __name__=='__main__':
    app.run(debug=True)

