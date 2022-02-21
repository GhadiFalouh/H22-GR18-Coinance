import requests
import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    #return HttpResponse('Hello')
    #return render(request, 'hello.html', {'name' : 'abc'})

    symbol = 'AAPL'
    exchange = 'CAD'
    start_date = '2022-02-10'
    api_key = '8J490IQR8EM1XK8E'
    # api_url = f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market={exchange}&apikey={api_key}'
    api_url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&apikey=8J490IQR8EM1XK8E'

    r = requests.get(api_url)
    data = r.json()
    raw_df = requests.get(api_url).json()

    # df = pd.DataFrame(raw_df['Time Series (Digital Currency Daily)']).T
    df = pd.DataFrame(raw_df['Time Series (Daily)']).T
    df = df.rename(
        columns={'1. open (USD)': 'open', '2. high (USD)': 'high', '3. low (USD)': 'low', '4. close (USD)': 'close',
                 '5. volume': 'volume'})

    for i in df.columns:
        df[i] = df[i].astype(float)
    df.index = pd.to_datetime(df.index)
    # df = df.iloc[::-1].drop(['1b. open (USD)', '2b. high (USD)', '3b. low (USD)', '4b. close (USD)', '6. market cap (USD)'],
    #      axis=1)
    if start_date:
        df = df[df.index >= start_date]

    # print(df)
    # print(df.values)  #affichage des donnees sans titres
    # print(df.at[, ])
    name = df.at['2022-02-17', '1. open']
    return render(request, 'hello.html', {'name' : name})
