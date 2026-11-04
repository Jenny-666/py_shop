目录 作用
main.py 接收用户输入、展示菜单和调用业务层
models 定义数据库模型  # 负责定义商品对象
api 定义 HTTP 接口
schemas 定义接口接收和返回的数据结构
services 处理业务逻辑  # 负责商品业务规则
repositories 执行数据库操作  # 负责所有商品数据库操作
database 连接数据库和初始化数据库  # 负责数据库连接和初始化
