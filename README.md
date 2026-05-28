# automated-testing-saucedemo

Proyecto de automatización de pruebas sobre la página https://www.saucedemo.com/.

## Tecnologías usadas

* Python
* Selenium WebDriver
* Pytest
* Pytest HTML

---

# Estructura del proyecto

```txt
automated-testing-saucedemo/
│
├── logs/
│   └── test_log.log
│
├── reports/
│   └── reporte.html
│
├── screenshots/
│   └── capturas automáticas en caso de error
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

# ¿Qué valida este proyecto?

## Login

* Inicio de sesión correcto
* Validación de acceso al inventario

## Catálogo

* Verificación de productos visibles
* Validación de menú lateral
* Validación de filtro de productos

## Carrito

* Agregar productos al carrito
* Verificación del contador
* Validación del producto agregado

---

# Evidencias automáticas

## Logs

Durante cada ejecución se genera un archivo `.log` dentro de:

```bash
logs/
```

El mismo registra eventos importantes de los tests ejecutados.

---

## Screenshots automáticos

Si un test falla, automáticamente se genera una captura de pantalla dentro de:

```bash
screenshots/
```

---

## Reporte HTML

Los reportes HTML se generan dentro de:

```bash
reports/
```

---

# Instalación

## Clonar repositorio

```bash
git clone https://github.com/wfacu/automated-testing-saucedemo.git
```

## Entrar al proyecto

```bash
cd automated-testing-saucedemo
```

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Ejecución de tests

## Ejecutar todos los tests

```bash
pytest
```

## Ejecutar tests en modo verbose

```bash
pytest -v
```

## Generar reporte HTML

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

---

# Datos externos

Actualmente el proyecto no utiliza archivos CSV o JSON externos.
