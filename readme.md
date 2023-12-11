# ENGENHARIA DE SOFTWARE - PUC-RIO 2023.1

## MVP-IV - Engenharia de Sistemas de Software Inteligentes

Este repositório contém o código fonte do projeto de Engenharia de Sistemas de Software Inteligentes desenvolvido para atender aops requsiitos do MVP-IV da disciplina de Engenharia de Sistemas de Software Inteligentes do curso de Engenharia de Software da PUC-Rio/2023.

O projeto consiste em um sistema de predição de morte / sobrevivência de passageiros do Titanic, baseado em um modelo de Machine Learning desenvolvido com base nos dados do dataset disponibilizado no Kaggle.

## Modelo de Machine Learning

O modelo de Machine Learning foi desenvolvido utilizando a linguagem Python e a biblioteca Scikit-Learn e foi escrito usando a plataforma Google Colabe o notebook utilizado por ser acessado aqui https://colab.research.google.com/drive/18fmovdw_M3VUTbCu2q6zUHEl-AgFg86u#scrollTo=MPtjghQ7Ywwv. 

O modelo foi exportado para o arquivo `_titanic.pkl` e é utilizado de forma embarcada na API Flask para realizar as predições. 

Uma cópia do notebook utilizado para desenvolver o modelo, bem como o dataset e um arquivo que raliza a predição de todos os passageiros dod ataset original pode ser encontrado na pasta `notebook`.

## API

A API foi desenvolvida utilizando a linguagem Python e o framework Flask e possui os seguintes endpoints:

- `GET /` - endpoint para a documentação da API
- `GET /passageiros` - endpoint para listar todos os passageiros cadastrados na API
    - retorna uma lista com os dados de todos os passageiros cadastrados e as respectivas predições de sobrevivência
    - Exemplo de requisição: `GET /passageiros`
    - Exemnplo de resposta:
    ```json
    [{
        "age": 38,
        "cabin": "C85",
        "embarked": "C",
        "fare": 71.2833,
        "id": 1,
        "name": "Mrs. John Bradley (Florence Briggs Thayer) Cumings",
        "outcome": 1,
        "parch": 0,
        "pclass": 1,
        "sex": "femake",
        "sibsp": 1,
        "ticket": "string"
    }]
    ```
- `GET /passageiros/<id>` - endpoint para listar um passageiro específico
    - retorna os dados do passageiro cadastrado e a predição de sobrevivência
    - Exemplo de requisição: `GET /passageiros/1`
    - Exemplo de resposta:
    ```json
        {
            "age": 38,
            "cabin": "C85",
            "embarked": "C",
            "fare": 71.2833,
            "id": 1,
            "name": "Mrs. John Bradley (Florence Briggs Thayer) Cumings",
            "outcome": 1,
            "parch": 0,
            "pclass": 1,
            "sex": "femake",
            "sibsp": 1,
            "ticket": "string"
        }
    ```
- `POST /passageiros` - endpoint para cadastrar um novo passageiro e realizar a predição de sobrevivência
    - Exemplo de requisição:
    ```json
    {
        "age": 38,
        "cabin": "C85",
        "embarked": "C",
        "fare": 71.2833,
        "name": "Mrs. John Bradley (Florence Briggs Thayer) Cumings",
        "parch": 0,
        "pclass": 1,
        "sex": "femake",
        "sibsp": 1,
        "ticket": "string"
    }
    ```
    - Exemplo de resposta:
    ```json
    {
        "age": 38,
        "cabin": "C85",
        "embarked": "C",
        "fare": 71.2833,
        "id": 1,
        "name": "Mrs. John Bradley (Florence Briggs Thayer) Cumings",
        "outcome": 1,
        "parch": 0,
        "pclass": 1,
        "sex": "femake",
        "sibsp": 1,
        "ticket": "string"
    }
    ```

## Requisitos

- Python 3.8.5+
- Node 14.17.0+
- npm 6.14.13+

## Como executar o projeto

- clone este repositório
- api (flask)
  - acesse a pasta api: `cd api`
  - crie um ambiente virtual executando o comando: `python -m venv .venv`
  - ative o ambiente virtual executando o comando: `source .venv/bin/activate` (unix) ou `source .venv/Scripts/activate` (windows)
  - execute o comando: `pip install -r requirements.txt`
  - execute o comando: `python app.py`
  - para acessar a documentação da API, acesse o endereço: `http://localhost:5000/`
- app (react):
  - acesse a pasta app: `cd app`
  - execute o comando: `npm install`
  - execute o comando: `npm start`
  - acesse o endereço: `http://localhost:3000/`

## Como executar os testes

- api (flask)
  - acesse a pasta api: `cd api`
  - caso ainda não tenha criado, crie um ambiente virtual executando o comando: `python -m venv .venv`
  - caso ainda não esteja ativado, ative o ambiente virtual executando o comando: `source .venv/bin/activate` (unix) ou `source .venv/Scripts/activate` (windows)
  - execute o comando: `pip install -r requirements.txt`
  - execute o comando: `python -m pytest -v`

## TODO

- Melhorar o modelo de predição de sobrevivência 
  - [ ] Trabalhar variáveis categóricas (Cabin, Name, Ticket)


- Melhorar a interface do usuário
  - [ ] Melhorar a interface do usuário
  - [ ] Adicionar gráficos
  - [ ] Adicionar informações sobre o modelo de predição
