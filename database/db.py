# 负责数据库连接和初始化
import sqlite3

# 数据库文件
DB_NAME = "shop.db"


# 获取数据库连接
def get_connection():
    conn = sqlite3.connect(DB_NAME)

    # 支持通过字段名称获取数据
    conn.row_factory = sqlite3.Row

    return conn


# 初始化数据库
def init_db():
    conn = get_connection()

    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL CHECK(price >= 0),
                stock INTEGER NOT NULL CHECK(stock >= 0)
            )
        """)

        conn.commit()

        print("数据库初始化成功！")

    finally:
        conn.close()
