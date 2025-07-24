from typing import List, Optional

from backend.models.schemas.schemas import (
    CategoryCreateSchema,
    CategorySchema,
    CategoryUpdateSchema,
)
from backend.models.tables.category import Category
from backend.services.conn import connection
from fastapi import HTTPException
from sqlalchemy import select


@connection
async def create_category(session, category_data: CategoryCreateSchema) -> CategorySchema:
    """Create a new category"""
    try:
        new_category = Category(**category_data.model_dump())
        session.add(new_category)
        await session.commit()
        await session.refresh(new_category)
        return CategorySchema.model_validate(new_category)
    except Exception as e:
        await session.rollback()
        raise HTTPException(status_code=400, detail=f"Error creating category: {str(e)}")


@connection
async def get_category(session, category_id: int) -> Optional[CategorySchema]:
    """Get category by ID"""
    category = await session.scalar(select(Category).where(Category.id == category_id))
    if not category:
        return None
    return CategorySchema.model_validate(category)


@connection
async def get_all_categories(session) -> List[CategorySchema]:
    """Get all categories"""
    result = await session.execute(select(Category).order_by(Category.id))
    categories = result.scalars().all()
    return [CategorySchema.model_validate(q) for q in categories]


@connection
async def update_category(session, category_id: int, category_data: CategoryUpdateSchema) -> Optional[CategorySchema]:
    """Update category by ID"""
    category = await session.scalar(select(Category).where(Category.id == category_id))
    if not category:
        return None

    update_data = category_data.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(category, field, value)

    await session.commit()
    await session.refresh(category)
    return CategorySchema.model_validate(category)


@connection
async def delete_category(session, category_id: int) -> bool:
    """Delete category by ID"""
    category = await session.scalar(select(Category).where(Category.id == category_id))
    if not category:
        return False

    await session.delete(category)
    await session.commit()
    return True
