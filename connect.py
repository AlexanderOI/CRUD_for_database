import sqlite3


class Connect:
    def __init__(self):
        self.database = sqlite3.connect('products.db')

    def show(self):
        cursor = self.database.cursor()
        cursor.execute('SELECT * FROM products')
        record = cursor.fetchall()
        cursor.close()
        return record

    def insert(self, name, price, category, quantity):
        cursor = self.database.cursor()
        sql = 'INSERT INTO products (name, price, category, quantity) VALUES (?, ?, ?, ?)'
        cursor.execute(sql, (name, price, category, quantity))
        self.database.commit()
        cursor.close()

    def delete(self, id_):
        cursor = self.database.cursor()
        sql = 'DELETE FROM products WHERE id = ?'
        cursor.execute(sql, (id_,))
        self.database.commit()
        cursor.close()

    def update(self, id_, name, price, category, quantity):
        cursor = self.database.cursor()
        sql = 'UPDATE products SET name = ?, price = ?, category = ?, quantity = ? WHERE id = ?'
        cursor.execute(sql, (name, price, category, quantity, id_))
        self.database.commit()
        cursor.close()

    def search(self, name):
        cursor = self.database.cursor()
        sql = 'SELECT * FROM products WHERE name = ?'
        cursor.execute(sql, (name,))
        register = cursor.fetchone()
        cursor.close()
        return register
