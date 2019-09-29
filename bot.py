import bot_config
import requests
import json
import telebot
from pprint import pprint
from telebot import apihelper
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

sticker = (
	"CAADAgADeQMAArarPwullRa4zzq2ThYE",)

TOKEN = bot_config.TOKEN
bot = telebot.TeleBot(TOKEN)

apihelper.proxy = {'https':'https://157.245.128.84:8080'}

def Button(message):
	r = requests.get('http://127.0.0.1:8000/api/button')
	data = json.loads(r.text)
	key = ReplyKeyboardMarkup(True, False)
	text = 'Hello'
	for i in range(len(data['list'])):
		button = KeyboardButton(data['list'][i]['name'])
		key.add(button)
	bot.send_message(message.from_user.id, text, reply_markup=key)

@bot.message_handler(commands=['start', 'help'])
def start(message):
    Button(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Привет")

@bot.message_handler(content_types=['sticker'])
def print_message(message):
    pprint(message.json)
    bot.send_sticker(message.chat.id, sticker)

bot.polling(none_stop=True)
