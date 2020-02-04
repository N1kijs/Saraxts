import pandas as pd
from flask import Flask, render_template
from openpyxl import load_workbook
workbook = load_workbook(filename='sheets/omegalul.xlsx')
sheet = workbook.active
app = Flask(__name__)

@app.route('/sheet')
def hello():
    needs = sheet['B3']
    df = needs
    return df


@app.route('/work')
def test():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()