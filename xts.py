import schedule
import time
import pandas as pd
from flask import Flask, render_template
from openpyxl import Workbook, load_workbook

logger = logging.getLogger('schedule')
workbook = load_workbook(filename='sheets/Pirmdiena.xlsx')
sheet = workbook.active
stundas = 1

def piesk():
    stundas + 1

def nulite():
    stundas == 0

def pirunotr():
    sheet.delete_rows(idx=6, amount=8)
    sheet.delete_rows(idx=10, amount=8)
    sheet.delete_rows(idx=14, amount=8)
    workbook.save(filename='need.xlsx')

def otruntre():
    sheet.delete_rows(idx=4, amount=1)
    sheet.delete_rows(idx=6, amount=7)
    sheet.delete_rows(idx=8, amount=1)
    sheet.delete_rows(idx=10, amount=7)
    sheet.delete_rows(idx=12, amount=1)
    sheet.delete_rows(idx=14, amount=7)
    workbook.save(filename='need.xlsx')

def treuncet():
    sheet.delete_rows(idx=4, amount=2)
    sheet.delete_rows(idx=6, amount=6)
    sheet.delete_rows(idx=8, amount=2)
    sheet.delete_rows(idx=10, amount=6)
    sheet.delete_rows(idx=12, amount=2)
    sheet.delete_rows(idx=14, amount=6)
    workbook.save(filename='need.xlsx')

def cetunpie():
    sheet.delete_rows(idx=4, amount=3)
    sheet.delete_rows(idx=6, amount=5)
    sheet.delete_rows(idx=8, amount=3)
    sheet.delete_rows(idx=10, amount=5)
    sheet.delete_rows(idx=12, amount=3)
    sheet.delete_rows(idx=14, amount=5)
    workbook.save(filename='need.xlsx')

def pieunses():
    sheet.delete_rows(idx=4, amount=4)
    sheet.delete_rows(idx=6, amount=4)
    sheet.delete_rows(idx=8, amount=4)
    sheet.delete_rows(idx=10, amount=4)
    sheet.delete_rows(idx=12, amount=4)
    sheet.delete_rows(idx=14, amount=4)
    workbook.save(filename='need.xlsx')

def sesunsep():
    sheet.delete_rows(idx=4, amount=5)
    sheet.delete_rows(idx=6, amount=3)
    sheet.delete_rows(idx=8, amount=5)
    sheet.delete_rows(idx=10, amount=3)
    sheet.delete_rows(idx=12, amount=5)
    sheet.delete_rows(idx=14, amount=3)
    workbook.save(filename='need.xlsx')

def sepunast():
    sheet.delete_rows(idx=4, amount=6)
    sheet.delete_rows(idx=6, amount=2)
    sheet.delete_rows(idx=8, amount=6)
    sheet.delete_rows(idx=10, amount=2)
    sheet.delete_rows(idx=12, amount=6)
    sheet.delete_rows(idx=14, amount=2)
    workbook.save(filename='need.xlsx')

def astundev():
    sheet.delete_rows(idx=4, amount=7)
    sheet.delete_rows(idx=6, amount=1)
    sheet.delete_rows(idx=8, amount=7)
    sheet.delete_rows(idx=10, amount=1)
    sheet.delete_rows(idx=12, amount=7)
    sheet.delete_rows(idx=14, amount=1)
    workbook.save(filename='need.xlsx')

def devundes():
    sheet.delete_rows(idx=4, amount=8)
    sheet.delete_rows(idx=8, amount=8)
    sheet.delete_rows(idx=12, amount=8)
    workbook.save(filename='need.xlsx')

# schedule.every().day.at("07:20").do(piesk)
# schedule.every().day.at("08:50").do(piesk)
# schedule.every().day.at("09:40").do(piesk)
# schedule.every().day.at("10:30").do(piesk)
# schedule.every().day.at("11:20").do(piesk)
# schedule.every().day.at("12:10").do(piesk)
# schedule.every().day.at("13:00").do(piesk)
# schedule.every().day.at("13:50").do(piesk)
# schedule.every().day.at("14:35").do(piesk)
# schedule.every().day.at("16:20").do(nulite)

if stundas == 1:
    pirunotr()
elif stundas == 2:
    otruntre()
elif stundas == 3:
    treuncet()
elif stundas == 4:
    cetunpie()
elif stundas == 5:
    pieunses()
elif stundas == 6:
    sesunsep()
elif stundas == 7:
    sepunast()
elif stundas == 8:
    astundev()
elif stundas == 9:
    devundes()

app = Flask(__name__)

@app.route('/sheet')
def hello():
    if stundas == 0:
        return render_template('hello.html')
    elif stundas > 0:
        df = pd.read_excel('need.xlsx')
        return df.to_html()

if __name__ == '__main__':
    app.run()
