import requests


default_currency = input().lower()
url = 'http://www.floatrates.com/daily/' + default_currency.lower() + '.json'
currencies_data = requests.get(url).json()
cache = {default_currency: {}}

if default_currency != "usd":
    cache[default_currency]['usd'] = dict.get(currencies_data, 'usd')['rate']
if default_currency != "eur":
    cache[default_currency]['eur'] = dict.get(currencies_data, 'eur')['rate']

while True:
    exchange_rate = None
    result = None
    currency_to = input().lower()
    if currency_to == "":
        break
    amount = float(input())
    in_cache = False
    appending = False
    print("Checking the cache...")
    for currencies in cache[default_currency]:
        if currencies == currency_to:
            exchange_rate = cache[default_currency][currency_to]
            result = round(amount * exchange_rate, 2)
            in_cache = True
            break
    if not in_cache:
        exchange_data = dict.get(currencies_data, currency_to)
        exchange_rate = exchange_data['rate']
        appending = True

    if in_cache:
        print("Oh! It is in the cache!")
    else:
        print("Sorry, but it is not in the cache!")
    if appending:
        cache[default_currency][currency_to] = exchange_rate
        result = round(amount * exchange_rate, 2)

    print("You received " + str(result) + " " + currency_to.upper() + ".")
