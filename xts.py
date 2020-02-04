import pandas as pd
from flask import Flask, render_template
from openpyxl import Workbook, load_workbook

workbook = load_workbook(filename='sheets/Pirmdiena.xlsx')
sheet = workbook.active

stundas = 34

def pirunotr():
    sheet.delete_rows(idx=6, amount=7)
    sheet.delete_rows(idx=10, amount=7)
    sheet.delete_rows(idx=14, amount=7)
    workbook.save(filename='need.xlsx')

def otruntre():
    sheet.delete_rows(idx=4, amount=1)
    sheet.delete_rows(idx=6, amount=6)
    sheet.delete_rows(idx=8, amount=1)
    sheet.delete_rows(idx=10, amount=6)
    sheet.delete_rows(idx=12, amount=1)
    sheet.delete_rows(idx=14, amount=6)
    workbook.save(filename='need.xlsx')

def treuncet():
    sheet.delete_rows(idx=4, amount=2)
    sheet.delete_rows(idx=6, amount=5)
    sheet.delete_rows(idx=8, amount=2)
    sheet.delete_rows(idx=10, amount=5)
    sheet.delete_rows(idx=12, amount=2)
    sheet.delete_rows(idx=14, amount=5)
    workbook.save(filename='need.xlsx')

def cetunpie():
    
    workbook.save(filename='need.xlsx')

def pieunses():
    
    workbook.save(filename='need.xlsx')

def sesunsep():
    
    workbook.save(filename='need.xlsx')

def sepunast():

    workbook.save(filename='need.xlsx')

def astundev():

    workbook.save(filename='need.xlsx')

if stundas == 34:
    treuncet()

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