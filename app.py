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


@app.route('/', methods=['POST'])
def calculate():
    pass