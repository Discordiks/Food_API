from fastapi import FastAPI, Depends, HTTPException, FastAPI, Request, status
from routers import category_router, ingredient_router, mealtime_router, recipe_router, count_router, step_router, sys_of_calc_router, user_router, photo_router, score_router
from sqlalchemy.orm import Session
from typing import List
#модули для связи бэка с фронтом
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse, JSONResponse
from fastapi.exceptions import RequestValidationError
#модули для инициализации Firebase
import os
import firebase_admin
from firebase_admin import credentials, messaging
from config import settings

if not firebase_admin._apps:
    cred = credentials.Certificate(settings.firebase_credentials)
    firebase_admin.initialize_app(cred)

app = FastAPI()

#подключение АпиРоутера (маршруты сущности)
app.include_router(user_router)
app.include_router(recipe_router)
app.include_router(count_router)
app.include_router(step_router)
app.include_router(photo_router)
app.include_router(score_router)
app.include_router(category_router)
app.include_router(ingredient_router)
app.include_router(mealtime_router)
app.include_router(sys_of_calc_router)

#управление CORS - совместное использование ресурсов разных источников
origins=["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)