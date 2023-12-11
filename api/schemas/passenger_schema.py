from pydantic import BaseModel, Field
from typing import List, Optional
from models.passenger import Passenger


class PassengerSchema(BaseModel):
    """ Define como um novo passageiro a ser inserido deve ser representado
    """
    pclass: int = Field(example=1, description="Classe do passageiro")
    name: str = Field(example="Mrs. John Bradley (Florence Briggs Thayer) Cumings", description="Nome do passageiro")
    sex: str = Field(example="femake", description="Sexo do passageiro")
    age: int = Field(example=38, description="Idade do passageiro")
    sibsp: int = Field(example=1, description="Número de irmãos e cônjuges a bordo")
    parch: int = Field(example=0, description="Número de pais e filhos a bordo")
    ticket: str = Optional[Field(example="PC 17599", description="Número do ticket do passageiro")]
    fare: float = Field(example=71.2833, description="Tarifa do passageiro")
    cabin: str = Field(example="C85", description="Cabine do passageiro")
    embarked: str = Field(example="C", description="Porto de embarque do passageiro")


class PassengerViewSchema(PassengerSchema):
    """Define como um passageiro será representado
    """
    id: int = Field(example=1, description="ID do passageiro")
    outcome: int = Field(example=1, description="Sobreviveu ou não")


class PassengerSearchSchema(BaseModel):
    """Define a estrutura para a busca de passageiros: apenas o nome
    """
    id: int = Field(example=1, description="ID do passageiro")


class PassengersListSchema(BaseModel):
    """Define a representação de uma lista de passageiros
    """
    passengers: List[PassengerViewSchema]


# class PacienteDelSchema(BaseModel):
class PassengerDelSchema(BaseModel):
    """Define a estrutura para a deleção de um passageiro: apenas o nome
    """
    name: str = "Mrs. John Bradley (Florence Briggs Thayer) Cumings"


# apresenta um passageiro
def passenger_show(passenger: Passenger):
    """ Retorna uma representação do passageiro seguindo o schema definido em
        PassengerViewSchema.
    """
    return passenger.to_dict()


# apresenta uma lista de passageiros
def passengers_show(passengers: List[Passenger]):
    """ Retorna uma representação de uma lista de passageiros seguindo o schema
        definido em PassengersListSchema.
    """
    result = []
    for passenger in passengers:
        result.append(passenger_show(passenger))

    return {"passengers": result}
