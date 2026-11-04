
from fastapi import FastAPI

# 创建 FastAPI 应用
app = FastAPI()


# 首页接口
@app.get("/")
def home():
    return {
        "message": "欢迎来到 Python 后端系统"
    }


# 查询商品接口
@app.get("/products")
def get_products():
    return {
        "code": 200,
        "message": "查询成功",
        "data": [
            {
                "id": 1,
                "name": "无线鼠标",
                "price": 89.9,
                "stock": 100
            },
            {
                "id": 2,
                "name": "机械键盘",
                "price": 299,
                "stock": 50
            }
        ]
    }
