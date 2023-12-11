# models/titanic.py
import os
import joblib
import pandas as pd


class Titanic:
    model = None
    path = '.ml-model/_titanic.pkl'

    def __init__(self, path='.ml-model/_titanic.pkl'):
        """Inicializa o modelo do Titanic"""
        self.path = path
        self.load_model()

    def load_model(self):
        """Carrega o modelo treinado."""
        if os.path.exists(self.path):
            self.model = joblib.load(self.path)
        else:
            raise FileNotFoundError(f"Modelo não encontrado em: {self.path}")

    def predict_survival(self, passenger):
        """Faz a predição de sobrevivência ou morte de um passageiro do Titanic
        """
        # criar um dataframe com os dados do passageiro formatando as colunas para compatibilidade com o modelo
        data = {
            'Pclass': [passenger.pclass],
            'Sex': [passenger.sex],
            'Age': [passenger.age],
            'SibSp': [passenger.sibsp],
            'Parch': [passenger.parch],
            'Fare': [passenger.fare],
            'Embarked': [passenger.embarked],
            'Cabin': [passenger.cabin]
        }
        df = pd.DataFrame(data)

        # fazer a predição
        survival = self.model.predict(df)
        return int(survival[0])

    def predict(self, data):
        """Faz a predição de sobrevivência ou morte de um passageiro do Titanic
        """
        # criar um dataframe com os dados do passageiro formatando as colunas para compatibilidade com o modelo
        df = pd.DataFrame(data)

        # fazer a predição
        return self.model.predict(df)
