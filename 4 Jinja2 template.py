### Jinja2 template engine
'''
{%...%} conditions, loops
{{...}} print
{#...#} comments
'''

### Integrate html file
### Methods like GET,POST

from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    res = ''
    if score>=50:
        res = 'PASS'
    else:
        res = 'FAIL'

    exp = {'score':score,'res':res}
    return render_template('result.html',marks = exp)

@app.route('/fail/<int:score>')
def fail(score):
    return f"Dhanuvanth scored {score} is a fail"

@app.route('/result/<int:score>')
def result(score):
    marks = ""
    if score > 40:
        marks = "success"
    else:
        marks = "fail"
    return redirect(url_for(marks,score= score))

@app.route('/submit', methods = ['POST','GET'])
def submit():
    total_score = 0
    if  request.method == 'POST':
        eng = float(request.form['eng'])
        maths = float(request.form['maths'])
        sci = float(request.form['sci'])
        soc = float(request.form['soc'])

        total_score = (eng + maths + sci + soc)/4
    
    res = ""
    if total_score >= 50:
        res = "success"
    else:
        res = "fail"

    return redirect(url_for(res,score= total_score))


if  __name__ == '__main__':
    app.run(debug=True)