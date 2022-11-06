# Dynamic URL 
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)               
@app.route('/')
def home():
    return render_template('index.html')

#name of page and method should be same
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

# @app.route('/results/<int:mark>')
# def results(mark):
#     result = ''
#     if mark<50:
#         result='fail'
#     else:
#         result='success'
    
#     return redirect(url_for(result, score=mark))

# Result checker HTML page
@app.route('/submit', methods=['POST','GET'])
def submit():
    total_score = 0
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
        
if __name__=='__main__':
    app.run(debug=True)

