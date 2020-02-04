import pandas as pd
from flask import Flask, render_template
from openpyxl import Workbook, load_workbook
workbook = load_workbook(filename='sheets/omegalul.xlsx')
sheet = workbook.active

sheet['B3']

workbook.save(filename='need.xlsx')

app = Flask(__name__)

@app.route('/sheet')
def hello():
    
    df = pd.read_excel('need.xlsx')
    return df.to_html()


@app.route('/work')
def test():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()