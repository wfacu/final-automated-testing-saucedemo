# final-automated-testing-saucedemo

Framework de automatización de pruebas desarrollado sobre https://www.saucedemo.com/ para pruebas de interfaz web y https://reqres.in/ para pruebas de API.

El proyecto implementa Selenium WebDriver, Pytest, Requests y el patrón de diseño Page Object Model (POM), además de reportes HTML, logging y capturas automáticas en caso de error.

---

# Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Requests
- Pytest HTML
- Git
- GitHub

---

# Estructura del proyecto

```text
final-automated-testing-saucedemo/
│
├── logs/
│   └── test_log.log
│
├── pages/
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   └── checkout_page.py
│
├── reports/
│   └── reporte.html
│
├── screenshots/
│   └── capturas automáticas en caso de error
│
├── test_data/
│   └── users.json
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_login_invalido.py
│   ├── test_catalogo.py
│   ├── test_carrito.py
│   ├── test_checkout.py
│   ├── test_api_get.py
│   ├── test_api_post.py
│   └── test_api_delete.py
│
├── utils/
│   └── functions.py
│
├── requirements.txt
└── README.md
```

---

# Funcionalidades implementadas

## Pruebas UI

- Login exitoso
- Login con credenciales inválidas
- Validación del catálogo de productos
- Agregado de productos al carrito
- Flujo completo de checkout

---

## Pruebas API

- Peticiones GET
- Peticiones POST
- Peticiones DELETE
- Validación de códigos de estado HTTP
- Validación del contenido de las respuestas JSON

---

## Page Object Model

La automatización de la interfaz web se encuentra organizada utilizando el patrón **Page Object Model (POM)**, separando la lógica de interacción con la aplicación de la lógica de las pruebas.

---

# Evidencias automáticas

## Logging

Durante la ejecución se genera un archivo de log en:

```text
logs/
```

El mismo registra los principales eventos de la ejecución para facilitar la depuración.

---

## Screenshots automáticos

Cuando una prueba falla, automáticamente se genera una captura de pantalla en:

```text
screenshots/
```

El nombre del archivo incluye el nombre del test y la fecha/hora de ejecución.

---

## Reporte HTML

Los resultados pueden visualizarse mediante un reporte HTML generado en:

```text
reports/
```

El reporte muestra:

- Tests ejecutados
- Estado de cada prueba
- Tiempo de ejecución
- Información detallada de los resultados

---

# Datos de prueba

Los datos utilizados para las pruebas parametrizadas se almacenan en archivos JSON dentro de:

```text
test_data/
```

---

# Instalación

## Clonar el repositorio

```bash
git clone https://github.com/wfacu/final-automated-testing-saucedemo.git
```

## Ingresar al proyecto

```bash
cd final-automated-testing-saucedemo
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución

## Ejecutar todas las pruebas

```bash
pytest
```

## Ejecutar en modo verbose

```bash
pytest -v
```

## Generar reporte HTML

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

---

# Autor

Facundo
