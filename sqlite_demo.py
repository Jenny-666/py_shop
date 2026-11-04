
import sqlite3


# 连接数据库
def connect_db():
    return sqlite3.connect("shop.db")


# 创建商品表
def create_table():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            price REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    conn.commit()
    conn.close()

    print("商品表创建成功！")


# 添加商品
def add_product(name, price, stock):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO products (name, price, stock)
        VALUES (?, ?, ?)
        """,
        (name, price, stock)
    )

    conn.commit()
    conn.close()

    print("商品添加成功！")


# 查询商品
def show_products():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    print("\n===== 商品列表 =====")

    for product in products:
        print(
            f"编号：{product[0]}，"
            f"名称：{product[1]}，"
            f"价格：{product[2]}，"
            f"库存：{product[3]}"
        )

    conn.close()


# 修改商品价格
def update_price(product_id, new_price):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE products SET price = ? WHERE id = ?",
        (new_price, product_id)
    )

    conn.commit()

    print("修改成功！" if cursor.rowcount else "商品不存在！")

    conn.close()


# 删除商品
def delete_product(product_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM products WHERE id = ?",
        (product_id,)
    )

    conn.commit()

    print("删除成功！" if cursor.rowcount else "商品不存在！")

    conn.close()


# 主程序
def main():
    create_table()

    while True:
        print("\n========== SQLite 商品管理 ==========")
        print("1. 添加商品")
        print("2. 查看商品")
        print("3. 修改商品价格")
        print("4. 删除商品")
        print("0. 退出")

        choice = input("请选择：")

        if choice == "1":
            name = input("商品名称：")
            price = float(input("商品价格："))
            stock = int(input("商品库存："))

            add_product(name, price, stock)

        elif choice == "2":
            show_products()

        elif choice == "3":
            product_id = int(input("商品编号："))
            new_price = float(input("新价格："))

            update_price(product_id, new_price)

        elif choice == "4":
            product_id = int(input("商品编号："))

            delete_product(product_id)

        elif choice == "0":
            print("退出系统！")
            break

        else:
            print("无效选择！")


if __name__ == "__main__":
    main()
