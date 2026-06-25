# 🚀 Proyecto Clientes API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![GitHub last commit](https://img.shields.io/github/last-commit/SteveCortesDev/Proyecto_Clientes)
![GitHub repo size](https://img.shields.io/github/repo-size/SteveCortesDev/Proyecto_Clientes)
![GitHub stars](https://img.shields.io/github/stars/SteveCortesDev/Proyecto_Clientes?style=social)

> **API RESTful** para gestión de clientes, facturas y transacciones, construida con **FastAPI** y **SQLModel**.

---
---

## ✨ Características

- ✅ **CRUD completo** para Clientes, Facturas y Transacciones
- ✅ **Validación de datos** con Pydantic
- ✅ **Documentación automática** con Swagger UI y ReDoc
- ✅ **Base de datos** con SQLModel (SQLite)
- ✅ **Relaciones** entre tablas (Cliente → Factura → Transacción)
- ✅ **Cálculo automático** del valor total de facturas
- ✅ **Manejo de errores** con HTTPException
- ✅ **Código modular** con routers y modelos separados
- ✅ **Control de versiones** con Git

📁 PROYECTO_CLIENTES/
├── 📄 .gitignore                 # Archivos ignorados por Git
├── 📄 requirements.txt           # Dependencias del proyecto
├── 📄 README.md                  # Documentación principal
├── 📄 main.py                    # Punto de entrada de la API
│
├── 📁 .mi_env/                   # Entorno virtual (ignorado)
│
└── 📁 app/
    ├── 📄 __init__.py
    ├── 📄 main.py                # Configuración principal de FastAPI
    ├── 📄 database.py            # Conexión a base de datos
    ├── 📄 listas.py              # Listas globales en memoria
    │
    ├── 📁 modelos/
    │   ├── 📄 __init__.py
    │   ├── 📄 clientes.py        # Modelo de Cliente
    │   ├── 📄 facturas.py        # Modelo de Factura
    │   └── 📄 transacciones.py   # Modelo de Transacción
    │
    └── 📁 enrutadores/
        ├── 📄 __init__.py
        ├── 📄 clientes.py        # Endpoints de Clientes
        ├── 📄 facturas.py        # Endpoints de Facturas
        └── 📄 transacciones.py   # Endpoints de Transacciones <br>
 👨‍💻 Autor
Steve Cortes Dev

GitHub: @SteveCortesDev
