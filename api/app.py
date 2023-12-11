#  app.py
from flask_cors import CORS
from flask_openapi3 import OpenAPI, Info, Tag
from flask import redirect, abort, request, jsonify
from werkzeug.exceptions import NotFound, BadRequest

from logger import logger
from models import Session, Titanic, passenger
from models.passenger import Passenger
from schemas.error_schema import ErrorSchema
from schemas.passenger_schema import PassengerViewSchema, PassengerSearchSchema, PassengerSchema

# Informações da API
info = Info(title="API - Titanic", version="0.0.1",
            description="API para uso do modelo de ML gerado para predição de morte/sobrevivência ao naufrágio do Titanic")

# Instanciando a aplicação
app = OpenAPI(__name__, info=info)

# Habilitando CORS
CORS(app)

# Criando tags para documentação da API
home_tag = Tag(name="Home", description="Selecionar estilo de documentação")
titanic_tag = Tag(name="Titanic",
                  description="API para uso do modelo de ML gerado para predição de morte/sobrevivência ao naufrágio do Titanic")
passenger_tag = Tag(name="Passageiros", description="Operações com passageiros")


# Rota home
@app.get('/', tags=[home_tag])
def home():
    """Redireciona para /openapi, tela que permite a escolha do estilo de documentação.
    """
    return redirect('/openapi')


# registrar passageiro e retornar dados incluindo predição
@app.post('/passageiros', tags=[passenger_tag],
          responses={200: PassengerViewSchema, 400: ErrorSchema},
          summary="Registrar passageiro")
def fate_predict(body: PassengerSchema):
    """Registrar passageiro

    :param body:

    Returns:
        PassengerViewSchema: Passageiro registrado
    """
    try:
        logger.info("Registrando passageiro e fazendo predição")

        titanic = Titanic()
        # instanciar passageiro usando os dados recebidos no body
        passenger = Passenger(**body.model_dump())

        # verifica se o passageiro já está cadastrado
        session = Session()

        # vamos considerar que um passageiro já cadastrado é aquele que tem o mesmo nome e a mesma idade
        passenger_exists = session.query(Passenger).filter(Passenger.name == passenger.name,
                                                           Passenger.age == passenger.age).first()

        if passenger_exists:
            raise BadRequest(description="Passageiro já cadastrado")

        # fazer a predição
        passenger.outcome = titanic.predict_survival(passenger)
        session.add(passenger)
        session.commit()

        passenger_dict = passenger.to_dict()
        return jsonify(passenger_dict)
    except BadRequest as e:
        logger.error(f"Tentativa de cadastrar passageiro já cadastrado: {e}")
        abort(400, description="Passageiro já cadastrado")
    except Exception as e:
        logger.error(f"Erro ao registrar passageiro: {e}")
        abort(500, description="Erro ao registrar passageiro")


@app.get('/passageiros', tags=[passenger_tag],
         responses={200: PassengerViewSchema},
         summary="Retorna uma lista de passageiros cadastrados")
def get_passengers():
    """Retorna uma lista de passageiros cadastrados com base no filtro opcional informado.
    Se nenhum filtro for informado, retorna todos os passageiros cadastrados.

    Returns:
        List[PassengerViewSchema]: Lista de passageiros cadastrados
    """
    try:
        logger.info("Buscando passageiros")

        session = Session()

        pclass = request.args.get('pclass')
        name = request.args.get('name')
        sex = request.args.get('sex')

        query = session.query(Passenger)
        if pclass:
            query = query.filter(Passenger.pclass == pclass)
        if name:
            query = query.filter(Passenger.name.like(f"%{name}%"))
        if sex:
            query = query.filter(Passenger.sex == sex)

        passengers = query.all()
        if not passengers:
            raise NotFound(description="Passageiros não encontrados")

        passengers = [passenger.to_dict() for passenger in passengers]
        return jsonify(passengers)
    except NotFound as e:
        abort(404, description="Passageiros não encontrados")
    except BadRequest as e:
        abort(400, description="Informe um termo de busca")
    except Exception as e:
        logger.error(f"Erro ao buscar passageiros: {e}")
        abort(500, description="Erro ao buscar passageiros")


@app.get('/passageiros/{id}', tags=[passenger_tag],
         responses={200: PassengerViewSchema},
         summary="Retorna um passageiro cadastrado")
def get_passenger(query: PassengerSearchSchema):
    """Retorna um passageiro cadastrado

    Args:
        :param query:
        id (int): ID do passageiro

    Returns:
        PassengerViewSchema: Passageiro cadastrado

    """
    try:
        id = query.id
        logger.info(f"Buscando passageiro {id}")

        session = Session()
        passenger = session.query(Passenger).filter(Passenger.id == id).first()
        if not passenger:
            logger.warning("Passageiro não encontrado")
            raise NotFound(description="Passageiro não encontrado")

        passenger_dict = passenger.to_dict()
        return jsonify(passenger_dict)

    except NotFound as e:
        abort(404, description="Passageiro não encontrado")

    except Exception as e:
        logger.error(f"Erro ao buscar passageiro: {e}")
        abort(500, description="Erro ao buscar passageiro")


if __name__ == '__main__':
    app.run()
