import json

from flask import Flask

from setting import conn

app = Flask(__name__)


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
    req_data = {"code": 0, "message": "Операция успешно проведена"}

    return 200, json.dumps(req_data)


def answer_ko():
    req_data = {"code": 500, "message": "Отказано в предоставлении услуги"}

    return 400, json.dumps(req_data)
