# 负责商品业务规则
import math

from repositories import product_repository as repo


# 查询全部商品
def get_products():
    return repo.get_all()


# 查询指定商品
def get_product(product_id):

    product = repo.get_by_id(product_id)

    if product is None:
        raise ValueError("商品不存在")

    return product


# 添加商品
def add_product(name, price, stock):

    name = name.strip()

    if not name:
        raise ValueError("商品名称不能为空")

    if not math.isfinite(price) or price < 0:
        raise ValueError("商品价格不合法")

    if stock < 0:
        raise ValueError("商品库存不能为负数")

    return repo.create(name, price, stock)


# 修改商品
def update_product(product_id, name, price, stock):

    name = name.strip()

    if not name:
        raise ValueError("商品名称不能为空")

    if not math.isfinite(price) or price < 0:
        raise ValueError("商品价格不合法")

    if stock < 0:
        raise ValueError("商品库存不能为负数")

    product = repo.update(
        product_id,
        name,
        price,
        stock
    )

    if product is None:
        raise ValueError("商品不存在")

    return product


# 删除商品
def delete_product(product_id):

    success = repo.delete(product_id)

    if not success:
        raise ValueError("商品不存在")
