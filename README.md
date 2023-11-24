# <div align="center"> Telegram Bot Alarm

## How to Install

### Step 1: Install Python

1. Go to the [PyCharm download page](https://www.jetbrains.com/ko-kr/pycharm/download/?section=mac).
3. Click on the appropriate installer for your operating system.
3. Follow the prompts to complete the installation.

### Step 2: Create a Shell script environment

1. Open a terminal or command prompt.
2. Move to the folder containing the script `cd /path/to/directory`
3. Grant script execution permissions `chmod +x init_setup.sh`
4. Run the script with the following command:`./init_setup.sh`


### Step 3: Set up your Telegram bot
1. Create `.env` file and in the `.env` file:
> TELEGRAM_API_KEY="_Your_TELEGRAM_API_KEY"
> TELEGRAM_CHAT_ID="Your_TELEGRAM_CHAT_ID"
> 
2. See [these instructions](https://core.telegram.org/bots/tutorial#obtain-your-bot-token) for more information on how to do this.
> https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getMe  
or
> https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates
3. `pip install -r requirements.txt`
 
### Step 4: Run the Telegram bot server
1. Open a terminal or command prompt.
2. Navigate to the directory where you installed the ChatGPT Telegram bot.
3. Run `python3 src/Telebot2.py` to start the server.

## Main Code
```python
 def send_message(chat_id):
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    time_str = now.strftime("%H:%M")
    message = f"Current time: {time_str}"
    bot.send_message(chat_id, message)
```

```python
def scheduler_job():
    now = datetime.now(pytz.timezone('Asia/Seoul'))
    if 23 > now.hour >= 6:
        send_message(CHAT_ID)
    scheduler.enter(1800, 1, scheduler_job)
While True:
    scheduler.enter(0, 1, scheduler_job)
    scheduler.run()

```
## View in My Channel: [Tele_Alarm_channel](https://t.me/Tele_K20232) <span><img src="https://img.shields.io/badge/telegram-26A5E4?logo=telegram&logoColor=F7DF1E"/></span>
&nbsp;
## Execution Results
<a href="#" target="_blank">
  <img src="image/Run .png" width="1200"/>

