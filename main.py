# 负责接收用户输入、展示菜单和调用业务层
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database.db import init_db
from api.product import router as product_router


# 应用生命周期
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 服务启动时执行
    init_db()

    yield

    # 服务关闭时执行
    print("商品管理 API 已关闭")


# 创建 FastAPI 应用
app = FastAPI(
    title="Python 商品管理系统",
    description="使用 FastAPI + SQLite 开发的商品管理 API",
    version="1.0.0",
    lifespan=lifespan
)

# 配置跨域
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# 注册商品路由
app.include_router(product_router)


# 首页
@app.get("/")
def home():
    return {
        "message": "Python 商品管理系统 API 已启动"
    }


# import math

# from database.db import init_db
# from services import product_service as service


# # 输入非负整数
# def get_int(prompt):
#     while True:
#         try:
#             value = int(input(prompt))

#             if value < 0:
#                 print("不能输入负数")
#                 continue

#             return value

#         except ValueError:
#             print("请输入整数")


# # 输入非负价格
# def get_price(prompt):
#     while True:
#         try:
#             value = float(input(prompt))

#             if not math.isfinite(value) or value < 0:
#                 print("请输入合法的非负价格")
#                 continue

#             return value

#         except ValueError:
#             print("请输入有效数字")


# # 查看商品
# def show_products():
#     products = service.get_products()

#     print("\n===== 商品列表 =====")

#     if not products:
#         print("暂无商品")
#         return

#     for product in products:
#         product.show()


# # 添加商品
# def add_product():
#     name = input("商品名称：").strip()

#     price = get_price("商品价格：")
#     stock = get_int("商品库存：")

#     try:
#         product_id = service.add_product(name, price, stock)

#         print(f"添加成功，商品编号：{product_id}")

#     except ValueError as e:
#         print(f"添加失败：{e}")


# # 修改商品价格
# def update_price():
#     product_id = get_int("请输入商品编号：")
#     price = get_price("请输入新价格：")

#     try:
#         service.change_price(product_id, price)

#         print("修改成功！")

#     except ValueError as e:
#         print(f"修改失败：{e}")


# # 删除商品
# def delete_product():
#     product_id = get_int("请输入商品编号：")

#     try:
#         service.remove_product(product_id)

#         print("删除成功！")

#     except ValueError as e:
#         print(f"删除失败：{e}")


# # 销售商品
# def sell_product():
#     product_id = get_int("请输入商品编号：")
#     quantity = get_int("请输入销售数量：")

#     try:
#         stock = service.sell_product(product_id, quantity)

#         print(f"销售成功，剩余库存：{stock}")

#     except ValueError as e:
#         print(f"销售失败：{e}")


# # 主菜单
# def main():

#     init_db()

#     while True:
#         print("\n========== 商品管理系统 ==========")
#         print("1. 查看商品")
#         print("2. 添加商品")
#         print("3. 修改商品价格")
#         print("4. 删除商品")
#         print("5. 商品销售")
#         print("0. 退出系统")

#         choice = input("请选择功能：")

#         if choice == "1":
#             show_products()

#         elif choice == "2":
#             add_product()

#         elif choice == "3":
#             update_price()

#         elif choice == "4":
#             delete_product()

#         elif choice == "5":
#             sell_product()

#         elif choice == "0":
#             print("感谢使用！")
#             break

#         else:
#             print("无效选择！")


# if __name__ == "__main__":
#     main()
