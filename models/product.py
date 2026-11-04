
class Product:

    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    # 显示商品信息
    def show(self):
        print(
            f"编号：{self.id}，"
            f"名称：{self.name}，"
            f"价格：{self.price}，"
            f"库存：{self.stock}"
        )
