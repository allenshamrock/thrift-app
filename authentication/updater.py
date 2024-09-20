"""
For testing purposes I used apscheduler to send the response at intervals of 10seconds
from apscheduler.schedulers.background import BackgroundScheduler
from . import message_update


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(message_update.send_sms_on_order, 'interval', seconds=10)
    scheduler.start()
    
"""


