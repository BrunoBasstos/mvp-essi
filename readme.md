# ENGENHARIA DE SOFTWARE - PUC-RIO 2023.1
## MVP-IV - Engenharia de Sistemas de Software Inteligentes

- Este repositório contém o código fonte do projeto de Engenharia de Sistemas de Software Inteligentes desenvolvido para atender aops requsiitos do MVP-IV da disciplina de Engenharia de Sistemas de Software Inteligentes do curso de Engenharia de Software da PUC-Rio/2023.

- O projeto consiste em um sistema de predição de morte / sobrevivência de passageiros do Titanic, baseado em um modelo de Machine Learning desenvolvido com base nos dados do dataset disponibilizado no Kaggle.

### Requisitos
- Python 3.8.5+
- Node 14.17.0+
- npm 6.14.13+


# Como executar o projeto
- clone este repositório
- api (flask)
    - acesse a pasta api: `cd api`
    - crie um ambiente virtual executando o comando: `python -m venv venv`
    - ative o ambiente virtual executando o comando: `source venv/bin/activate`
    - execute o comando: `pip install -r requirements.txt`
    - execute o comando: `python app.py`
- app (react):
    - acesse a pasta app: `cd app`	
    - execute o comando: `npm install`
    - execute o comando: `npm start`ø
    - acesse o endereço: `http://localhost:3000/`


# Como executar os testes
- api (flask)
    - acesse a pasta api: `cd api`
    - crie um ambiente virtual executando o comando: `python -m venv venv`
    - ative o ambiente virtual executando o comando: `source venv/bin/activate`
    - execute o comando: `pip install -r requirements.txt`
    - execute o comando: `python -m pytest -v`


## TODO
- Melhorar o modelo de predição de sobrevivência
    - [ ] Trabalhar variáveis categóricas (Cabin, Name, Ticket)
ø
- Melhorar a interface do usuário
    - [ ] Melhorar a interface do usuário
    - [ ] Adicionar gráficos
    - [ ] Adicionar informações sobre o modelo de predição
