
from database.db import get_connection
from models.product import Product


# 查询全部商品
def get_all():
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM products")

        rows = cursor.fetchall()

        return [
            Product(
                row["id"],
                row["name"],
                row["price"],
                row["stock"]
            )
            for row in rows
        ]

    finally:
        conn.close()


# 根据 ID 查询商品
def get_by_id(product_id):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM products WHERE id = ?",
            (product_id,)
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Product(
            row["id"],
            row["name"],
            row["price"],
            row["stock"]
        )

    finally:
        conn.close()


# 添加商品
def create(name, price, stock):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO products (name, price, stock)
            VALUES (?, ?, ?)
            """,
            (name, price, stock)
        )

        conn.commit()

        return cursor.lastrowid

    finally:
        conn.close()


# 修改商品价格
def update_price(product_id, price):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE products SET price = ? WHERE id = ?",
            (price, product_id)
        )

        conn.commit()

        return cursor.rowcount > 0

    finally:
        conn.close()


# 删除商品
def delete(product_id):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            "DELETE FROM products WHERE id = ?",
            (product_id,)
        )

        conn.commit()

        return cursor.rowcount > 0

    finally:
        conn.close()


# 修改库存
def update_stock(product_id, stock):
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute(
            "UPDATE products SET stock = ? WHERE id = ?",
            (stock, product_id)
        )

        conn.commit()

        return cursor.rowcount > 0

    finally:
        conn.close()
