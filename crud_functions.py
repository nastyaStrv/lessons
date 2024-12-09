import sqlite3


def initiate_db():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS Products (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      title TEXT NOT NULL,
                      description TEXT,
                      price INTEGER NOT NULL)''')
    connection.commit()
    connection.close()


def get_all_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Products")
    products = cursor.fetchall()
    connection.close()
    return products


def add_products():
    connection = sqlite3.connect('not_telegram.db')
    cursor = connection.cursor()

    for i in range(1, 5):
        cursor.execute("SELECT * FROM Products WHERE title = ?", (f'Продукт {i}',))
        product = cursor.fetchone()

        if product is None:
            cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                           (f'Продукт {i}', f'Описание {i}', i * 100))

    connection.commit()
    connection.close()
