import psycopg2

# Создаем соединение с нашей базой данных

conn = psycopg2.connect(dbname='payments_dobrobot', user='dobrobot', password='dobrobot', host='localhost')

cursor = conn.cursor()

# Делаем INSERT запрос к базе данных, используя обычный SQL-синтаксис
cursor.execute(
    "INSERT INTO public.payments (id, outer_id, status, stamp_date, description) "
    "VALUES"
    "(3, '1000000000000000003', 'auth', CURRENT_TIMESTAMP,'')"
)

# Если мы не просто читаем, но и вносим изменения в базу данных - необходимо сохранить транзакцию
conn.commit()

# Не забываем закрыть соединение с базой данных
conn.close()
