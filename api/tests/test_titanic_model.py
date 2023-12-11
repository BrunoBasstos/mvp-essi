# tests/test_titanic_model.py
import os
import pytest
from models import Passenger
from models.titanic import Titanic


@pytest.fixture(scope="module")
def titanic_model():
    # Caminho absoluto do modelo
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_dir, '.ml-model', '_titanic.pkl')

    # Carregar o modelo do Titanic
    model = Titanic(model_path)
    return model


def test_it_should_predict_the_survival_of_passenger_2(titanic_model, session):
    # Dados de um passageiro que sobreviveu (passageiro 2)
    # Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    # 1,"Cumings, Mrs. John Bradley (Florence Briggs Thayer)",female,38,1,0,PC 17599,71.2833,C85,C
    survivor = {
        'pclass': 1,
        'name': 'Cumings, Mrs. John Bradley (Florence Briggs Thayer)',
        'sex': 'female',
        'age': 38,
        'sibsp': 1,
        'parch': 0,
        'ticket': 'PC 17599',
        'fare': 71.2833,
        'cabin': 'C85',
        'embarked': 'C'
    }
    passenger = Passenger(**survivor)
    # Verificar se o modelo prevê sobrevivência
    prediction = titanic_model.predict_survival(passenger)
    assert prediction == 1  # 1 representa sobrevivência


def test_it_should_predict_the_deth_of_passenger_1(titanic_model, session):
    # Dados de um passageiro que não sobreviveu (passageiro 1)
    # Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,Cabin,Embarked
    # 3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
    non_survivor = {
        'pclass': 3,
        'name': 'Braund, Mr. Owen Harris',
        'sex': 'male',
        'age': 22,
        'sibsp': 1,
        'parch': 0,
        'ticket': 'A/5 21171',
        'fare': 7.25,
        'cabin': '',
        'embarked': 'S'
    }
    passenger = Passenger(**non_survivor)

    # Verificar se o modelo prevê não sobrevivência
    prediction = titanic_model.predict_survival(passenger)
    assert prediction == 0  # 0 representa não sobrevivência


import pandas as pd


def test_it_should_have_accuracy_greater_than_85_percent(titanic_model, session):
    # Carregar o dataset de teste gerado durante o treinamento no train_test_split
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    test_dataset_path = os.path.join(base_dir, '.ml-model', '_test_dataset.csv')
    test_dataset = pd.read_csv(test_dataset_path)

    # Contador para predições corretas
    correct_predictions = 0

    # Iterar sobre o dataset de teste e fazer predições
    for index, row in test_dataset.iterrows():
        passenger_data = {
            'pclass': row['Pclass'],
            'name': 'Nome de teste',
            'sex': row['Sex'],
            'age': row['Age'],
            'sibsp': row['SibSp'],
            'parch': row['Parch'],
            'ticket': row['Ticket'],
            'fare': row['Fare'],
            'embarked': row['Embarked']
        }
        passenger = Passenger(**passenger_data)
        prediction = titanic_model.predict_survival(passenger)

        if prediction == row['Survived']:
            correct_predictions += 1

    # Calcular percentual de acertos
    percentual = correct_predictions / len(test_dataset)

    # Verificar se a acurácia é maior ou igual a 85%
    assert percentual >= 0.85
