from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/report')
def report():
    is_lower = False
    is_upper = False
    is_numb = False

    user_name = request.args.get('user_name')
    is_lower = any(c.islower() for c in user_name)
    is_upper = any(c.isupper() for c in user_name)
    is_numb = user_name[-1].isdigit()

    is_passed = is_lower and is_upper and is_numb

    return render_template('report.html', is_passed=is_passed, 
                           is_lower=is_lower, is_numb=is_numb)


if __name__ == "__main__":
    app.run(debug=True)
