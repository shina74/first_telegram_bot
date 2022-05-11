from get import *
from currency import *

class Smthn_wrong(Exception):
    pass

class try_():
    @staticmethod
    def convert(base,quote,amount):
        if base not in symbols_now:
            raise Smthn_wrong(f"К сожалению, мы не нашли такую валюту {base}. Проверьте правильность написания и посмотрите доступные валюты /values")

        if quote not in symbols_now:
            raise Smthn_wrong(f"К сожалению, мы не нашли такую валюту {quote}. Проверьте правильность написания и посмотрите доступные валюты /values")

        try:
            float(amount)
        except ValueError:
            raise Smthn_wrong(f'Мы не смогли обработать количество "{amount}"')

        if quote == base:
            raise Smthn_wrong(f'Цена {amount} {base} в {base} = {amount}')