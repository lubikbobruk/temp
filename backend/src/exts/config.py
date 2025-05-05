from decouple import config
from datetime import timedelta
import os


BASE_DIR = os.path.dirname(os.path.realpath(__file__))


# General configuration settings.
class Config:
    SECRET_KEY = config("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = config("SQLALCHEMY_TRACK_MODIFICATIONS", cast=bool)
    JWT_SECRET_KEY = config("JWT_SECRET_KEY")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_ACCESS_TOKEN_LOCATION = ["headers"]


# Development configuration settings with DEV DB.
class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'dev.db')
    SQLALCHEMY_ECHO = True
    DEBUG = True


# Testing configuration settings with TEST DB.
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, 'test.db')
    SQLALCHEMY_ECHO = False
    TESTING = True
