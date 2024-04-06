# Приложение ВЫДАЧА КРЕДИТОВ для некоторой организации. БД должна
# содержать таблицу Клиент со следующей структурой записи: ФИО клиента, ФИО
# сотрудника банка, срок кредита, процент кредита, сумма кредита.

import sqlite3

conn = sqlite3.connect('base.db')

with conn:
    cur = conn.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS clients("
        "id INTEGER PRIMARY KEY,"
        "fio VARCHAR(100),"
        "employee_fio VARCHAR(100),"
        "loan_period INTEGER,"
        "loan_percent INTEGER,"
        "loan_sum INTEGER"
        ")"
    )

with conn:
    cur = conn.cursor()
    cur.execute("DELETE FROM clients")
    cur.executemany("INSERT INTO clients VAlUES(NULL,?,?,?,?,?)", [
        ('Иванов И. И.', 'Петров П. П.', 1, 15, 500_000),
        ('Смирнов А. С.', 'Петров П. П.', 2, 10, 200_000),
        ('Козлов И. С.', 'Сидоров П. П.', 5, 12, 700_000),
        ('Соколов Ф. К.', 'Петров П. П.', 2, 13, 550_000),
        ('Васильев А. И.', 'Сидоров П. П.', 10, 15, 900_000),
        ('Кузнецов С. И.', 'Петров П. П.', 8, 15, 100_000),
        ('Лебедева Е. К.', 'Петров П. П.', 30, 15, 10_000_000),
        ('Николаев А. И.', 'Петров П. П.', 7, 5, 200_000),
        ('Птенцов Г. К.', 'Сидоров П. П.', 9, 15, 300_000),
        ('Иванова А. Ф.', 'Сидоров П. П.', 3, 5, 400_000),
    ])

with conn:
    cur = conn.cursor()
    print(*cur.execute('SELECT * FROM clients WHERE employee_fio = "Сидоров П. П." ORDER BY id DESC').fetchall(), sep='\n', end='\n\n')
    print(*cur.execute('SELECT * FROM clients WHERE loan_sum >= 500000').fetchall(), sep='\n', end='\n\n')
    print(*cur.execute('SELECT employee_fio, COUNT(*) FROM clients GROUP BY employee_fio').fetchall(), sep='\n', end='\n\n')

with conn:
    cur = conn.cursor()
    cur.execute('DELETE FROM clients WHERE fio = ?', ('Иванова А. Ф.',))
    cur.execute('DELETE FROM clients WHERE loan_sum = (SELECT loan_sum FROM clients ORDER BY loan_sum DESC LIMIT 1)')
    cur.execute('DELETE FROM clients WHERE loan_period = 1')

with conn:
    cur = conn.cursor()
    cur.execute('UPDATE clients SET employee_fio = ? WHERE loan_period = ?', ('Сидоров П. П.', 30))
    cur.execute('UPDATE clients SET loan_period = ? WHERE fio = ?', (3, 'Васильев А. И.'))
    cur.execute('UPDATE clients SET loan_percent = 10 WHERE loan_percent = 5')

with conn:
    cur = conn.cursor()
    print(*cur.execute('SELECT * FROM clients').fetchall(), sep='\n')
