from flask import Flask
from flask import jsonify
from dotenv import dotenv_values
from flask import request
from controllers import operation, calculate
from flask import render_template

app = Flask(__name__)


@app.route("/")
def server_info():
    # return "My server"
    return render_template('index.html')


@app.route("/author")
def author():
    author = {
        "name": "qwerty",
        "course": 3,
        "age": 21,
    }
    # author=jsonify(author)
    return render_template('author.html', author=author)


def get_port() -> int:
    config = dotenv_values(".env")
    if "PORT" in config:
        return int(config["PORT"])
    return 5000


@app.route("/sum", methods=['GET', 'POST'])
def runner():
    if request.method == 'POST':
        str = request.form['content']
        for i in str:
            if i == '+':
                oper = '+'
            elif i == '-':
                oper = '-'
            elif i == '*':
                oper = '*'
            elif i == '/':
                oper = '/'
        str = str.split(oper)
        a = int(str[0])
        b = int(str[-1])
        ans = {'ans': calculate(a, b, oper)}
        return render_template('answer.html', ans=ans)
    # a = request.args.get('a', type=int)
    # b = request.args.get('b', type=int)
    # return jsonify({'sum': operation(a, b)})
    return render_template('calculator.html')


if __name__ == "__main__":
    app.run(debug=True, port=get_port())
