from typing import List

import backend.services.requests.category as rq
from backend.models.schemas.schemas import (
    CategoryCreateSchema,
    CategorySchema,
    CategoryUpdateSchema,
)
from fastapi import APIRouter, HTTPException, Path

router = APIRouter(prefix="/api/categories", tags=["Categories"])


@router.post("/", response_model=CategorySchema, status_code=201)
async def create_category(category_data: CategoryCreateSchema):
    return await rq.create_category(category_data)


@router.get("/", response_model=List[CategorySchema])
async def get_all_categories():
    return await rq.get_all_categories()



@router.get("/{category_id}", response_model=CategorySchema)
async def get_category(category_id: int = Path(..., description="Category ID")):
    category = await rq.get_category(category_id)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.put("/{category_id}", response_model=CategorySchema)
async def update_category(category_id: int, category_data: CategoryUpdateSchema):
    category = await rq.update_category(category_id, category_data)
    if not category:
        raise HTTPException(status_code=404, detail="Category not found")
    return category


@router.delete("/{category_id}")
async def delete_category(category_id: int):
    success = await rq.delete_category(category_id)
    if not success:
        raise HTTPException(status_code=404, detail="Category not found")
    return {"message": "Category deleted successfully"}
