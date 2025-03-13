# pythonWeb

## ejecucion de proyecto en local

para ejecutar la aplicacion web en un ambiente local debe seguir los siguientes pasos

1. acceder a la carpeta raiz del proyecto

```bash
cd /home/user/Descargas/pythonWeb
```

2. instalar las librerias que estan en el archivo **requirements.txt**

```bash
pip install -r requirements.txt
```

3. despues de que se instalen los paqueten ejecutar la aplicacion web
```bash
streamlit run app.py
```

## despliegue en render.com

para poder ejecutar la aplicacion web en render debe seguir los siguientes pasos

1. Crear una cuenta en render
2. Inicia o crea sesión en [Render](https://render.com/)
3. Crea un nuevo servicio web y conecta con el repositorio web de gitHub
4. busca la opcion **start Command** e ingresa el siguiente comando

    ```bash
    streamlit run app.py    
    ```
5. busca la opcion **Build Command** e ingresa el siguiente comando

    ```bash
    pip install -r requirements.txt  
    ```
6. revisar que en Instance Type este seleccionada la opcion **Free**

7. Despues de estos pasos presionar el boton **Deploy Web Services** que se encuentra al final de la pagina

