import sched
import time
from datetime import datetime
import pytz
from dotenv import load_dotenv
import telebot
import os

load_dotenv()
TOKEN = os.getenv('TELEGRAM_API_KEY')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(TOKEN)
scheduler = sched.scheduler(time.time, time.sleep)


def send_message(chat_id):
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    time_str = now.strftime("%H:%M")
    message = f"Current time: {time_str}"
    bot.send_message(chat_id, message)


def scheduler_job():
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    if 23 > now.hour >= 6:
        send_message(CHAT_ID)
    scheduler.enter(1800, 1, scheduler_job)


while True:
    scheduler.enter(0, 1, scheduler_job)
    try:
        scheduler.run()
    except KeyboardInterrupt:
        print("Program interrupted by user.")
        # Include any cleanup or resource release code here
