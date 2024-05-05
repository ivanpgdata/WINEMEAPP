
# WineMeApp
![This is an alt text.](https://github.com/ivanpgdata/WineMeApp/blob/main/WineMeApp/images/banner_img.jpg?raw=true "This is a sample image.")


# Winemeapp! Recomendador de Vinos

🍷 https://winemeapp.streamlit.app/ 🍷

## 🍇Datos🍇
Hemos sacado todos los 4800 vinos españoles disponibles en la pagina web bodeboca.como utilizando paquetes como beatiful soup

## 🍇Preprocesamiento🍇

Hemos limpiado, revisado NAs del dataset. Despues para las variables/columnas tipo string, hemos pasado a minuscula, limpiado de stop words oficiales del castellano, y otras personalizadas que creamos para cada columna, normalizado, tokenizado y lematizado para tener los strings mas limpios (procesamiento de NLP)

## 🍇EDA🍇
Hemos revisado los datos haciendo un Exploratory Data Analysis

# 🍷Modelo de Recomendación🍷
Una vez normalizado el texto de cata y maridaje, los unimos en una columna: "descripcion", que será la que usemos como elemento del vino a evaluar.

Utilizamos un modelo preentrenado (transfer learning: Google Universal Sentence Encoder version 4 (USE)), para convertir las notas de cata y maridaje (descripcion), en vectores de 512 dimensiones para capturar el significado semántico. El USE utiliza una arquitectura de redes neuronales profundas entrenada en grandes corpus de texto.

Por último, utilizamos similitudes de coseno entre dos vectores que representan vinos para calcular los valores de similitud entre ellos. Esto es lo que usamos para la recomendacion, obteniendo aquellos con el valor más cercano a 1 y así determinar los vinos más afines en función de cata y maridaje.

# 🍷Modelo TOPSIS🍷

Una vez realizado el modelo de recomendación, usamos el modelo TOPSIS, un método de toma de decisiones utilizado para evaluar la mejor opción entre un conjunto de alternativas basándose en múltiples criterios el cual tiene los diferentes pasos:

Una vez se han establecido los criterios  que se usarán para evaluar las alternativas junto con qué alternativas se van a comparar (usando el modelo de recomendación), y tras normalizar los datos escalándolos entre valores 0 y 1, ee construye una matriz de decisión donde las filas representan las alternativas y las columnas representan los criterios normalizados. Con los datos normalizados, aplica pesos a cada atributo según los valores proporcionados y crea un DataFrame con características ponderadas. 

Tras ello, se determinan dos soluciones de referencia: la solución ideal, que maximiza cada criterio, y la solución anti-ideal, que minimiza cada criterio. 

Posteriormente se calcula la distancia euclidea entre cada alternativa y las soluciones ideal y anti-ideal. Esta distancia mide la proximidad de cada alternativa a cada una de 
estas soluciones de referencia. 

Por último se calcula el índice de similitud para cada alternativa dividiendo la distancia a la solución anti-ideal entre la suma de la distancia a la solución ideal y la distancia a la solución anti-ideal. Este índice cuantifica qué tan cerca está cada 
alternativa de ser la mejor o la peor solución posible.
