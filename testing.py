import time
import datetime
import schedule

memes = 0

def gay():
    memes +1
    print(memes)

def gaynt():
    memes == 0
    
schedule.every().wednesday.at("09:12").do(gay)

while True:
    schedule.run_pending()