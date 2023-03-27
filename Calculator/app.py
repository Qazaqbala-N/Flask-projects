from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def calculate():
    return render_template('calc.html')


@app.route('/math')
def printer():
    num = int(request.args.get('num1'))
    num2 = int(request.args.get('num2'))
    operation = request.args.get('calculation')

    if operation == "add":
        return f"{num + num2}"
    if operation == "subtract":
        return f"{num - num2}"
    if operation == "multiply":
        return f"{num * num2}"
    if operation == "divide":
        return f"{num / num2}"

