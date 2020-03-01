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
import os


def ChecarRespuesta(respuesta: str, df: DataFrame, row) -> bool:
    if respuesta.upper() == df.at[row, 'Respuesta'].upper():
        print("¡Respuesta correcta! ✅")
        return True
    else:
        print("Respuesta incorrecta ❌ , la respuesta correcta era: " +
              df.at[row, 'Respuesta'])
        return False


def OpcionMultiple(df: DataFrame, row: int) -> bool:
    # Columnas donde se encuentran los incisos
    opciones = [4, 5, 6, 7]
    # Revolver las respuestas para que siempre salgan en diferente orden los incisos
    random.shuffle(opciones)
    random.shuffle(opciones)

    # Valor numérico de A
    inciso = 65
    for opcion in opciones:
        print("Inciso " + chr(inciso) + ": " +
              df.loc[row].iloc[opcion])
        inciso += 1
    while True:
        respuesta = input()
        respuesta = respuesta.upper()
        if ord(respuesta[0]) < 65 or ord(respuesta[0]) > 68:
            print("Solo debe escribir el inciso")
        else:
            numRespuesta = ord(respuesta[0]) - 65
            # Respuesta correcta
            # Sacar el valor numérico de la respuesta correcta del 4 al 7 y revisarlo contra el valor del vector de incisos revuelto que se tiene
            if ord(df.at[row, 'Respuesta'].upper()) - 61 == opciones[numRespuesta]:
                print("¡Respuesta correcta! ✅")
                return True
            # Respuesta incorrecta
            else:
                # Calcular inciso correcto aunque estén revueltos
                respuestaCorrecta = ord(df.at[row, 'Respuesta'].upper()) - 61
                letraCorrecta = 0
                for i in range(len(opciones)):
                    if opciones[i] == respuestaCorrecta:
                        letraCorrecta = i
                        break

                print("Respuesta incorrecta ❌ , la respuesta correcta era: " +
                      chr(letraCorrecta + 65))
                return False


def ComenzarCuestionario(rutaArchivo: str):
    print('Cargando ' + rutaArchivo)
    df = pd.read_csv(rutaArchivo)
    n_row, n_col = df.shape

    # Revolver que número de columna usar
    rowNum = [i for i in range(n_row)]
    random.shuffle(rowNum)
    random.shuffle(rowNum)

    correctas = 0
    incorrectas = 0

    counter = 0
    for row in rowNum:
        print("\n\n\n\n\n===== Pregunta " +
              str(counter+1) + " de " + str(n_row) + " =====")
        tipo = df.at[row, 'Tipo']

        # Opción múltiple
        if tipo == "OM":
            print("Opción múltiple:")
            print(df.at[row, 'Pregunta'])
            if OpcionMultiple(df, row) == True:
                correctas += 1
            else:
                incorrectas += 1
                if df.at[row, 'Tip']:
                    print("Tip: " + df.at[row, 'Tip'])
                time.sleep(0.5)
                counter += 1
            continue

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

        # Revisar que si se introduzca V o F en preguntas de verdadero o falso
        if tipo == "VF":
            while True:
                respuesta = input()
                if respuesta.upper() == 'V' or respuesta.upper() == 'F':
                    break
                print("Solo escribe V para verdadero o F para falso")
        else:
            respuesta = input()
        
        if ChecarRespuesta(respuesta, df, row) == True:
            correctas += 1
        else:
            incorrectas += 1
            if df.at[row, 'Tip']:
                print("Tip: " + df.at[row, 'Tip'])
        time.sleep(0.5)
        counter += 1

    print("\n\n\n+=+=+= RESULTADOS +=+=+=\n")
    print("Respuestas correctas  \t" + str(correctas) + "  ✅")

    if correctas == n_row:
        print("🎆  ¡Felicidades todas tus respuestas son correctas! 🎆")
    else:
        print("Respuestas incorrectas\t" + str(incorrectas) + "  ❌")
    
    calificacion = correctas/n_row * 10
    print("Calificación: " + str(round(calificacion,1)))


if __name__ == "__main__":
    # Escanear en el directorio para encontrar archivos .csv
    path = 'Preguntas'
    files = []
    # r=root, d=directories, f = files
    for r, d, f, in os.walk(path):
        for file in f:
            if '.csv' in file:
                files.append(os.path.join(r, file))

    # Mostrar menu
    print("=== Cuestionarios ===")
    while True:
        print("\n")
        for i in range(len(files)):
            print(str(i+1) + ".- " + str(files[i]))
        print("\nPor favor escoja un archivo escribiendo el número que le corresponda:")
        numArchivo = input()
        if numArchivo.isnumeric() == False:
            print("Debe escribir un número")
        elif int(numArchivo) > 0 and int(numArchivo) < len(files) + 1:
            break
        else:
            print("Debe escribir un número entre 1 y " + str(len(files) + 1))
        time.sleep(1.0)

    ComenzarCuestionario(files[int(numArchivo) - 1])
