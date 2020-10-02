from rest_framework.views import APIView
from rest_framework.response import Response

from telegram import Update

from .dispatcher import setup


class WebHookView(APIView):
    def post(self, request, *args, **kwargs):
        req = request.data

        dispatcher = setup()
        update = Update.de_json(req, dispatcher.bot)
        dispatcher.process_update(update)
        return Response({'status': 'Messages sent'})
