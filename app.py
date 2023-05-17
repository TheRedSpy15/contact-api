import asyncio
from flask import Flask, request
from aiogram import Bot, Dispatcher
import aiohttp

app = Flask(__name__)

def read_config(file_path):
    config = {}
    with open(file_path) as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

config = read_config('config.txt')
bot_token = config.get('BOT_TOKEN')
bot_chat_id = config.get('CHAT_ID')

async def send_telegram_message(name, email, subject, message):
    message_text = f"New email received:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}"
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://api.telegram.org/bot{bot_token}/sendMessage", params={
            "chat_id": bot_chat_id,
            "text": message_text
        }) as response:
            if response.status == 200:
                return True
            else:
                return False

@app.route('/', methods=['POST'])
def index():
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    if email:
        success = asyncio.run(send_telegram_message(name, email, subject, message))
        if success:
            return f'Message sent via Telegram:\nName: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}', 201
        else:
            return 'Failed to send message via Telegram', 500
    else:
        return 'No email address provided', 400

@app.route('/health', methods=['GET'])
def health_check():
    return 'OK', 200

if __name__ == '__main__':
    app.run(port=5000)
