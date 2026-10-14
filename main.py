from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.api.v1.products import router as products_router
from app.core.database import Base, engine

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    await engine.dispose()

app = FastAPI(
    title="Product Catalog & Inventory API",
    version="1.0.0",
    lifespan=lifespan
)

app.include_router(products_router, prefix="/api/v1")