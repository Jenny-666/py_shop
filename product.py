
class Product:

    # 初始化商品对象
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # 显示商品信息
    def show(self):
        print(
            f"名称：{self.name}，"
            f"价格：{self.price}，"
            f"库存：{self.stock}"
        )

    # 商品销售
    def sell(self, quantity):
        if quantity <= 0:
            print("销售数量必须大于 0")

        elif quantity > self.stock:
            print("库存不足")

        else:
            self.stock -= quantity
            print(f"销售成功，剩余库存：{self.stock}")

    # 将商品对象转换成字典
    def to_dict(self):
        return {
            "name": self.name,
            "price": self.price,
            "stock": self.stock
        }

    # 将字典转换成商品对象
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["price"],
            data["stock"]
        )
