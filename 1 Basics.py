from flask import Flask

### WSGI Application ###
app = Flask(__name__)

@app.route('/')
def Welcome():
    return 'Hello Dhanu!!!'

@app.route('/sri')
def Greating():
    return 'Hello Sri!!!'

# Module
if __name__ == '__main__':
    # run main file
    app.run(debug=True)