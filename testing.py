import time
import datetime
import schedule

memes = 2

def gay():
    print(memes)

def gaynt():
    memes == 0
    
schedule.every().day.at("09:28").do(gay) 

while True:
    schedule.run_pending()