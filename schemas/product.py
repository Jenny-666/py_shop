
from pydantic import BaseModel, Field


# 新增商品时接收的数据
class ProductCreate(BaseModel):

    name: str = Field(
        min_length=1,
        max_length=100,
        description="商品名称"
    )

    price: float = Field(
        ge=0,
        allow_inf_nan=False,
        description="商品价格"
    )

    stock: int = Field(
        ge=0,
        description="商品库存"
    )


# 修改商品时接收的数据
class ProductUpdate(BaseModel):

    name: str = Field(
        min_length=1,
        max_length=100
    )

    price: float = Field(ge=0)

    stock: int = Field(ge=0)


# 返回商品时使用的数据
class ProductResponse(BaseModel):

    id: int
    name: str
    price: float
    stock: int
