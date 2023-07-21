# Proyecto_final

**<h1 align="center">Sistema de recomendación de cursos</h1>** :mortar_board:
===========================================================================


Este proyecto es un Sistema de Recomendación de cursos desarrollado en Python. Utiliza Streamlit como interfaz para que los usuarios seleccionen sus preferencias y, en función de ellas, se les ofrezcan runas u otras recomendaciones. 

El sistema utiliza datos de cursos almacenados en un archivo CSV y permite filtrar las recomendaciones según diferentes criterios seleccionados por el usuario que se recibirán en formato JSON.

💻 **#Tecnología utilizada**
-----------------------------------------

- [Python](https://docs.python.org/3.7/l)
- [Pandas](https://pandas.pydata.org/)
- [JSON](https://www.json.org/json-es.html)
- [Numpy](https://numpy.org/)
- [Streamlit](https://docs.streamlit.io/)
- [Visual Studio Code](https://code.visualstudio.com/)

**#Cómo ejecutar el programa** :rocket:
-----------------------------------------

Clonar o descargar el repositorio en su máquina local.
Asegurarse de tener instaladas las bibliotecas requeridas mencionadas en los requisitos.
Ejecutar el archivo app.py con el siguiente comando:
    
    streamlit run main.py

**#Cómo utilizar el sistema de recomendación** :mag:
----------------------------------------------------

Seleccione su provincia en el menú desplegable.
Seleccione el formato de curso deseado (Presencial, Online o ambos) utilizando la función de selección múltiple.
Seleccione las etapas educativas que le interesan (Infantil, Primaria, Secundaria, Bachillerato) utilizando la función de selección múltiple.
Elija la temática que le interesa de la lista proporcionada.
Seleccione el objetivo que mejor se ajuste a sus necesidades (Ofrecer formación variada, Aumentar la participación de las familias, Sorprender con contenidos innovadores y formatos novedosos).


**Funcionamiento del sistema** :gear:
-------------------------------------

El sistema cargará los datos de cursos desde un archivo CSV ubicado en la ruta data/Datos_ampliados.csv. Luego, utilizará la información ingresada por el usuario para filtrar los cursos y generar recomendaciones personalizadas.

Las recomendaciones se mostrarán en una tabla con detalles como el título del curso, formato, etapa educativa, temática y número de sesiones.

Además, el usuario tendrá la opción de descargar las recomendaciones en formato CSV haciendo clic en el botón "Descarga tu recomendación".

**Enlace a la web oficial** :globe_with_meridians:
--------------------------------

También se proporciona un enlace a la web oficial del sistema de recomendación, donde puede obtener más información sobre la empresa o los cursos ofrecidos.

Para cualquier pregunta o soporte técnico, no dude en contactarnos a través del enlace proporcionado en la web. 

**Siguientes pasos**
-----------------------
- El JSON del que partimos debe generarse de forma automática a través de la selección en Streamlit del usuario.
- Que la valoración de los cursos reciba la información automática a trvés de la web, y sea esa la información que se utiliza.
- Evitar recomendar a los clientes formaciones previamente realizadas.
- Utilizar la información como un dashboard de negocio

:incoming_envelope: **Información de contacto**
-------------------------------------
[Linkedin](www.linkedin.com/in/herminiapr-data-analist-product-manager)

Si tienes cualquier duda, ¡contáctame! :smile: