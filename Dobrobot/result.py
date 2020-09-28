import hashlib
import hmac
import json

import psycopg2
import requests
from flask import Flask

app = Flask(__name__)

api_key = 'ds9qKLc8lkl91oM8O71'
secret_key = 'testdobrobot'

conn = psycopg2.connect(dbname='payments_dobrobot', user='dobrobot', password='dobrobot', host='localhost')


def add_res_data(res_data):
    cursor = conn.cursor()

    query = "INSERT INTO public.result (method, pid, pay_type, status, code, params, credentials, pstamp, astamp, merc_data)" \
            "VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING id"

    cursor.execute(query, (tuple(str(value) if isinstance(value, dict) else value for value in res_data.values())))

    add_id = cursor.fetchone()

    conn.commit()
    conn.close()

    return add_id


def answer_ok():
    req_data = json.dumps(
        {
            "code": 0,
            "message": "Операция успешно проведена"
        })

    sign = hmac.new(bytearray(secret_key, 'utf-8'), bytearray(req_data, 'utf-8'),
                    digestmod=hashlib.sha256).hexdigest()
    headers = {"Content-type": "application/json"}
    url = ' https://demo-api2.inplat.ru/?api_key={0}&sign={1}'.format(api_key, sign)
    answer = requests.get(url, params=req_data, headers=headers)

    return answer
