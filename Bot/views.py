import json
import logging.config
import os
from pathlib import Path
from threading import Thread
from time import sleep
from datetime import datetime, timedelta, timezone
import pandas as pd
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

# PROJECT_ROOT = Path(os.path.abspath(os.path.dirname(__file__)))
# api_key = os.getenv("BYBIT_API_KEY")
# api_secret = os.getenv("BYBIT_API_SECRET")
# START_UNITS = os.getenv("START_UNITS")
# UNIT_PRICE = float(os.getenv("UNIT_PRICE"))
# RECOVERY_ZONE_TICKS = float(os.getenv("RECOVERY_ZONE_TICKS"))
# TP_SL_TICKS = float(os.getenv("TP_SL_TICKS"))
# TICK_PRICE = float(os.getenv("TICK_PRICE"))
# client = usdt_perpetual.HTTP(endpoint='https://api-testnet.bybit.com', api_key=api_key, api_secret=api_secret)
# ws = usdt_perpetual.WebSocket(test=True, api_key=api_key, api_secret=api_secret)


# def handle_execution(message):
#     order = json.loads(json.dumps(message, indent=4))
#     print(f'Execution Status: {order["data"][0]["order_status"]}')
#     # if order["data"][0]["order_status"] == "Filled":
#     #     print(f'Placing buy limit TP/SL order')
#     #     order = client.place_active_order(
#     #         symbol=symbol,
#     #         side="Buy",
#     #         order_type="Limit",
#     #         qty=quantity,
#     #         price=buy_price,
#     #         take_profit=take_profit,
#     #         stop_loss=stop_loss,
#     #         time_in_force="GoodTillCancel",
#     #         reduce_only=False,
#     #         close_on_trigger=False
#     #     )
#     #     order = json.loads(json.dumps(order, indent=4))['result']
#     #     print(f"TP/SL limit order: {order}")
#
#
# # Convert to DataFrame and save
# def save_data_frame(msg):
#     df = pd.DataFrame([msg])
#     df = df.loc[:, ['timestamp', 'symbol', 'price']]
#     df.columns = ['Time', 'Symbol', 'Price']
#     df["Price"] = df["Price"].astype(float)
#     df["Time"] = pd.to_datetime(df["Time"])
#     # print(f'Trade Data: {df}')
#     file_path = str(PROJECT_ROOT / f'{symbol}.csv')
#     df.to_csv(file_path, index=False)
#     # if not os.path.isfile(file_path):
#     #     data_frame.to_csv(file_path, index=False)
#     # else:  # else if exists so append without writing the header
#     #     data_frame.to_csv(file_path, mode='a', header=False, index=False)
#
#
# def handle_trade(message):
#     trade_data = json.loads(json.dumps(message, indent=4))
#     # print(f'Trade Data: {trade_data["data"][0]}')
#     save_data_frame(msg=trade_data["data"][0])
#
#
# def get_data_frame(symbol):
#     file_path = str(PROJECT_ROOT / f'{symbol}.csv')
#     return pd.read_csv(file_path, index_col=None)
#
#
#
# # Subscribe to the execution topics
# def get_connected():
#     # Subscribe to the execution topics
#     # ws.execution_stream(handle_execution)
#     ws.trade_stream(callback=handle_trade, symbol=symbol)
#     ws.order_stream(handle_order)
#     print(f'Websocket connected')
#     # while True:
#     #     print(f'Websocket status: {ws.test}')
#     #     sleep(1)

# Start WebSocket in a separate thread
# Thread(target=get_connected).start()
# get_connected()


# Create your views here.
# def index(request):
#     account_balance = client.get_wallet_balance(coin='USDT')["result"]["USDT"]["wallet_balance"]
#     if request.method == 'POST' and "trades" in request.POST:
#         user_trades = client.user_trade_records(symbol=symbol)
#         # print(f'Trades: {trades}')
#         user_trades = json.loads(json.dumps(user_trades, indent=4))["result"]["data"]
#         user_trades = [
#             {"Order No": i, "Order ID": trade["order_id"], "Symbol": trade["symbol"], "Side": trade["side"],
#              "Order Type": trade["order_type"], "Price": trade["price"], "Quantity": trade["order_qty"],
#              "Trade Time": pd.to_datetime(trade["trade_time_ms"], unit="ms")
#              } for i, trade in enumerate(user_trades)]
#         # print(f'User trades {symbol}: {user_trades}')
#         return render(request, "index.html", context={"account_balance": account_balance, "trades": user_trades})
#     return render(request, "index.html", context={"account_balance": account_balance})


# # Check on your order and position through WebSocket.
# def handle_order(message):
#     order = json.loads(json.dumps(message, indent=4))
#     if order["data"][0]["order_status"] == "Cancelled":
#         return
#     order_id = order["data"][0]["order_id"]
#     exp_time = pd.to_datetime(order["data"][0]["create_time"]) + timedelta(seconds=exp_time_sec)
#     order_price = float(order["data"][0]["price"])
#     qty = float(order["data"][0]["qty"])
#     while True:
#         sleep(3)
#         df = get_data_frame(symbol=symbol)
#         df["Time"] = pd.to_datetime(df["Time"])
#         df["Price"] = df["Price"].astype(float)
#         order = client.query_active_order(symbol=symbol, order_id=order_id)
#         print(f'Status: {order["result"][0]["order_status"]}, Time created at: {pd.to_datetime(order["result"][0]["create_time"])}, Time expires at: {exp_time}, Time now: {datetime.now(timezone.utc)}')
#         if order["result"][0]["order_status"] == "Cancelled":
#             return
#         elif order["result"][0]["order_status"] != "Filled" and (datetime.now(timezone.utc) > exp_time or order_price - (buy_range / 2) <= df.iloc[-1]['Price'] <= order_price + (buy_range / 2)):
#             # print(f"Price range condition: {order_price - (buy_range / 2) <= df.iloc[-1]['Price'] <= order_price + (buy_range / 2)}, {order_price - (buy_range / 2)} <= {df.iloc[-1]['Price']} <= {order_price + (buy_range / 2)}")
#             # print(f'Cancelling the first limit order')
#             print(f'Status: {order["result"][0]["order_status"]}, Time created at: {pd.to_datetime(order["result"][0]["create_time"])}, Time expires at: {exp_time}, Time now: {datetime.now(timezone.utc)}')
#             try:
#                 client.cancel_active_order(symbol=symbol, order_id=order_id)
#                 print(f'Order has been cancelled')
#             except:
#                 pass
#             buy_price = df.iloc[-1]['Price']
#             if buy_price % 100 == 0:
#                 buy_price = df.iloc[-1]['Price'] - 1
#             # print(f'Placing new buy limit order at price: {buy_price - buy_less}')
#             order_buy = client.place_active_order(
#                 symbol=symbol,
#                 side="Buy",
#                 position_idx=0,
#                 order_type="Limit",
#                 qty=qty,
#                 price=buy_price - buy_less,
#                 time_in_force="PostOnly",
#                 reduce_only=False,
#                 close_on_trigger=False
#             )
#             order_buy = json.loads(json.dumps(order_buy, indent=4))['result']
#             print(f"New buy limit order has been placed: {order_buy}")
#             return
#             # print(f"Switching TP/SL mode to Partial")
#             # tp_sl_mode = client.full_partial_position_tp_sl_switch(symbol=symbol, tp_sl_mode="Partial")
#             # tp_sl_mode = json.loads(json.dumps(tp_sl_mode, indent=4))['result']
#             # print(f"TP/SL Mode: {tp_sl_mode}")
#         elif order["result"][0]["order_status"] == "Filled":
#             sell_price = df.iloc[-1]['Price']
#             if sell_price % 100 == 0:
#                 sell_price = df.iloc[-1]['Price'] + 1
#             print(f'Placing SL limit sell order first: 30%')
#             # Sell first 30%
#             order_sell = client.place_active_order(
#                 symbol=symbol,
#                 side="Sell",
#                 position_idx=0,
#                 order_type="Limit",
#                 qty=float(qty / 3.33),
#                 price=sell_price + sell_a,
#                 stop_loss=sell_price - stop_loss,
#                 time_in_force="PostOnly",
#                 reduce_only=True,
#                 close_on_trigger=False
#             )
#             order_sell = json.loads(json.dumps(order_sell, indent=4))['result']
#             print(f"Limit sell order has been placed: {order_sell}")
#             print(f'Placing SL sell order second: 50%')
#             # Sell second: 50%
#             order_sell = client.place_active_order(
#                 symbol=symbol,
#                 side="Sell",
#                 position_idx=0,
#                 order_type="Limit",
#                 qty=qty / 2,
#                 price=sell_price + sell_b,
#                 stop_loss=sell_price - stop_loss,
#                 time_in_force="PostOnly",
#                 reduce_only=True,
#                 close_on_trigger=False
#             )
#             order_sell = json.loads(json.dumps(order_sell, indent=4))['result']
#             print(f"SL limit sell order has been placed: {order_sell}")
#             # Set Trailing Stop on Buy position
#             # client.set_trading_stop(
#             #     symbol=symbol,
#             #     side="Sell",
#             #     trailing_stop=stop_loss
#             # )
#             # order = json.loads(json.dumps(order, indent=4))['result']
#             # print(f"TS has been placed: {order}")
#
#
# @csrf_exempt
# def trades(request):
#     account_balance = client.get_wallet_balance(coin='USDT')["result"]["USDT"]["wallet_balance"]
#     if request.method == 'POST':
#         if "BUY 3" in str(request.POST):
#             request_data = str(request.POST)
#             print(f'REQUEST METHOD: {request.method}, DATA: {request_data}')
#             print(f"Account Balance: {account_balance}")
#             print(f'TradingView Alert Data: {request_data}')
#             # client.cancel_all_active_orders(symbol=symbol)
#             # client.cancel_all_conditional_orders(symbol=symbol)
#             df = get_data_frame(symbol=symbol)
#             df["Time"] = pd.to_datetime(df["Time"])
#             df["Price"] = df["Price"].astype(float)
#             print(f"{symbol} price: {df.iloc[-1]['Price']}")
#             buy_price = df.iloc[-1]['Price']
#             if buy_price % 100 == 0:
#                 buy_price = buy_price - 1
#             # quantity = round(account_balance / buy_price)
#             order = client.place_active_order(
#                 symbol=symbol,
#                 side="Buy",
#                 position_idx=0,
#                 order_type="Limit",
#                 qty=quantity,
#                 price=buy_price - buy_less,
#                 time_in_force="GoodTillCancel",
#                 reduce_only=False,
#                 close_on_trigger=False
#             )
#             order = json.loads(json.dumps(order, indent=4))["result"]
#             order = {"order_id": order["order_id"], "symbol": order["symbol"], "side": order["side"],
#                      "order_type": order["order_type"], "price": order["price"],
#                      "qty": order["qty"], "order_status": order["order_status"],
#                      "TP": order["take_profit"], "SL": order["stop_loss"], "created_time": pd.to_datetime(order["created_time"])
#                      }
#             print(f"Buy Limit order has been placed: {order}")
#             return render(request, 'trades.html', {"account_balance": account_balance, "order": order})
#         elif "BUY 3" in request.body.decode(encoding="utf-8"):
#             request_data = json.loads(request.body.decode(encoding="utf-8"))
#             print(f'REQUEST METHOD: {request.method}, DATA: {request_data}')
#             print(f"Account Balance: {account_balance}")
#             print(f'TradingView Alert Data: {request_data}')
#             # client.cancel_all_active_orders(symbol=symbol)
#             # client.cancel_all_conditional_orders(symbol=symbol)
#             df = get_data_frame(symbol=symbol)
#             df["Time"] = pd.to_datetime(df["Time"])
#             df["Price"] = df["Price"].astype(float)
#             print(f"{symbol} price: {df.iloc[-1]['Price']}")
#             buy_price = df.iloc[-1]['Price']
#             if buy_price % 100 == 0:
#                 buy_price = buy_price - 1
#             # quantity = round(account_balance / buy_price)
#             order = client.place_active_order(
#                 symbol=symbol,
#                 side="Buy",
#                 position_idx=0,
#                 order_type="Limit",
#                 qty=quantity,
#                 price=buy_price - buy_less,
#                 time_in_force="GoodTillCancel",
#                 reduce_only=False,
#                 close_on_trigger=False
#             )
#             order = json.loads(json.dumps(order, indent=4))["result"]
#             order = {"order_id": order["order_id"], "symbol": order["symbol"], "side": order["side"],
#                      "order_type": order["order_type"], "price": order["price"],
#                      "qty": order["qty"], "order_status": order["order_status"],
#                      "TP": order["take_profit"], "SL": order["stop_loss"], "created_time": pd.to_datetime(order["created_time"])
#                      }
#             print(f"Buy Limit order has been placed: {order}")
#             return render(request, 'trades.html', {"account_balance": account_balance, "order": order})
#         # Get trades data
#         elif "trades" in request.POST:
#             print(f'REQUEST METHOD: {request.method}, DATA: {request.POST}')
#             user_trades = client.user_trade_records(symbol=symbol)
#             user_trades = json.loads(json.dumps(user_trades, indent=4))["result"]["data"]
#             user_trades = [
#                 {"Order No": i, "Order ID": trade["order_id"], "Symbol": trade["symbol"], "Side": trade["side"],
#                  "Order Type": trade["order_type"], "Price": trade["price"], "Quantity": trade["order_qty"],
#                  "Trade Time": pd.to_datetime(trade["trade_time_ms"], unit="ms")
#                  } for i, trade in enumerate(user_trades)]
#             # print(f'User trades {symbol}: {user_trades}')
#             return render(request, "trades.html", context={"account_balance": account_balance, "trades": user_trades})
#         # Get active orders
#         elif "orders" in request.POST:
#             print(f'REQUEST METHOD: {request.method}, DATA: {request.POST}')
#             user_orders = client.query_active_order(symbol=symbol)
#             user_orders = json.loads(json.dumps(user_orders, indent=4))["result"]
#             user_orders = [
#                 {"No": i, "ID": order["order_id"], "Symbol": order["symbol"], "Side": order["side"],
#                  "Type": order["order_type"], "Price": order["price"], "Quantity": order["qty"], "Status": order["order_status"],
#                  "TP": order["take_profit"], "SL": order["stop_loss"], "Created Time": pd.to_datetime(order["created_time"])
#                  } for i, order in enumerate(user_orders)]
#             # print(f'User orders {symbol}: {user_orders}')
#             return render(request, "trades.html", context={"account_balance": account_balance, "orders": user_orders})
#         elif "cancelorders" in request.POST:
#             print(f'REQUEST METHOD: {request.method}, DATA: {request.POST}')
#             print(f'Cancelling active orders')
#             client.cancel_all_active_orders(symbol=symbol)
#             client.cancel_all_conditional_orders(symbol=symbol)
#             if client.my_position(symbol=symbol):
#                 try:
#                     client.close_position(symbol=symbol)
#                 except:
#                     pass
#             return render(request, "trades.html", context={"account_balance": account_balance})
#         elif "getpositions" in request.POST:
#             print(f'REQUEST METHOD: {request.method}, DATA: {request.POST}')
#             positions = client.my_position(symbol=symbol)
#             positions = json.loads(json.dumps(positions, indent=4))["result"]
#             positions = [
#                 {"No": i, "Symbol": order["symbol"], "Side": order["side"],
#                  "Size": order["size"], "Position Value": order["position_value"], "Entry Price": order["entry_price"],
#                  "Leverage": order["leverage"], "Free Qty": order["free_qty"], "TP": order["take_profit"], "SL": order["stop_loss"],
#                  "TS": order["trailing_stop"]
#                  } for i, order in enumerate(positions)]
#             # print(f'Positions {symbol}: {positions}')
#             return render(request, "trades.html", context={"account_balance": account_balance, "positions": positions})
#     return render(request, 'trades.html', context={"account_balance": account_balance})


def cc(request):
    response = {
        "CC": 0,
        "Send": 0,
        "OverWrite": 0,
        "Delete": 0
    }
    return JsonResponse(response)


def db(request):
    greeting = Greeting()
    greeting.save()
    greetings = Greeting.objects.all()
    return render(request, "db.html", {"greetings": greetings})
