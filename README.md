# 🚀 Proyecto Clientes API

![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)

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

📁 PROYECTO_CLIENTES/<br>
├── 📄 .gitignore                 # Archivos ignorados por Git<br>
├── 📄 requirements.txt           # Dependencias del proyecto<br>
├── 📄 README.md                  # Documentación principal<br>
├── 📄 main.py                    # Punto de entrada de la API<br>
│<br>
├── 📁 .mi_env/                   # Entorno virtual (ignorado)<br>
│<br>
└── 📁 app/<br>
    ├── 📄 __init__.py
    ├── 📄 main.py                # Configuración principal de FastAPI<br>
    ├── 📄 database.py            # Conexión a base de datos<br>
    ├── 📄 listas.py              # Listas globales en memoria<br>
    │<br>
    ├── 📁 modelos/<br>
    │   ├── 📄 __init__.py
    │   ├── 📄 clientes.py        # Modelo de Cliente<br>
    │   ├── 📄 facturas.py        # Modelo de Factura<br>
    │   └── 📄 transacciones.py   # Modelo de Transacción<br>
    │<br>
    └── 📁 enrutadores/<br>
        ├── 📄 __init__.py<br>
        ├── 📄 clientes.py        # Endpoints de Clientes<br>
        ├── 📄 facturas.py        # Endpoints de Facturas<br>
        └── 📄 transacciones.py   # Endpoints de Transacciones <br>
 👨‍💻 Autor
Steve Cortes Dev

GitHub: @SteveCortesDev
