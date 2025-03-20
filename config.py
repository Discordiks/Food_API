from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import EmailStr, BaseModel
from pathlib import Path
import json

BASE_DIR= Path(__file__).parent

#указание путей к ключам
class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algrotihm: str = "RS256" #специальный алгоритм, который используется при наличии двух ключей
    access_token_expire_minutes: int = 3 #минуты

class TokenInfo(BaseModel):
    access_token:str
    token_type:str

class Settings(BaseSettings):
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./sql_app.sqlite"

    EMAIL_SMTP:str
    EMAIL_PORT:str='465'
    EMAIL_LOG:str
    EMAIL_PWD:str

    model_config = SettingsConfigDict(env_file=".env")
    token_phone_path:Path = BASE_DIR / "certs" / "AccountKey.json"
    firebase_credentials: dict = {}
    auth_jwt:AuthJWT = AuthJWT()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        try:
            with open(self.token_phone_path, "r") as f:
                self.firebase_credentials = json.load(f)
        except FileNotFoundError:
            print(f"Ошибка: Файл {self.token_phone_path} не найден.")
            self.firebase_credentials = {}
        except json.JSONDecodeError:
            print(f"Ошибка: Некорректный JSON в файле {self.token_phone_path}.")
            self.firebase_credentials = {}

settings = Settings()

