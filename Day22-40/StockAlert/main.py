import requests
import os
from twilio.rest import Client

api_key = os.environ.get("STOCK_KEY")
stock_news_key = os.environ.get("NEWS_KEY")
sms_sid = os.environ.get("SMS_SID")
sms_token = os.environ.get("SMS_TOKEN")
from_number = os.environ.get("FROM_NUMBER")
to_number = os.environ.get("TO_NUMBER")

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key,
    "outputsize": "compact"
}
news_params = {
    "apiKey": stock_news_key,
    "q": COMPANY_NAME,
    "searchIn": "title,description",
    "from": "2023-11-01",
    "language": "en",
    "pageSize": 3
}
#
# data_response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
# data_response.raise_for_status()
# stock_data = data_response.json()
# # TODO:  get the closing stock price of last two recent data
# daily_stock_data = stock_data["Time Series (Daily)"]
# print(daily_stock_data)
prev_val = 0
percentage = 0.0
percentage_gap = ""
# short_dict = {k: daily_stock_data[k] for k in list(daily_stock_data.keys())[:2]}
short_dict = {'2023-11-24': {'1. open': '233.7500', '2. high': '238.7500', '3. low': '232.3300',
                             '4. close': '235.4500', '5. volume': '65125203'},
              '2023-11-22': {'1. open': '242.0400', '2. high': '244.0100',
                             '3. low': '231.4000', '4. close': '234.2100', '5. volume': '118117078'}}
# TODO: calculate the percentage difference
for key, value in short_dict.items():
    close_val = float(value["4. close"])
    diff = abs(close_val - prev_val)
    average = (close_val + prev_val) / 2
    if (close_val - prev_val) < 0:
        percentage_gap = "🔻"
    else:
        percentage_gap = "🔺"
    percentage = (diff / average) * 100
    prev_val = close_val
# TODO: if percentage is greater than 5, send a message of latest news about TESLA using twilio
if percentage > 5.00:
    news_data = requests.get("https://newsapi.org/v2/everything", params=news_params)
    news_data.raise_for_status()
    news_data_val = news_data.json()['articles']

    # TODO: get the first element only for sample
    # news_data_val = news_data_val[0]
    for data in news_data_val[:1]:
        title = data['title']
        desc = data['description']
        print(title, desc)
        client = Client(sms_sid, sms_token)
        message = client.messages \
            .create(body=f"TSLA : {percentage}{percentage_gap} \n Headline: {title}\nBrief: {desc}\n ",
                    from_=from_number,
                    to=to_number)
        print(message.sid)
