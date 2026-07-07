import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = "troque_essa_chave_no_futuro"

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "database", "gremio.db")

    SQLALCHEMY_TRACK_MODIFICATIONS = False

    ADMIN_PASSWORD = "GREMIO2026.LABEL"