from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    user_name = request.args.get('user_name')
    failed_list = []
    is_passed = False
    is_lower = False
    is_upper = False
    is_numb = False
    if ord(user_name[-1]) >= 48 and ord(user_name[-1]) <= 57:
        is_numb = True
    for each_string in user_name:
        if each_string.islower():
            is_lower = True
        if each_string.isupper():
            is_upper = True
    if is_lower and is_upper and is_numb:
        is_passed = True
    elif is_lower:
        failed_list = ['you did not use an upper case letter',
                       'you did not end your user name with a number']
    elif is_upper:
        failed_list = ['you did not use an lower case letter',
                       'you did not end your user name with a number']
    else:
        failed_list = ['you did not use an lower case letter',
                       'you did not use an upper case letter']

    return render_template('report.html', is_passed=is_passed,
                           failed_list=failed_list)


if __name__ == '__main__':
    app.run(debug=True)
