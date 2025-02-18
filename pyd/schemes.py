from .base_models import *
from typing import List, Dict

class CountScheme(CountBase):
    ingredient: IngredientBase
    system_of_calc:System_of_calculationBase

class TranslationCategoryScheme(TranslationCategoryBase): #связь с языком
    lang:LangBase 
class TranslationMealtimeScheme(TranslationMealtimeBase):
    lang:LangBase
class TranslationIngredientScheme(TranslationIngredientBase):
    lang:LangBase 
class TranslationSysOfCalcScheme(TranslationSysOfCalcBase):
    lang:LangBase 
class TranslationRecipeScheme(TranslationRecipeBase):
    lang:LangBase 
class TranslationStepScheme(TranslationStepBase):
    lang:LangBase

class RecipeScheme(RecipeBase):
    translation_recipes:List[TranslationRecipeScheme]
    user:UserBase #связь с рецептами
    category:CategoryBase #связь с категориями
    mealtime:List[MealtimeBase] #связь с временем приёма пищи
    steps:List[StepBase]
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
