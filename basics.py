from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World'

# Routing process


@app.route('/some_method')
def some_method():
    return '<h1>Hello Buddy</h1>'

# differnet URLs


@app.route('/puppy/<name>')
def puppy(name):
    return 'Upper case: {}'.format(name[100])

# dynamic routing


@app.route('/puppy_latin/<name>')
def puppy_latin(name):
    puppy_name = ''
    if name[-1] == 'y':
        puppy_name = name[:-1] + 'iful'
    else:
        puppy_name = name + 'y'

    return "<h1>Your puppy latin name is {}</h1>".format(puppy_name)

# Dynamic routing exercise

if __name__ == '__main__':
    app.run(debug=True)
