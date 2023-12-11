# models/passenger.py
from sqlalchemy import Column, String, Integer, DateTime, Float
from datetime import datetime
from typing import Union, Optional

from models import Base


class Passenger(Base):
    __tablename__ = 'passengers'

    id = Column(Integer, primary_key=True)
    pclass = Column("pclass", Integer)
    name = Column("name", String(255))
    sex = Column("sex", String(6))  # female ou male
    age = Column("age", Integer)
    sibsp = Column("sibsp", Integer)
    parch = Column("parch", Integer)
    ticket = Column("ticket", String(50))
    fare = Column("fare", Float)
    cabin = Column("cabin", String(50))
    embarked = Column("embarked", String(1))  # C, Q ou S
    outcome = Column("outcome", Integer, nullable=True)
    data_insercao = Column(DateTime, default=datetime.now())

    def __init__(self, pclass: int, name: str, sex: str, age: int, sibsp: int, parch: int, ticket: str, fare: float,
                 embarked: str, cabin: Union[str, None] = None, outcome: Union[int, None] = None,
                 data_insercao: Union[datetime, None] = None):
        """
        Cria um passageiro

        Arguments:
            pclass: a classe do passageiro.
            name: o nome do passageiro.
            sex: o sexo do passageiro.
            age: a idade do passageiro.
            sibsp: o número (a bordo) de irmãos/cônjuges do passageiro.
            parch: o número (a bordo) de pais/filhos do passageiro.
            ticket: o número do ticket do passageiro.
            fare: a tarifa paga pelo passageiro.
            cabin: o número da cabine do passageiro.
            embarked: o porto de embarque do passageiro.
            outcome: o resultado da predição do passageiro.
            data_insercao: data de quando o passageiro foi feito ou inserido à base
        """
        self.pclass = pclass
        self.name = name
        self.sex = sex
        self.age = age
        self.sibsp = sibsp
        self.parch = parch
        self.ticket = ticket
        self.fare = fare
        self.cabin = cabin
        self.embarked = embarked
        self.outcome = outcome if outcome else None
        # se não for informada, uysar data atual
        if data_insercao:
            self.data_insercao = data_insercao

    def to_dict(self):
        return {
            "id": self.id,
            "pclass": self.pclass,
            "name": self.name,
            "sex": self.sex,
            "age": self.age,
            "sibsp": self.sibsp,
            "parch": self.parch,
            "ticket": self.ticket,
            "fare": self.fare,
            "cabin": self.cabin,
            "embarked": self.embarked,
            "outcome": self.outcome
        }
