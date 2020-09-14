# apis-project

Para realizar este proyecto he trabajado con un dataset de libros de Kaggle.com.
https://www.kaggle.com/jealousleopard/goodreadsbooks
https://www.youtube.com/watch?v=bJ5K7IERMRE

## Elección de dataset

Los datos obtenidos están muy bien estructurados. 
El archivo parece que está en buenas condiciones, pero al abrirlo encontramos errores.
En data_set_cleaning veo cómo subsanarlos y llevo a cabo un análisis más exhaustivo de las columnas y datos para entender mejor la información.

Este dataset cuenta con cerca de 12000 referencias clasificadas por título, autor, fecha de publicación y puntuación media, además del número de páginas y reviews.



## Creación de main.py con argparse


## Filtrado de dataset con el script generado en main.py

## Enriquecimiento del dataset con información externa

https://thegreatestbooks.org/


Elegí esta web porque contiene una lista generada a partir de otras listas de libros "mejores de" de una variedad de fuentes.
En este site utilizan un algoritmo para crear esta lista maestra basada en la cantidad de listas en las que aparece un libro en particular. Las listas más relevantes que tienen en cuenta  de "lo mejor de todos los tiempos" votadas por autores y expertos sobre las listas generadas por los usuarios. 

Esta información es de gran interés para cotejarla con el dataset extraído de Kaggle y hacer una comparación entre los mejor valorados y las métricas puestas de manifiesto en la data obtenida previamente.

