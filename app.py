from flask import Flask, render_template, request
import requests, json


app = Flask(__name__)

@app.route('/')
def form():
    url = "https://currency-converter18.p.rapidapi.com/api/v1/supportedCurrencies"

    headers = {
        "X-RapidAPI-Key": "d2d13630f3mshd03bcb7dad5af15p184ed1jsn68d86f77b783",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers)
    data = json.loads(response.text)
    currency_list = []
    for d in data:
        code = d['symbol']
        currency_list.append(code)
    
    return render_template('index.html', currency_list=currency_list)


@app.route('/calculate', methods=['POST'])
def calculate():
    currency_from = request.form.get('currency_from')
    currency_to = request.form.get('currency_to')
    amount = request.form.get('amount')

    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {"from":currency_from,"to":currency_to,"amount":amount}

    headers = {
        "X-RapidAPI-Key": "d2d13630f3mshd03bcb7dad5af15p184ed1jsn68d86f77b783",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = data['result']['convertedAmount']
    formatted = '{:,.2f}'.format(converted_amount)

    return render_template('index.html', formatted=formatted, amount=amount,
                           currency_from=currency_from, currency_to=currency_to)