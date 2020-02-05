import schedule
import time

def run_schedule():
    while True:
        schedule.run_pending()