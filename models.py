from sqlalchemy import Table, Boolean, Column, ForeignKey, Integer, String, TIMESTAMP, DateTime, LargeBinary
from sqlalchemy.orm import Mapped, mapped_column, relationship #связь между таблицами
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_utils import EmailType, URLType
from sqlalchemy.sql import func

#from sqlalchemy_imageattach.entity import Image, image_attachment #библиотека для изображений

from database import Base

Mealtime_recipes=Table('mealtime_recipe', Base.metadata, #таблица, связывающая время приготовления еды и рецепты
               Column('id', Integer, primary_key=True),           
               Column('id_mealtime', ForeignKey('mealtimes.id'), nullable=False, default=1),
               Column('id_recipe', ForeignKey('recipes.id'), nullable=False, default=1))

class User(Base): #пользователи
    __tablename__ = "users"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False, unique=True)
    mail = Column(EmailType, nullable=False, unique=True)
    img_avatar = Column(String(255), nullable=False, default="recipe/files/food.png") #фото по умолчанию есть всегда
    password = Column(String(255), nullable=False)
    mailing = Column(Boolean, nullable=False, default=False)
    created_at=Column(TIMESTAMP(timezone=False), 
                        server_default=func.now())
    email_verify=Column(Boolean(),nullable=False,
                        default=False)
    email_verify_code=Column(String(255), nullable=True, unique=True)
    token_phone=Column(String(500)) #на деле должен быть уникальным

class Recipe(Base): #рецепты
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False)
    face_img = Column(String(255), nullable=False, default="recipe/files/food.png") #фото обязательно
    id_category = Column(Integer, ForeignKey("categories.id", ondelete="CASCADE"), nullable=False, default=1) #внешний ключ
    id_user = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, default=1) #внешний ключ
    created_at=Column(TIMESTAMP(timezone=False), 
                        server_default=func.now())
    cooking_time=Column(Integer, nullable=False)
    views=Column(Integer, nullable=False,default=0)
    published=Column(Boolean, nullable=False,default=0) #публикация

    user=relationship("User", backref="recipes") #обратная связь
    category=relationship("Category", backref="recipes") #обратная связь
    mealtime=relationship("Mealtime", secondary='mealtime_recipe', backref='recipes', order_by="Mealtime.id.asc()") #время приготовления

    steps: Mapped[list["Step"]]  = relationship(
        #back_populates="recipes",
        primaryjoin="and_(Recipe.id == Step.id_recipe)",
        order_by="Step.number.asc()"
        )
    counts: Mapped[list["Count"]] = relationship(
        #back_populates="recipes",
        primaryjoin="and_(Recipe.id == Count.id_recipe)"
        )

class Ingredient(Base): #ингредиенты
    __tablename__ = "ingredients"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False)

class System_of_calculation(Base): #система исчисления
    __tablename__ = "system_of_calculations"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False)

    #translation_sys: Mapped[list["TranslationSysOfCalc"]]  = relationship(
        #back_populates="recipes",
    #    primaryjoin="and_(System_of_calculation.id == TranslationSysOfCalc.id_sys_of_calc)"
    #    )

class Category(Base): #категории еды
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False)

class Mealtime(Base): #время приёма пищи
    __tablename__ = "mealtimes"

    id = Column(Integer, primary_key=True) #первичный ключ
    name = Column(String(255), nullable=False)

class Additional_photo(Base): #дополнительные фото
    __tablename__ = "additional_photos"

    id = Column(Integer, primary_key=True) #первичный ключ
    img = Column(String(255), nullable=False, default="recipe/files/food.png") #фото обязательно
    id_recipe = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False, default=1) #внешний ключ

    recipe_photo=relationship("Recipe", backref="additional_photos") #обратная связь

class Step(Base): #шаги рецепта
    __tablename__ = "steps"

    id = Column(Integer, primary_key=True) #первичный ключ
    number = Column(Integer, default=1) 
    info = Column(String(255), nullable=False)
    id_recipe = Column(Integer, ForeignKey("recipes.id", ondelete="CASCADE"), nullable=False, default=1) #внешний ключ

    #recipe=relationship("Recipe", backref="steps") #обратная связь #overlaps="steps"
    recipe: Mapped["Recipe"] = relationship(back_populates="steps")

class Count(Base): #таблица, связывающая ингредиенты и рецепты
    __tablename__ = "counts"

    id = Column(Integer, primary_key=True)          
    id_recipe = Column(Integer, ForeignKey('recipes.id'), nullable=False, default=1)
    id_ingredient = Column(Integer, ForeignKey('ingredients.id'), nullable=False, default=1)
    count = Column(Integer, nullable=False, default=1)
    id_system_of_calc = Column(Integer, ForeignKey('system_of_calculations.id'), nullable=False, default=1)

    recipe: Mapped["Recipe"] = relationship(back_populates='counts')
    ingredient: Mapped["Ingredient"] = relationship(backref='counts')
    system_of_calc: Mapped["System_of_calculation"] = relationship( backref='counts') #система исчисления

class Score(Base): #таблица лайков и дизлайков
    __tablename__ = "scores"
    id = Column(Integer, primary_key=True)    
    id_user = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False, default=1)
    id_recipe = Column(Integer, ForeignKey('recipes.id', ondelete="CASCADE"), nullable=False, default=1)
    like = Column(Boolean, nullable=False, default=False)
    dizlike = Column(Boolean, nullable=False, default=False)

    user: Mapped["User"] = relationship(backref='scores')
    recipe: Mapped["Recipe"] = relationship(backref='scores')

class Lang(Base):
    __tablename__ = "langs"
    id = Column(Integer, primary_key=True)    
    name = Column(String(255), nullable=False)
    code = Column(String(255), nullable=False)

class TranslationCategory(Base):
    __tablename__ = "translation_categories"
    id = Column(Integer, primary_key=True)
    id_category = Column(Integer, ForeignKey('categories.id', ondelete="CASCADE"), nullable=False, default=1)
    id_lang = Column(Integer, ForeignKey('langs.id', ondelete="CASCADE"), nullable=False, default=1)
    text = Column(String(255), nullable=False)

    category: Mapped["Category"] = relationship(backref='translation_categories')
    lang: Mapped["Lang"] = relationship(backref='translation_categories')

class TranslationMealtime(Base):
    __tablename__ = "translation_mealtimes"
    id = Column(Integer, primary_key=True)
    id_mealtime = Column(Integer, ForeignKey('mealtimes.id', ondelete="CASCADE"), nullable=False, default=1)
    id_lang = Column(Integer, ForeignKey('langs.id', ondelete="CASCADE"), nullable=False, default=1)
    text = Column(String(255), nullable=False)

    mealtime: Mapped["Mealtime"] = relationship(backref='translation_mealtimes')
    lang: Mapped["Lang"] = relationship(backref='translation_mealtimes')

class TranslationIngredient(Base):
    __tablename__ = "translation_ingredients"
    id = Column(Integer, primary_key=True)
    id_ingredient = Column(Integer, ForeignKey('ingredients.id', ondelete="CASCADE"), nullable=False, default=1)
    id_lang = Column(Integer, ForeignKey('langs.id', ondelete="CASCADE"), nullable=False, default=1)
    text = Column(String(255), nullable=False)

    ingredient: Mapped["Ingredient"] = relationship(backref='translation_ingredients')
    lang: Mapped["Lang"] = relationship(backref='translation_ingredients')

class TranslationSysOfCalc(Base):
    __tablename__ = "translation_sys_of_calcs"
    id = Column(Integer, primary_key=True)
    id_sys_of_calc = Column(Integer, ForeignKey('system_of_calculations.id', ondelete="CASCADE"), nullable=False, default=1)
    id_lang = Column(Integer, ForeignKey('langs.id', ondelete="CASCADE"), nullable=False, default=1)
    text = Column(String(255), nullable=False)

    sys_of_calc: Mapped["System_of_calculation"] = relationship(backref='translation_sys_of_calcs')
    lang: Mapped["Lang"] = relationship(backref='translation_sys_of_calcs')

class TranslationRecipe(Base):
    __tablename__ = "translation_recipes"
    id = Column(Integer, primary_key=True)
    id_recipe = Column(Integer, ForeignKey('recipes.id', ondelete="CASCADE"), nullable=False, default=1)
    id_lang = Column(Integer, ForeignKey('langs.id', ondelete="CASCADE"), nullable=False, default=1)
    text = Column(String(255), nullable=False)

    recipe: Mapped["Recipe"] = relationship(backref='translation_recipes')
    lang: Mapped["Lang"] = relationship(backref='translation_recipes')

class TranslationStep(Base):
    __tablename__ = "translation_steps"
    id = Column(Integer, primary_key=True)
    id_step = Column(Integer, ForeignKey('steps.id', ondelete="CASCADE"), nullable=False, default=1)
    id_lang = Column(Integer, ForeignKey('langs.id', ondelete="CASCADE"), nullable=False, default=1)
    text = Column(String(255), nullable=False)

    step: Mapped["Step"] = relationship(backref='translation_steps')
    lang: Mapped["Lang"] = relationship(backref='translation_steps')


