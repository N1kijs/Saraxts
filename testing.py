import time
import datetime
import schedule

memes = 1

def gay():
    global memes
    memes += 1
    print(memes)

def gaynt():
    global memes
    memes = 0
    print(memes)
    
schedule.every().wednesday.at("09:57").do(gay)
schedule.every().wednesday.at("09:58").do(gaynt) 

while True:
    schedule.run_pending()