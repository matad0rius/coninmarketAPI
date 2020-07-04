import requests

key = ''

def get_price_history(**kwargs): # as many arguments as we want 

    url = 'https://api.tdameritrade.com/v1/marketdata/{}/pricehistory'.format(kwargs.get('symbol'))

    params = {}
    params.update({'apikey': key})

    for arg in kwargs:
        parameter = {arg: kwargs.get(arg)}
        params.update(parameter)

    return requests.get(url, params=params).json()

print(get_price_history(symbol='AAPL', period=1, periodType='day', frequencyType='minute'))
