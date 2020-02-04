import pandas as pd
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/sheet')
def hello():
    df = pd.read_excel("sheets/7.-9.kl._27_l.xlsx")
    return df.to_html()

@app.route('/work')
def test():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()