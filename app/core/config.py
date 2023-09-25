import os
import pytz

from dotenv import load_dotenv
from starlette.config import Config

# TODO: config 설정 방법 변경 ( 현재 방법은 임시 )

config = Config(".env")

API_PROTOCOL = config("API_PROTOCOL")
API_HOST = config("API_HOST")
API_PORT = config("API_PORT")

# postgres
POSTGRES_HOST = config("POSTGRES_HOST")
POSTGRES_PORT = config("POSTGRES_PORT")
POSTGRES_USER = config("POSTGRES_USER")
POSTGRES_PASSWORD = config("POSTGRES_PASSWORD")
POSTGRES_DB = config("POSTGRES_DB")

# misc
TIMEZONE = pytz.timezone("Asia/Seoul")

# 토큰 관련
# to get a string like this run: openssl rand -hex 32
JWT_SECRET_KEY = config("JWT_SECRET_KEY")
JWT_REFRESH_SECRET_KEY = config("JWT_REFRESH_SECRET_KEY")
ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30  # 30분
REFRESH_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7  # 1주일
