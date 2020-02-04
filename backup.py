import pandas as pd
from flask import Flask, render_template
from openpyxl import load_workbook
app = Flask(__name__)

@app.route('/sheet')
def hello():
    df = pd.read_excel("sheets/10-12kl_27_ I.xlsx")
    return df.to_html()

@app.route('/work')
def test():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()