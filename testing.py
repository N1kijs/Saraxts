import time
import datetime
import schedule

memes = 1

def gay():
    memes += 1
    print(memes)

def gaynt():
    memes == 0
    
schedule.every().day.at("09:49").do(gay) 

while True:
    schedule.run_pending()