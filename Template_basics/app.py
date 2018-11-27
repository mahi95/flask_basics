from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/index')
def index():
    return render_template('index.html')

# Template rendering

@app.route('/template_variable')
def template_func():
    name = 'Anand'
    letters = list(name)
    puppy_dict = {'puppy_name':'sammy'}
    return render_template('basic.html', name=name, letters=letters, puppy_dict=puppy_dict)

# Template flow_control

@app.route('/template_flow')
def template_flow():
    name = 'Anand'
    letters = list(name)
    puppy_dict = {'puppy_name':'sammy'}
    puppy_list = ['Rufus', 'Abigail', 'Sammy']
    return render_template('basic.html', puppy_list=puppy_list, name=name, letters=letters,               
                          puppy_dict=puppy_dict)

# Template  and url_for

@app.route('/home_page')
def home():
    return render_template('home.html')

@app.route('/puppy_name/<name>')
def puppy_name(name):
    return render_template('puppy.html', name=name)

# Template forms

@app.route('/')
def index_f():
    return render_template('indexf.html')

@app.route('/signup_form')
def signup_form():
    return render_template('signupf.html')

@app.route('/thank_you')
def thank_you():
    first = request.args.get('first')
    last = request.args.get('last')

    return render_template('thankyouf.html', first=first, last=last)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

if __name__ == '__main__':
    app.run(debug=True)