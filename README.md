# Generador de preguntas Moodle

Este proyecto es una herramienta para generar preguntas en formato XML compatibles con Moodle. Sigue los pasos a continuación para instalar y ejecutar el proyecto.

## Requisitos previos

- Python 3.8 o superior
- [pip](https://pip.pypa.io/en/stable/installation/)
- Opcional: [Virtualenv](https://virtualenv.pypa.io/en/latest/) para entornos virtuales

## Instalación

1. **Clona el repositorio**:

    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd <NOMBRE_DEL_REPOSITORIO>
    ```

2. **Crea un entorno virtual** (opcional pero recomendado):

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # Para macOS/Linux
    .venv\Scripts\activate     # Para Windows
    ```

3. **Instala las dependencias**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Ejecuta la aplicación**:

    ```bash
    streamlit run app.py
    ```

5. **Accede a la aplicación en el navegador**:
   Abre el enlace que aparece en la terminal (por ejemplo: `http://localhost:8501`).

## Estructura del proyecto

```plaintext
<REPOSITORIO>/
├── moodle_generator/
│   ├── __init__.py
│   ├── xml_generator.py
│   ├── models.py
├── gui_interface/
│   ├── __init__.py
│   ├── gui.py
├── app.py
├── requirements.txt
├── README.md
```

## Archivo `requirements.txt`

Incluye todas las dependencias necesarias para ejecutar el proyecto:
Ejecutá en la consola, si estás en el entorno virtual.

```plaintext
streamlit
```

## Uso de la interfaz gráfica

1. En la barra lateral, ingresa los valores base para los DATOS y selecciona el modelo matemático.
2. Especifica el número de preguntas que deseas generar.
3. Haz clic en "Generar preguntas" para obtener el XML.
4. Descarga el archivo generado haciendo clic en "Descargar archivo XML".

## Notas y futuras mejoras

- Modifica el archivo models.py para añadir o personalizar los modelos matemáticos.
- Asegúrate de importar correctamente las funciones en `gui.py` desde el módulo `models.py`.
