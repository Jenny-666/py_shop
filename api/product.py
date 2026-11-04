
from fastapi import APIRouter, HTTPException, status

from schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from services import product_service as service


# 创建路由
router = APIRouter(
    prefix="/api/products",
    tags=["商品管理"]
)


# 查询全部商品
@router.get("", response_model=list[ProductResponse])
def get_products():

    return service.get_products()


# 查询单个商品
@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int):

    try:
        return service.get_product(product_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# 添加商品
@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def add_product(product: ProductCreate):

    try:
        return service.add_product(
            product.name,
            product.price,
            product.stock
        )

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )


# 修改商品
@router.put("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate):

    try:
        return service.update_product(
            product_id,
            product.name,
            product.price,
            product.stock
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )


# 删除商品
@router.delete("/{product_id}")
def delete_product(product_id: int):

    try:
        service.delete_product(product_id)

        return {
            "message": "删除成功"
        }

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )
