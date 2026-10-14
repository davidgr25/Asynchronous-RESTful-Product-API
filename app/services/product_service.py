from typing import Optional, Sequence
from fastapi import HTTPException, status
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.schemas.product import ProductCreate, ProductPartialUpdate, ProductUpdate

class ProductService:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    async def create_product(self, data: ProductCreate) -> Product:
        existing = await self.repository.get_by_sku(data.sku)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Product with SKU '{data.sku}' already exists."
            )
        new_product = Product(**data.model_dump())
        return await self.repository.create(new_product)

    async def get_product_by_id(self, product_id: int) -> Product:
        product = await self.repository.get_by_id(product_id)
        if not product:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Product with ID {product_id} not found."
            )
        return product

    async def list_products(self, skip: int, limit: int, name: Optional[str]) -> Sequence[Product]:
        return await self.repository.get_all(skip=skip, limit=limit, name=name)

    async def replace_product(self, product_id: int, data: ProductUpdate) -> Product:
        product = await self.get_product_by_id(product_id)
        
        if data.sku != product.sku:
            existing_sku = await self.repository.get_by_sku(data.sku)
            if existing_sku:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Product with SKU '{data.sku}' already exists."
                )

        for key, value in data.model_dump().items():
            setattr(product, key, value)

        return await self.repository.update(product)

    async def update_product_partial(self, product_id: int, data: ProductPartialUpdate) -> Product:
        product = await self.get_product_by_id(product_id)
        update_data = data.model_dump(exclude_unset=True)

        if "sku" in update_data and update_data["sku"] != product.sku:
            existing_sku = await self.repository.get_by_sku(update_data["sku"])
            if existing_sku:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"Product with SKU '{update_data['sku']}' already exists."
                )

        for key, value in update_data.items():
            setattr(product, key, value)

        return await self.repository.update(product)

    async def delete_product(self, product_id: int) -> None:
        product = await self.get_product_by_id(product_id)
        await self.repository.delete(product)