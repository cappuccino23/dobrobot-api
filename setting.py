from configparser import ConfigParser

import psycopg2


config = ConfigParser()
read = config.read("settings.cfg")

secret_key = config.get('keys', 'SECRET_KEY')
api_key = config.get('keys', 'APIKEY')

conn = psycopg2.connect(dbname=config.get('db', 'dbname'), user=config.get('db', 'user'), password=config.get('db', 'password'), host=config.get('db', 'host'))