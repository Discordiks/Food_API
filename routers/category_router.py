from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models
from database import get_db
import pyd
#модули для JWT токена
import auth_utils
from config import TokenInfo

router = APIRouter(
    prefix="/category",
    tags=["category"],
)

#получение списка категорий
@router.get('/', response_model=List[pyd.CategoryScheme])
async def get_categorys(lang_code:str,db:Session=Depends(get_db)):
    categorys=db.query(models.Category).all()
    if lang_code == "ru" or lang_code == "" or lang_code == None:
        return categorys
    if lang_code == "en" or lang_code == "fr":
        for category in categorys:
            for code in category.translation_categories:
                if code.lang.code == lang_code:
                    category.name = code.text
        return categorys

#добавление категории
@router.post('/', response_model=pyd.CategoryBase)
async def create_categorys(category_input:pyd.CategoryCreate, db:Session=Depends(get_db),payload:dict=Depends(auth_utils.auth_wrapper)):
    category_db=models.Category()
    category_db.name=category_input.name
    db.add(category_db)
    db.commit()
    return category_db

#редактирование категории
@router.put('/{category_id}', response_model=pyd.CategoryBase)
async def update_categorys(category_id:int, category_input:pyd.CategoryBase, db:Session=Depends(get_db),payload:dict=Depends(auth_utils.auth_wrapper)):
    category_db=db.query(models.Category).filter(models.Category.id==category_id).first()
    if not category_db:
        raise HTTPException(status_code=404, detail="Категория не найдена!")
    category_db.name=category_input.name
    db.commit()
    return category_db

#удаление категории
@router.delete('/{category_id}')
async def delete_categorys(category_id:int, db:Session=Depends(get_db),payload:dict=Depends(auth_utils.auth_wrapper)):
    category_db=db.query(models.Category).filter(models.Category.id==category_id).first()
    if not category_db:
        raise HTTPException(status_code=404, detail="Категория не найдена!")
    db.delete(category_db)
    #удаление рецепта
    db.query(models.Recipe).filter(models.Recipe.id_category==category_id).delete()
    db.commit()
    return "Удаление категории прошло успешно!"