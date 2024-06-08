
# Proyecto Hinner

Este proyecto proporciona una aplicación de Streamlit que permite analizar y visualizar árboles de sintaxis abstracta (AST) generados a partir de una gramática definida en ANTLR. La gramática específica se utiliza para analizar expresiones lambda y aplicaciones en un lenguaje definido.

## Contenido

- [Descripción](#descripción)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuciones](#contribuciones)
- [Licencia](#licencia)

## Descripción

La aplicación `Hinner` permite a los usuarios ingresar texto conforme a una gramática definida y generar un árbol de sintaxis abstracta (AST) que se visualiza mediante Graphviz. Además, analiza y muestra las definiciones de tipos de las variables y expresiones dentro del texto ingresado.

## Instalación

Para ejecutar esta aplicación localmente, sigue estos pasos:

1. Clona el repositorio:

   ```bash
   git clone https://github.com/tu_usuario/hinner.git
   cd hinner
   ```

2. Crea un entorno virtual (opcional pero recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. Instala las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Uso

Para iniciar la aplicación de Streamlit, ejecuta:

```bash
streamlit run hinner.py
```

Luego, abre tu navegador web y navega a `http://localhost:8501` para ver la aplicación en acción. 

### Interacción con la Aplicación

1. Introduce el texto que deseas analizar en el área de texto proporcionada.
2. Haz clic en el botón "Run" para procesar el texto.
3. La aplicación mostrará las definiciones y el árbol de sintaxis generado.

## Estructura del Proyecto

- `hinner.py`: El archivo principal que contiene la aplicación de Streamlit, la definición de la gramática, y las funciones necesarias para analizar y visualizar el AST.
- `hinnerLexer.py`, `hinnerParser.py`, `hinnerVisitor.py`: Archivos generados por ANTLR a partir de la gramática definida.

## Contribuciones

¡Las contribuciones son bienvenidas! Si deseas contribuir, por favor sigue estos pasos:

1. Haz un fork del proyecto.
2. Crea una rama con tu nueva característica (`git checkout -b feature/nueva-caracteristica`).
3. Realiza tus cambios y haz commits (`git commit -am 'Añadir nueva característica'`).
4. Sube los cambios a tu repositorio (`git push origin feature/nueva-caracteristica`).
5. Crea un Pull Request.

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para obtener más detalles.
