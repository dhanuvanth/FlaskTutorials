### Building a dynamic url

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Welcome Dhanuvanth"

@app.route('/Success/<int:score>')
def Success(score):
    return f"Dhanuvanth scored {score} is a Success"

@app.route('/fail/<int:score>')
def fail(score):
    return f"Dhanuvanth scored {score} is a fail"

@app.route('/result/<int:score>')
def result(score):
    marks = ""
    if score > 40:
        marks = "Success"
    else:
        marks = "fail"
    return redirect(url_for(marks,score= score))

if  __name__ == '__main__':
    app.run(debug=True)