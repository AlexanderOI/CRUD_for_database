import sqlite3
import random

data_base = sqlite3.connect('products.db')

cursor = data_base.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL,
        category TEXT NOT NULL,
        quantity INTEGER NOT NULL
    )
''')

products = [
    ('Manzanas', 2.99, 'Frutas', random.randint(5, 20)),
    ('Leche', 3.49, 'Lácteos', random.randint(5, 20)),
    ('Pan integral', 2.99, 'Panadería', random.randint(5, 20)),
    ('Pollo', 5.99, 'Carnes', random.randint(5, 20)),
    ('Pasta', 1.99, 'Alimentos secos', random.randint(5, 20)),
    ('Huevos', 2.49, 'Lácteos', random.randint(5, 20)),
    ('Arroz', 2.29, 'Alimentos secos', random.randint(5, 20)),
    ('Aceite de oliva', 4.99, 'Aceites', random.randint(5, 20)),
    ('Detergente para ropa', 7.99, 'Limpieza', random.randint(5, 20)),
    ('Yogur', 1.29, 'Lácteos', random.randint(5, 20))
]

cursor.executemany('INSERT INTO products(name, price, category,  quantity) VALUES (?, ?, ?, ?)', products)

data_base.commit()
data_base.close()