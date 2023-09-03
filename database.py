import sqlite3
import random

data_base = sqlite3.connect('products.db')

cursor = data_base.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        category TEXT NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

products = [
    ('Manzanas',  'Frutas', 2.99, random.randint(5, 20)),
    ('Leche',  'Lácteos', 3.49,  random.randint(5, 20)),
    ('Pan integral',  'Panadería', 2.99, random.randint(5, 20)),
    ('Pollo',  'Carnes', 5.99, random.randint(5, 20)),
    ('Pasta',  'Alimentos secos', 1.99, random.randint(5, 20)),
    ('Huevos',  'Lácteos', 2.49, random.randint(5, 20)),
    ('Arroz',  'Alimentos secos', 2.29, random.randint(5, 20)),
    ('Aceite de oliva', 'Aceites',4.99, random.randint(5, 20)),
    ('Detergente', 'Limpieza', 7.99, random.randint(5, 20)),
    ('Yogur',  'Lácteos', 1.29, random.randint(5, 20))
]

cursor.executemany('INSERT INTO products(name, category, price, quantity) VALUES (?, ?, ?, ?)', products)

data_base.commit()
data_base.close()