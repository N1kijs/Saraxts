import pandas as pd
from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/sup/')
def jeff():
    df = pr.read_excel('C:\\Users\\gvido\\Desktop\\Projektu ned\\omegalul.xlsx')
    return df.to_html()

@app.route('/hello/')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run()