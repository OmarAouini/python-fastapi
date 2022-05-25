"""SQLALCHEMY DATABASE MODULE"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DB_URL = "mysql://localhost:3306"
DB_NAME = "employees"
SQLALCHEMY_DATABASE_URL = f'{DB_URL}/{DB_NAME}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
