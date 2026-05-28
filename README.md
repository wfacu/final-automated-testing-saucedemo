# SauceDemo | QA Automation Testing

Proyecto de automatización de pruebas realizado con Python, Selenium y Pytest sobre la página demo de SauceDemo.

## Tecnologías utilizadas

* Python
* Selenium WebDriver
* Pytest
* Pytest HTML

---

# Project Tree

```bash
project/
│
├── logs/
│   └── test_log.log
│
├── reports/
│   └── reporte.html
│
├── screenshots/
│   └── screenshots automáticos en caso de error
│
├── tests/
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_catalogo.py
│   └── test_carrito.py
│
├── utils/
│   └── functions.py
│
├── requirements.txt
└── README.md
```

---

# Funcionalidades automatizadas

## Login

* Inicio de sesión exitoso
* Verificación de redirección al catálogo

## Catálogo de productos

* Validación de productos visibles
* Verificación de menú lateral
* Verificación de filtro de productos

## Carrito

* Agregar productos al carrito
* Validación de contador del carrito
* Verificación de producto agregado

---

# Evidencias automáticas

El proyecto genera automáticamente:

## Logs de ejecución

Ubicación:

```bash
logs/test_log.log
```

Se registran eventos importantes de cada ejecución de tests.

## Screenshots automáticos

Ubicación:

```bash
screenshots/
```

Cuando un test falla, se genera automáticamente una captura de pantalla del error.

## Reporte HTML

Ubicación:

```bash
reports/reporte.html
```

Incluye el resultado completo de la ejecución de los tests. El mismo es modificado si se ejecuta nuevamente y, por ejemplo, un test diera error.

---

# Instalación

## 1. Clonar repositorio

```bash
git clone URL_DEL_REPOSITORIO
```

## 2. Ingresar a la carpeta

```bash
cd NOMBRE_DEL_PROYECTO
```

## 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución de tests

## Ejecutar todos los tests

```bash
pytest
```

## Ejecutar tests con detalle

```bash
pytest -v
```

## Generar reporte HTML

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

---

# Datos externos

Actualmente el proyecto no utiliza archivos externos como CSV o JSON.

---

Proyecto realizado por Facundo como práctica de QA Automation Testing.
