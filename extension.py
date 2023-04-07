import requests
import json
from config import keys


class ConvertionExeption(Exception):
    pass

class Get_price:
    @staticmethod
    def convert( quote: str, base: str, amount: str):
        if quote == base:
            raise ConvertionExeption(f'Невозможно перевести одинаковые валюты <<{base}>>.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionExeption(f'Введена неправильная или несуществующая переводимая валюта <<{quote}>>')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionExeption(f'Введена неправильная или несуществующая валюта в которую требуется перевести <<{base}>>')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionExeption(f'Неправильно введено число <<{amount}>>')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]] * amount

        return total_base

