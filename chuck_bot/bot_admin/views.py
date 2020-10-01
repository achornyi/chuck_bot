import json

import requests
from rest_framework.views import APIView
from rest_framework.response import Response

import telegram

from .models import Greeting, Helper
from chuck_bot.settings import BOT_TOKEN, NGROK_URL

TELEGRAM_URL = 'https://api.telegram.org/bot'
bot = telegram.Bot(token=BOT_TOKEN)


class WebHookView(APIView):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        message = data['message']
        chat = message['chat']

        try:
            text = message['text'].strip().lower()
        except Exception as e:
            return Response({'ok': f'POST request processed: {e}'})

        if text == '/start':
            latest_greeting = Greeting.objects.latest('id')
            msg = latest_greeting.hello_world
        elif text == '/help':
            latest_helper = Helper.objects.latest('id')
            msg = latest_helper.help
        elif text == '/chuck':
            msg = self.get_chuck_joke()
        else:
            msg = text.upper()

        self.send_message(msg, chat['id'])
        return Response({'ok': 'POST request processed'})

    @staticmethod
    def get_chuck_joke():
        try:
            contents = requests.get('https://api.chucknorris.io/jokes/random').json()
            joke = contents['value']
        except requests.RequestException:
            joke = "Chuck broke Internet, so we can't find new stories about him"
        return joke

    @staticmethod
    def send_message(message, chat_id):
        data = {
            'chat_id': chat_id,
            'text': message,
            'parse_mode': 'Markdown',
        }
        requests.post(
            f'{TELEGRAM_URL}{BOT_TOKEN}/sendMessage', data=data
        )


class SetWebHookView(APIView):
    def get(self, request, format=None):
        try:
            bot.setWebhook('{URL}{HOOK}'.format(URL=f'https://{NGROK_URL}/', HOOK=BOT_TOKEN))
            return Response({'ok': 'webhook setup ok'})
        except Exception as e:
            return Response({'ok': f'webhook setup failed: {e}'})

