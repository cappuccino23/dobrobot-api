import psycopg2
from flask import Flask, request

from Dobrobot.pay_initiation import init_pay

from Dobrobot.result import add_res_data

app = Flask(__name__)

conn = psycopg2.connect(dbname='payments_dobrobot', user='dobrobot', password='dobrobot', host='localhost')


@app.route('/add', methods=['POST'])
def add():
    in_data = request.get_json()
    init_pay(in_data)

    return 'ok'


@app.route('/result', methods=['POST'])
def result():
    res_data = request.get_json()
    try:

        add_res_data(res_data)

        return {"code": 0, "message": "Операция успешно проведена"}

    except ValueError:
        return 'Not OK'


if __name__ == '__main__':
    app.run()
