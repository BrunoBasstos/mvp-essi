#test.py
import joblib
import pandas as pd
from transformers import CabinToNumber

modelo = joblib.load('_titanic.pkl')

# ler todos os registros do dataset e avaliar no modelo, depois comparar com o resultado real
df = pd.read_csv('src/titanic-dataset.csv')

# fazer a predição para cada registro
predicao = modelo.predict(df)

# comparar a predição com o resultado real
acertos = []
erros = []

for i in range(len(predicao) - 1):
    if predicao[i] == int(df['Survived'][i]):
        acertos.append(df['PassengerId'][i])
    else:
        erros.append(df['PassengerId'][i])
    print(f"Predição {i}: ", "sobreviveu    " if predicao[i] == 1 else "não sobreviveu", f"\t passageiro {df['Name'][i]}")

print("\n")
print(f"Acertos: {len(acertos)}", f"   |   Erros: {len(erros)}")

