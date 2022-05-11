def get_price(base,quote,amount):
    import requests
    import json

    url = f"https://api.apilayer.com/exchangerates_data/convert?to={quote}&from={base}&amount={amount}"

    payload = {}
    headers = {
        "apikey": "h8F76tyV3cZ74IIz744NoOOOy8QcSeum"
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    status_code = response.status_code
    result = json.loads(response.content)
    return result['result']
