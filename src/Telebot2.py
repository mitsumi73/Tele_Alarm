import sched
import time
import asyncio
from datetime import datetime
import pytz
from dotenv import load_dotenv
import telebot
import os


load_dotenv()
TOKEN = os.getenv('TELEGRAM_API_KEY')
CHAT_ID = os.getenv('TELEGRAM_CHAT_ID')

bot = telebot.TeleBot(TOKEN)
bot.send_message(CHAT_ID, "Hello")
scheduler = sched.scheduler(time.time, time.sleep)

def send_message(chat_id):
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    time_str = now.strftime("%H:%M")
    message = f"Current time: {time_str}"
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(bot.send_message(chat_id, message))
    loop.close()

def scheduler_job():
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    if 23 > now.hour >= 6:
        send_message(CHAT_ID)
    scheduler.enter(1800, 1, scheduler_job)

scheduler.enter(0, 1, scheduler_job)
scheduler.run()