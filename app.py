import jsonschema
import requests
from flask import Flask, request
from jsonschema import validate

from Dobrobot.pay_initiation import init_pay

from Dobrobot.result import add_res_data, answer_ok, answer_ko

from setting import schema, headers

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"


@app.route('/add', methods=['POST'])
def add():
    in_data = request.get_json()

    try:
        validate(instance=in_data, schema=schema)
        # answer = {"message": "Запрос принят"}
        # requests.post(url_in, data=answer, headers=headers)
        init_pay(in_data)

        return

    except jsonschema.exceptions.ValidationError:

        return {"message": "неверный формат запроса"}


@app.route('/result', methods=['POST'])
def result():
    res_data = request.get_json()
    try:

        add_res_data(res_data)

        return answer_ok()

    except ValueError:

        return answer_ko()


if __name__ == "__main__":
    app.run()
