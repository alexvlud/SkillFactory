import json
import requests
from config import keys

class APIException(Exception):
    pass

class CurrConverter:
    @staticmethod
    def get_price(base: str, quote: str, amount:str):

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{base}"')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту "{quote}"')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество "{amount}"')

        #if float(amount) < 0:
        #    raise APIException('Количество валюты отрицательное.')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={base_ticker}&tsyms={quote_ticker}')
        return json.loads(r.content)[keys[quote]]