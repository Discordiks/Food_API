from .base_models import *
from typing import List, Dict

class TranslationRecipeScheme(TranslationRecipeBase): #перевод названия рецепта
    lang:LangBase 

class TranslationCategoryScheme(TranslationCategoryBase): #перевод категорий
    lang:LangBase 
class CategoryScheme(CategoryBase):
    translation_categories:List[TranslationCategoryScheme]

class TranslationMealtimeScheme(TranslationMealtimeBase): #перевод времени приготовления
    lang:LangBase
class MealtimeScheme(MealtimeBase):
    translation_mealtimes:List[TranslationMealtimeScheme]

class TranslationStepScheme(TranslationStepBase): #перевод шагов
    lang:LangBase
class StepsScheme(StepBase):
    translation_steps:List[TranslationStepScheme]

class TranslationIngredientScheme(TranslationIngredientBase): #перевод ингредиентов
    lang:LangBase 
class IngredientScheme(IngredientBase):
    translation_ingredients:List[TranslationIngredientScheme]

class TranslationSysOfCalcScheme(TranslationSysOfCalcBase): #перевод системы исчисления
    lang:LangBase 
class SysOfCalcScheme(System_of_calculationBase):
    translation_sys_of_calcs:List[TranslationSysOfCalcScheme]

class CountScheme(CountBase): #перевод ингредиентов и системы исчисления
    ingredient: IngredientScheme
    system_of_calc: SysOfCalcScheme

class RecipeScheme(RecipeBase):
    translation_recipes:List[TranslationRecipeScheme]
    user:UserBase #связь с рецептами
    category:CategoryScheme #связь с категориями
    mealtime:List[MealtimeScheme] #связь с временем приёма пищи
    steps:List[StepsScheme]
    counts:List[CountScheme]
    likes:int
    dizlikes:int
    raiting:int

class Additional_photoScheme(Additional_photoBase):
    recipe_photo:RecipeBase #связь с рецептами

class StepScheme(StepBase):
    recipe:RecipeBase #связь с рецептами

class ScoreScheme(BaseModel):
    likes:int
    dislikes:int
    status_like:int
    status_dizlike:int

class UserScheme(UserBase):
    #user:UserBase 
    count_r:int
    raiting:int
