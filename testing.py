import time
import schedule

memes = 0

def gay():
    memes +1
    print memes

def gaynt():
    memes == 0
    
schedule.every().wednesday.at("08:53").do(gay)

while True:
    schedule.run_pending() 
    time.sleep(1)