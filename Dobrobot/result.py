import json

from flask import Flask

from setting import conn

app = Flask(__name__)


def add_res_data(res_data):
    cursor = conn.cursor()

    exec_dict = {key: str(value) if callable(getattr(value, '__iter__', None)) else value for key, value in res_data.items()}

    print(exec_dict)

    query = "INSERT INTO public.result (method, pid, pay_type, status, code, params, credentials, pstamp, astamp, merc_data)" \
            "VALUES(%(method)s, %(id)s, %(pay_type)s, %(status)s, %(code)s, %(params)s, %(credentials)s, %(pstamp)s, %(astamp)s, %(merc_data)s)"

    cursor.execute(query, exec_dict)

    conn.commit()
    conn.close()

    return


def answer_ok():
    req_data = {"code": 0, "message": "Операция успешно проведена"}

    return 200, json.dumps(req_data)


def answer_ko():
    req_data = {"code": 500, "message": "Отказано в предоставлении услуги"}

    return 400, json.dumps(req_data)