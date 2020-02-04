import pandas as pd
from flask import Flask, render_template
from openpyxl import Workbook, load_workbook

workbook = load_workbook(filename='sheets/Pirmdiena.xlsx')
sheet = workbook.active

sheet.delete_rows(idx=6, amount=7)
sheet.delete_rows(idx=17, amount=7)
sheet.delete_rows(idx=28, amount=7)

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