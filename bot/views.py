from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Button, Text
import bot_config
import json
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from django.views import View
from django.http import HttpResponse
from telebot import types

TOKEN = bot_config.TOKEN
bot = telebot.TeleBot(TOKEN, threaded=False)
sticker = 'CAADAgADeQMAArarPwullRa4zzq2ThYE'

class GetList(View):
    def get(self, requests, *args, **kwargs):
        return HttpResponse("В работе")

    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])

        return Response({'code': 200})

@bot.message_handler(commands=['start'])
def start(message):
    data = {'list':[]}
    button = Button.objects.all()
    for i in button:
        data['list'].append({'name':i.button})
    key = ReplyKeyboardMarkup(True, False)
    text = 'Выберите категорию, которая вас интересует:'
    for i in range(len(data['list'])):
        buttons = KeyboardButton(data['list'][i]['name'])
        key.add(buttons)
    bot.send_message(message.from_user.id, text, reply_markup=key)

@bot.message_handler(content_types='text')
def send_message(message):
    get_button = Button.objects.get(button=message.text)
    text = Text.objects.get(button=get_button)
    bot.send_message(message.from_user.id, text)
