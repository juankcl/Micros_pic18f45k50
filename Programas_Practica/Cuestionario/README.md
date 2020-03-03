# Cuestionarios
### Hecho por Emilio Puga
Programa hecho en Python
## Descripción
Este programa es utilizado para generar un cuestionario a partir de un archivo xlsx.

Hay tres tipos de preguntas:
- Pregunta abierta: El programa simplemente revisa si la respuesta es exactamente igual (no toma en cuenta las mayúsculas o minúsculas) a la respuesta correcta.
- Verdadero o falso: Pregunta donde la respuesta solo es verdadero o falso
- Opción múltiple: Muestra los incisos, estos son mostrados al azar cada vez que se muestra la pregunta y se le pide al usuario escoger un inciso.

## Uso
Al iniciar el programa, este escanea la carpeta de *Preguntas* buscando archivos de tipo `.xlsx`, a continuación muestra todos los archivos que encontró y se debe escoger uno escribiendo el número del archivo.

A continuación comienza la evaluación, mostrando el número de la pregunta. El tipo de pregunta, la pregunta y se le pide al usuario proporcionar la respuesta. Después de esto muestra si la respuesta era correcta o incorrecta.

### Sintaxis archivo xlsx
(Por el momento se recomienda usar excel para escribir los archivos, al momento de guardar se debe poner que es en formato xlsx)

El archivo xlsx debe seguir el siguiente formato:

| Tipo | Pregunta          | Respuesta | Tip                                             | Inciso A | Inciso B | Inciso C | Inciso D  |
|------|-------------------|-----------|-------------------------------------------------|----------|----------|----------|-----------|
| PA   | Pregunta Abierta  | Respuesta | Esto se muestra si la respuesta no fue correcta |          |          |          |           |
| VF   | Verdadero o Falso | V         | Esto se muestra si la respuesta no fue correcta |          |          |          |           |
| OM   | Opción múltiple   | A         | Esto se muestra si la respuesta no fue correcta | Inciso A | Inciso B | Inciso C |  Inciso D |

1. En la primera columna (*Tipo*) se pone que tipo de pregunta es, utilizando las siglas PA, VF y OM.
2. En la segunda columna (*Pregunta*) se escribe la pregunta que se mostrará.
3. La tercera columna (*Respuesta*) es donde se escribe la respuesta. En el caso de las preguntas abiertas se escribe la respuesta correcta tal y como es, en verdadero o falso se debe escribir V (*verdadero*) o F (*falso*) y cuando es opción múltiple se escribe A, B, C o D dependiendo de cuál será el inciso correcto.
4. La cuarta columna (*Tip*) es un texto que se mostrará si la respuesta dada por el usuario es incorrecta.
5. Por último de la quinta a la octava columna son los espacios para escribir los incisos que se mostrarán en las preguntas que se sean de opción múltiple.

## Instalación
Para poder ejecutar este programa es necesario tener Python3 e instalar la paquetería de Pandas utilizando el siguiente comando:

```
pip install pandas
pip install xlrd
```