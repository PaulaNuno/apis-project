




![API_project_book](input/API_PROJECT_CABECERA.png)





# API-project

En este proyecto tenemos que enriquecer un dataset elegido libremente con información externa que obtengamos de un site (API, tećnicas de scrapeo). Además, plantearemos mediante el método Argparse, un script que nos ayude a filtrar dicho dataset.
Por otro lado, plantearemos un resumen de estadísticas y, finalmente, exportaremos la información obtenida.

Para realizar este proyecto he seleccionado <a href="https://www.kaggle.com/jealousleopard/goodreadsbooks">un dataset de libros</a> de Kaggle.com y la página https://thegreatestbooks.org/, que contiene una selección de las mejores obras de todos los tiempos.

Mi objetivo es cotejar si los títulos con mayor average rating en el dataframe the Kaggle están contenidos en la lista proporcionada por el site de los mejores libros.

## Elección de dataset

Los datos obtenidos están muy bien estructurados y, en principio, limpios.
El archivo parece que está en buenas condiciones, pero al abrirlo encontramos errores.
En <a href="data_set_cleaning.ipynb">data_set_cleaning</a> veo cómo subsanarlos y llevo a cabo un análisis más exhaustivo de las columnas y datos para entender mejor la información.

Este dataset cuenta con cerca de 12000 referencias clasificadas por título, autor, fecha de publicación y puntuación media, además del número de páginas y reviews.

Uno de los escollos que encuentro al analizar esta información es la forma en la que aparecen las fechas.
Para poder acceder a la información a través de los años de publicación de las obras, es necesario limpiar esta columna y convertir las fechas en años para poder utilizarlos posteriormente cuando vaya a filtrar el dataset.


## Creación de main.py con argparse y filtrado de dataset

Para la creación del <a href="main.py">script main.py</a> me basé en el average rating de los títulos.
El objetivo es que al introducir la valoración que deseamos obtener, el programa devuelva los títulos y sus correspondientes autores dentro de esa media.

##  Web scraping para enriquecer el dataset con información externa

Elegí el site de <a href="https://thegreatestbooks.org/">The greatest books</a> porque contiene una lista generada a partir de otras listas de libros "mejores de" de una variedad de fuentes.
En este site utilizan un algoritmo para crear esta lista maestra basada en la cantidad de listas en las que aparece un libro en particular. Las listas más relevantes que tienen en cuenta  de "lo mejor de todos los tiempos" votadas por autores y expertos sobre las listas generadas por los usuarios. 

Esta información es de gran interés para cotejarla con el dataset extraído de Kaggle y hacer una comparación entre los mejor valorados y las métricas puestas de manifiesto en la data obtenida previamente.

Para realizar el scrapeo de esta página analizamos la estructura de la información relevante para nuestro objetivo.

La URL base es https://thegreatestbooks.org/ y los parámetros de la query en este caso, están relacionados con la paginación del contenido. Ejemplo: ?page=2

Con esta información sobre las URL, probamos a cambiar los parámetros de la URL y vemos que las distintas páginas cargan correctamente y muestran el contenido que queremos obtener.

Una vez comprobado el comportamiento de la URL, analizo la estructura de la página en cuestión para conocer de qué manera se estructura la información en el HTML y accedo a través de la consola de Chrome para explorar el DOM.

Explorado el DOM, vemos que la información que queremos extraer está contenida debajo de la etiqueta h4.

En este fragmento aparece el contenido concerniente al primer libro de la lista.
De ahí queremos extraer la posición, 1 en este caso, el título de la obra y el autor.
Toda la lista de libros se esctructura de este modo a lo largo de las distintas páginas del site.

      <h4>
            1
. <a href="/items/225">In Search of Lost Time </a> by <a href="/authors/4798">Marcel Proust</a>
        </h4> 
        
        
Para obtener esta información utilicé el módulo Beautiful Soup. 
En el archivo <a href="web_scraping_procedure.ipynb">web_scraping_procedure</a> intenté llevar a cabo la extracción de datos que me interesaban. 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        