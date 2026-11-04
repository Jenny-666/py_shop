# 负责商品业务规则
import math

from repositories import product_repository as repo


# 查询所有商品
def get_products():
    return repo.get_all()


# 添加商品
def add_product(name, price, stock):

    if not name or not name.strip():
        raise ValueError("商品名称不能为空")

    if not math.isfinite(price) or price < 0:
        raise ValueError("商品价格不合法")

    if stock < 0:
        raise ValueError("商品库存不能为负数")

    return repo.create(name.strip(), price, stock)


# 修改商品价格
def change_price(product_id, price):

    if not math.isfinite(price) or price < 0:
        raise ValueError("商品价格不合法")

    success = repo.update_price(product_id, price)

    if not success:
        raise ValueError("商品不存在")


# 删除商品
def remove_product(product_id):

    success = repo.delete(product_id)

    if not success:
        raise ValueError("商品不存在")


# 销售商品
def sell_product(product_id, quantity):

    if quantity <= 0:
        raise ValueError("销售数量必须大于 0")

    product = repo.get_by_id(product_id)

    if product is None:
        raise ValueError("商品不存在")

    if quantity > product.stock:
        raise ValueError("库存不足")

    new_stock = product.stock - quantity

    success = repo.update_stock(product_id, new_stock)

    if not success:
        raise ValueError("库存更新失败")

    return new_stock
