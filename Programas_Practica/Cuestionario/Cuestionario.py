'''
Tipos:
- (OM) Opción múltiple:
    Escribir la letra del inciso que es correcta en la columna de respuesta
    y escribir las diferentes respuestas en las columnas de inciso A hasta D

- (VF) Verdadero falso
    Escribir V o F en la columna de respuesta dependiendo si la respuesta es
    verdadera o falsa

- (PA) Pregunta abierta
    Escribir la respuesta correcta en la columna de respuesta
'''

# pip install pandas
import pandas as pd
from pandas import DataFrame, read_csv

import random
import time


def ChecarRespuesta(respuesta: str, df: DataFrame) -> bool:
    if respuesta.upper() == df.at[row, 'Respuesta'].upper():
        print("¡Respuesta correcta! ✅")
        return True
    else:
        print("Respuesta incorrecta ❌ , la respuesta correcta era: " +
              df.at[row, 'Respuesta'])
        return False


numPreguntas = 10
file = r'Preguntas/Instrucciones.csv'
df = pd.read_csv(file)

n_row, n_col = df.shape

if numPreguntas > n_row:
    raise UserWarning(
        "Error numPreguntas es mayor al número de preguntas que hay en el archivo csv")
# Revolver que número de columna usar
rowNum = [i for i in range(n_row)]
random.shuffle(rowNum)
random.shuffle(rowNum)
rowNum = rowNum[:numPreguntas]
correctas = 0
incorrectas = 0

# print(df)
# print(rowNum)

counter = 0
for row in rowNum:
    print("\n\n\n\n\n===== Pregunta " +
        str(counter+1) + " de " + str(numPreguntas) + " =====")
    tipo = df.at[row, 'Tipo']

    # Opción múltiple
    if tipo == "OM":
        print("Opción múltiple:")
        print(df.at[row, 'Pregunta'])
        print(df.loc[row].iloc[3:].to_string(header=False))

        print("\nEscribe el inciso de tu respuesta: ")

    # Escribir la respuesta
    elif tipo == "PA":
        print("Pregunta abierta:")
        print(df.at[row, 'Pregunta'])

        print("\nEscribe tu respuesta: ")

    # Verdadero o falso
    elif tipo == "VF":
        print("Verdadero o falso:")
        print(df.at[row, 'Pregunta'])

        print("\nEscribe V para verdadero o F para falso: ")
    else:
        print("ERROR en " + str(row))

    respuesta = input()
    if (ChecarRespuesta(respuesta, df) == True):
        correctas += 1
    else:
        incorrectas += 1
    time.sleep(0.5)
    counter += 1

print("\n\n\n+=+=+= RESULTADOS +=+=+=\n")
print("Respuestas correctas  \t" + str(correctas) + "  ✅")

if correctas == numPreguntas:
    print("🎆  ¡Felicidades todas tus respuestas son correctas! 🎆")
else:
    print("Respuestas incorrectas\t" + str(incorrectas) + "  ❌")
