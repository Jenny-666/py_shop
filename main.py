
import json
import math

from product import Product


# ==============================
# 一、读取商品数据
# ==============================

def load_products():
    try:
        with open("products.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return [Product.from_dict(item) for item in data]

    except FileNotFoundError:
        print("商品数据文件不存在，将创建空商品列表")
        return []

    except json.JSONDecodeError:
        print("商品数据文件格式错误，请检查 products.json")
        return []

    except OSError as e:
        print(f"读取文件失败：{e}")
        return []


# ==============================
# 二、保存商品数据
# ==============================

def save_products():
    data = [product.to_dict() for product in products]

    try:
        with open("products.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    except OSError as e:
        print(f"保存文件失败：{e}")


# ==============================
# 三、输入校验
# ==============================

# 获取非负价格
def get_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))

            if not math.isfinite(value):
                print("请输入正常的有限数字")
                continue

            if value < 0:
                print("不能输入负数")
                continue

            return value

        except ValueError:
            print("请输入有效数字")


# 获取非负整数
def get_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))

            if value < 0:
                print("不能输入负数")
                continue

            return value

        except ValueError:
            print("请输入整数")


# ==============================
# 四、初始化商品列表
# ==============================

products = load_products()


# ==============================
# 五、查看商品
# ==============================

def show_products():
    print("\n===== 商品列表 =====")

    if not products:
        print("暂无商品")
        return

    for product in products:
        product.show()


# ==============================
# 六、添加商品
# ==============================

def add_product():
    name = input("商品名称：").strip()

    if not name:
        print("商品名称不能为空")
        return

    price = get_non_negative_float("商品价格：")
    stock = get_non_negative_int("商品库存：")

    products.append(Product(name, price, stock))

    save_products()

    print("商品添加成功！")


# ==============================
# 七、删除商品
# ==============================

def delete_product():
    name = input("请输入要删除的商品名称：").strip()

    for product in products:
        if product.name == name:
            products.remove(product)

            save_products()

            print("删除成功！")
            return

    print("商品不存在！")


# ==============================
# 八、修改商品价格
# ==============================

def update_price():
    name = input("请输入商品名称：").strip()

    for product in products:
        if product.name == name:
            new_price = get_non_negative_float("请输入新价格：")

            product.price = new_price

            save_products()

            print("修改成功！")
            return

    print("商品不存在！")


# ==============================
# 九、商品销售
# ==============================

def sell_product():
    name = input("请输入商品名称：").strip()

    for product in products:
        if product.name == name:
            quantity = get_non_negative_int("请输入销售数量：")

            if quantity == 0:
                print("销售数量必须大于 0")
                return

            old_stock = product.stock

            product.sell(quantity)

            if product.stock != old_stock:
                save_products()

            return

    print("商品不存在！")


# ==============================
# 十、主菜单
# ==============================

def main():
    while True:
        print("\n========== 商品管理系统 ==========")
        print("1. 查看商品")
        print("2. 添加商品")
        print("3. 删除商品")
        print("4. 修改商品价格")
        print("5. 商品销售")
        print("0. 退出系统")

        choice = input("请选择功能：")

        if choice == "1":
            show_products()

        elif choice == "2":
            add_product()

        elif choice == "3":
            delete_product()

        elif choice == "4":
            update_price()

        elif choice == "5":
            sell_product()

        elif choice == "0":
            print("感谢使用！")
            break

        else:
            print("无效选择，请重新输入！")


# ==============================
# 十一、程序入口
# ==============================

if __name__ == "__main__":
    main()
