import json
import logging.config
import os
from pathlib import Path
from threading import Thread
from time import sleep
from datetime import datetime, timedelta, timezone
import pandas as pd
import requests
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# from dotenv import load_dotenv
from pybit import usdt_perpetual
from django.views.decorators.csrf import csrf_exempt
from .models import Greeting

# load_dotenv()

# logging.config.dictConfig({
#     "version": 1,
#     "disable_existing_loggers": False,
#     'formatters': {
#         'colored': {
#             '()': 'colorlog.ColoredFormatter',  # colored output
#             # --> %(log_color)s is very important, that's what colors the line
#             'format': '[%(asctime)s,%(lineno)s] %(log_color)s[%(message)s]',
#             'log_colors': {
#                 'DEBUG': 'green',
#                 'INFO': 'cyan',
#                 'WARNING': 'yellow',
#                 'ERROR': 'red',
#                 'CRITICAL': 'bold_red',
#             },
#         },
#         'simple': {
#             'format': '[%(asctime)s,%(lineno)s] [%(message)s]',
#         },
#     },
#     "handlers": {
#         "console": {
#             "class": "colorlog.StreamHandler",
#             "level": "INFO",
#             "formatter": "colored",
#             "stream": "ext://sys.stdout"
#         },
#         "file": {
#             "class": "logging.handlers.RotatingFileHandler",
#             "level": "INFO",
#             "formatter": "simple",
#             "filename": 'app-log.log'
#         },
#     },
#     "root": {"level": "INFO",
#              "handlers": ["console", "file"]
#              }
# })
# LOGGER = logging.getLogger()

PROJECT_ROOT = Path(os.path.abspath(os.path.dirname(__file__)))
# api_key = os.getenv("BYBIT_API_KEY")
# api_secret = os.getenv("BYBIT_API_SECRET")
# START_UNITS = os.getenv("START_UNITS")
# UNIT_PRICE = float(os.getenv("UNIT_PRICE"))
# RECOVERY_ZONE_TICKS = float(os.getenv("RECOVERY_ZONE_TICKS"))
# TP_SL_TICKS = float(os.getenv("TP_SL_TICKS"))
# TICK_PRICE = float(os.getenv("TICK_PRICE"))
# client = usdt_perpetual.HTTP(endpoint='https://api-testnet.bybit.com', api_key=api_key, api_secret=api_secret)
# ws = usdt_perpetual.WebSocket(test=True, api_key=api_key, api_secret=api_secret)


def send_telegram_msg(msg):
    bot_token = '5684091804:AAFovNuL9EIthkdLWw3HS-ZJbuw8ELPfnh8'
    chat_id = '1442986099'
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}'
    response = requests.get(url=str(send_text))
    print(response.json())
    return response.json()


# Create your views here.
def index(request):
    return render(request, "index.html", context={"account_balance": "account_balance"})


@csrf_exempt
def uploads(request):
    return render(request, 'test.html', context={"account_balance": "account_balance"})


def get_telegram_msg(request):
    resp = send_telegram_msg(msg="This Is a Test Msg")
    response = {
        "Message": resp}
    return JsonResponse(response)


def cc(request):
    bot_token = '5684091804:AAFovNuL9EIthkdLWw3HS-ZJbuw8ELPfnh8'
    chat_id = '1442986099'
    send_text = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}'
    response = requests.get(url=str(send_text))
    print(response.json())
    return JsonResponse(response)


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
