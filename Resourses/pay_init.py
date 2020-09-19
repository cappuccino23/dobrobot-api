import psycopg2
import requests
import hashlib
import hmac
import json

api_key = 'ds9qKLc8lkl91oM8O71'
secret_key = 'testdobrobot'

conn = psycopg2.connect(dbname='payments_dobrobot', user='dobrobot', password='dobrobot', host='localhost')

req_data = json.dumps(
    {
    "method": "form",
    "pay_type": "card",
    "client_id": "hp1L18kmOWVegdka30",
    "params":
        {
            "phone": "79261112233",
            "email": "user@example.com",
            "account": "test",
            "sum": 15000,
            "merc_email": "merc@example.com",
            "details": "Оплата заказа №123",
            "address": "Москва"
        },
    "merc_data": "Random information"
})

sign = hmac.new(bytearray(secret_key, 'utf-8'), bytearray(req_data, 'utf-8'), digestmod=hashlib.sha256).hexdigest()

headers = {"Content-type": "application/json"}
url = ' https://demo-api2.inplat.ru/?api_key={0}&sign={1}'.format(api_key, sign)
r = requests.post(url, data=req_data, headers=headers)

rec_json = r.json()
print(rec_json)
