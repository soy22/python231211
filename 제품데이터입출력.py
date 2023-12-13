import sqlite3

class ProductDatabase:
    def __init__(self, db_name='products.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                price REAL NOT NULL
            )
        ''')
        self.conn.commit()

    def insert_product(self, product_id, product_name, price):
        self.cursor.execute('''
            INSERT INTO products (id, name, price)
            VALUES (?, ?, ?)
        ''', (product_id, product_name, price))
        self.conn.commit()

    def update_product(self, product_id, new_price):
        self.cursor.execute('''
            UPDATE products
            SET price = ?
            WHERE id = ?
        ''', (new_price, product_id))
        self.conn.commit()

    def delete_product(self, product_id):
        self.cursor.execute('''
            DELETE FROM products
            WHERE id = ?
        ''', (product_id,))
        self.conn.commit()

    def select_all_products(self):
        self.cursor.execute('''
            SELECT * FROM products
        ''')
        return self.cursor.fetchall()

    def close_connection(self):
        self.conn.close()

# 샘플 데이터 10개 삽입
db = ProductDatabase()
sample_data = [
    (1, 'Product1', 19.99),
    (2, 'Product2', 29.99),
    (3, 'Product3', 39.99),
    (4, 'Product4', 49.99),
    (5, 'Product5', 59.99),
    (6, 'Product6', 69.99),
    (7, 'Product7', 79.99),
    (8, 'Product8', 89.99),
    (9, 'Product9', 99.99),
    (10, 'Product10', 109.99),
]

for data in sample_data:
    db.insert_product(*data)

# 모든 제품 출력
all_products = db.select_all_products()
print("All Products:")
for product in all_products:
    print(product)

# 제품 업데이트
db.update_product(1, 24.99)

# 업데이트된 제품 출력
updated_product = db.select_all_products()
print("\nUpdated Product:")
for product in updated_product:
    print(product)

# 제품 삭제
db.delete_product(3)

# 삭제 후 제품 출력
remaining_products = db.select_all_products()
print("\nRemaining Products:")
for product in remaining_products:
    print(product)

# 연결 종료
db.close_connection()