import requests
from config import keys, headers, payload


class APIException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести одинаковые валюты{quote}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}')

        url = f"https://api.apilayer.com/currency_data/convert?to={quote_ticker}&from={base_ticker}&amount={amount}"

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()

        return result['result']
