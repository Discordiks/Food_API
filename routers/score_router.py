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
    prefix="/score",
    tags=["score"],
)

#получение рецептов с пользователями
@router.get('/', response_model=List[pyd.ScoreScheme])
async def get_scores(db:Session=Depends(get_db)):
    scores=db.query(models.Score).all()
    return scores

#лайк
@router.post('/like/{id_recipe}', response_model=pyd.ScoreScheme)
async def create_like(id_recipe:int, db:Session=Depends(get_db),payload:dict=Depends(auth_utils.auth_wrapper)):
    user_db = db.query(models.User).filter(models.User.name==payload.get("username")).first() #получаем пользователя
    recipe_db = db.query(models.Recipe).filter(models.Recipe.id==id_recipe).first() #находим рецепт, принадлежащий пользователю
    if not recipe_db:
        raise HTTPException(status_code=404, detail="Рецепт не найден!")
    score_db=db.query(models.Score).filter(models.Score.id_user==user_db.id).filter(models.Score.id_recipe==id_recipe).first() #получаем score
    if score_db:
        score_db.like=True
        score_db.dizlike=False
        db.commit()
    else:
        score_db=models.Score()
        score_db.user=user_db
        score_db.recipe=recipe_db
        score_db.like=True
        score_db.dizlike=False
        db.add(score_db)
        db.commit()
    return score_db

#дизлайк
@router.post('/dizlike/{id_recipe}', response_model=pyd.ScoreScheme)
async def create_dizlike(id_recipe:int, db:Session=Depends(get_db),payload:dict=Depends(auth_utils.auth_wrapper)):
    user_db = db.query(models.User).filter(models.User.name==payload.get("username")).first() #получаем пользователя
    recipe_db = db.query(models.Recipe).filter(models.Recipe.id==id_recipe).first() #находим рецепт, принадлежащий пользователю
    if not recipe_db:
        raise HTTPException(status_code=404, detail="Рецепт не найден!")
    score_db=db.query(models.Score).filter(models.Score.id_user==user_db.id).filter(models.Score.id_recipe==id_recipe).first() #получаем score
    if score_db:
        score_db.like=False
        score_db.dizlike=True
        db.commit()
    else:
        score_db=models.Score()
        score_db.user=user_db
        score_db.recipe=recipe_db
        score_db.like=False
        score_db.dizlike=True
        db.add(score_db)
        db.commit()
    return score_db

#нет никакой оценки
@router.delete('/no/{id_recipe}', response_model=pyd.ScoreScheme)
async def no_scores(id_recipe:int, db:Session=Depends(get_db),payload:dict=Depends(auth_utils.auth_wrapper)):
    user_db = db.query(models.User).filter(models.User.name==payload.get("username")).first() #получаем пользователя
    recipe_db = db.query(models.Recipe).filter(models.Recipe.id==id_recipe).first() #находим рецепт, принадлежащий пользователю
    if not recipe_db:
        raise HTTPException(status_code=404, detail="Рецепт не найден!")
    score_db=db.query(models.Score).filter(models.Score.id_user==user_db.id).filter(models.Score.id_recipe==id_recipe).first() #получаем score
    if not score_db:
        raise HTTPException(status_code=404, detail="Пользователь не поставил оценку этому рецепту")
    db.delete(score_db)
    db.commit()
    return "Пользователь не поставил оценку этому рецепту"

