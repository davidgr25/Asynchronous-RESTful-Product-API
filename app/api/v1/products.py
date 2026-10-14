from typing import List, Optional
from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import get_db
from app.repositories.product_repository import ProductRepository
from app.schemas.product import (
    ProductCreate,
    ProductPartialUpdate,
    ProductResponse,
    ProductUpdate,
)
from app.services.product_service import ProductService

router = APIRouter(prefix="/products", tags=["Products"])

def get_product_service(session: AsyncSession = Depends(get_db)) -> ProductService:
    repository = ProductRepository(session)
    return ProductService(repository)

@router.post("/", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(
    payload: ProductCreate,
    service: ProductService = Depends(get_product_service)
):
    return await service.create_product(payload)

@router.get("/", response_model=List[ProductResponse], status_code=status.HTTP_200_OK)
async def list_products(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    name: Optional[str] = Query(None),
    service: ProductService = Depends(get_product_service)
):
    return await service.list_products(skip=skip, limit=limit, name=name)

@router.get("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def get_product(
    id: int,
    service: ProductService = Depends(get_product_service)
):
    return await service.get_product_by_id(id)

@router.put("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def replace_product(
    id: int,
    payload: ProductUpdate,
    service: ProductService = Depends(get_product_service)
):
    return await service.replace_product(id, payload)

@router.patch("/{id}", response_model=ProductResponse, status_code=status.HTTP_200_OK)
async def partial_update_product(
    id: int,
    payload: ProductPartialUpdate,
    service: ProductService = Depends(get_product_service)
):
    return await service.update_product_partial(id, payload)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_product(
    id: int,
    service: ProductService = Depends(get_product_service)
):
    await service.delete_product(id)