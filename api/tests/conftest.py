# tests/conftest.py
import os
import sys

os.environ["TESTING"] = "True"
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from flask_openapi3 import OpenAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base


@pytest.fixture(scope="module")
def test_app():
    app = OpenAPI(__name__)
    app.config["TESTING"] = True
    app.config["DATABASE_URI"] = "sqlite:///:memory:"
    engine = create_engine(app.config["DATABASE_URI"])
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    with app.app_context():
        yield app
        Base.metadata.drop_all(bind=engine)


@pytest.fixture
def session(test_app):
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(bind=engine)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    yield session
    session.close()


@pytest.fixture
def client(test_app):
    return test_app.test_client()
