# models/__init__.py
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from models.base import Base
from models.titanic import Titanic
from models.passenger import Passenger

if os.environ.get("TESTING") == "True":
    db_url = "sqlite:///:memory:"
else:
    db_path = "database/"
    if not os.path.exists(db_path):
        os.makedirs(db_path)
    db_url = 'sqlite:///%s/titanic.sqlite3' % db_path

engine = create_engine(db_url, echo=False)
Session = sessionmaker(bind=engine)

if not os.environ.get("TESTING") and not database_exists(engine.url):
    create_database(engine.url)
    Base.metadata.create_all(engine)
