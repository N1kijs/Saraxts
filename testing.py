import time
import datetime
import schedule

memes = 2

def gay():
    memes + 1
    print(memes)

def gaynt():
    memes == 0
    
schedule.every().day.at("09:41").do(gay) 

while True:
    schedule.run_pending()