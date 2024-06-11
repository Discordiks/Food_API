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

#функция подсчёта лайков
def likes_recipes(recipe,db:Session=Depends(get_db)):
    recipes_likes=db.query(models.Score).filter(models.Score.id_recipe==recipe).filter(models.Score.like==True).all()
    likes = recipes_likes.__len__()
    return likes

#функция подсчёта дизлайков
def dizlikes_recipes(recipe,db:Session=Depends(get_db)):
    recipes_dizlikes=db.query(models.Score).filter(models.Score.id_recipe==recipe).filter(models.Score.dizlike==True).all()
    dizlikes = recipes_dizlikes.__len__()
    return dizlikes

#функция добавления рецептам лайков и дизлайков
def for_recipes(recipe_db,db:Session=Depends(get_db)):
    for recipe in recipe_db:
        recipe.likes=likes_recipes(recipe.id,db)
        recipe.dizlikes=dizlikes_recipes(recipe.id,db)
    return recipe_db

#получение рецептов с пользователями
@router.get('/', response_model=List[pyd.ScoreScheme])
async def get_scores(db:Session=Depends(get_db)):
    scores=db.query(models.Score).all()
    return scores

#лайк
@router.post('/like/{id_recipe}')
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
    recipe_db.likes=likes_recipes(recipe_db.id,db)
    recipe_db.dizlikes=dizlikes_recipes(recipe_db.id,db)
    return recipe_db.likes

#дизлайк
@router.post('/dizlike/{id_recipe}')
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
    recipe_db.likes=likes_recipes(recipe_db.id,db)
    recipe_db.dizlikes=dizlikes_recipes(recipe_db.id,db)
    return recipe_db.dizlikes

#нет никакой оценки
@router.delete('/no/{id_recipe}')
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

#проверка на лайки у определённого рецепта
@router.get('/likes/{id_recipe}')
async def get_likes_user(id_recipe:int, db:Session=Depends(get_db),payload:dict=Depends(auth_utils.auth_wrapper)):
    user_db = db.query(models.User).filter(models.User.name==payload.get("username")).first() #получаем пользователя
    recipe_db = db.query(models.Recipe).filter(models.Recipe.id==id_recipe).first() #находим рецепт, принадлежащий пользователю
    if not recipe_db:
        raise HTTPException(status_code=404, detail="Рецепт не найден!")
    recipe_db.likes=likes_recipes(recipe_db.id,db)
    recipe_db.dizlikes=dizlikes_recipes(recipe_db.id,db)
    score_db=db.query(models.Score).filter(models.Score.id_user==user_db.id).filter(models.Score.id_recipe==id_recipe).filter(models.Score.like==True).first() #получаем score
    if not score_db:
        raise HTTPException(status_code=404, detail=False)
    return True

#проверка на дизлайки у определённого рецепта
@router.get('/dizlikes/{id_recipe}')
async def get_dizlikes_user(id_recipe:int, db:Session=Depends(get_db),payload:dict=Depends(auth_utils.auth_wrapper)):
    user_db = db.query(models.User).filter(models.User.name==payload.get("username")).first() #получаем пользователя
    recipe_db = db.query(models.Recipe).filter(models.Recipe.id==id_recipe).first() #находим рецепт, принадлежащий пользователю
    if not recipe_db:
        raise HTTPException(status_code=404, detail="Рецепт не найден!")
    recipe_db.likes=likes_recipes(recipe_db.id,db)
    recipe_db.dizlikes=dizlikes_recipes(recipe_db.id,db)
    score_db=db.query(models.Score).filter(models.Score.id_user==user_db.id).filter(models.Score.id_recipe==id_recipe).filter(models.Score.dizlike==True).first() #получаем score
    if not score_db:
        raise HTTPException(status_code=404, detail=False)
    return True