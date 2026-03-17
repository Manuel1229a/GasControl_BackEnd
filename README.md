# 🚀 GasControl API

Sistema backend para la gestión de distribución de gas, enfocado en operadores que necesitan administrar clientes, pedidos e inventario de manera eficiente.

## 🧠 Descripción

GasControl es una API REST desarrollada con FastAPI que permite:

- Gestión de clientes
- Registro de pedidos
- Control de inventario de gas
- Base para futura integración con rutas inteligentes y analítica financiera

Este proyecto está diseñado con una arquitectura escalable, separando responsabilidades en capas (controllers, services, models).

---

## 🛠️ Tecnologías

- Python
- FastAPI
- SQLAlchemy
- SQLite (preparado para PostgreSQL)
- Uvicorn

---

## 🏗️ Arquitectura

El proyecto sigue una arquitectura por capas:

/app
/controllers → Manejo de endpoints
/services → Lógica de negocio
/models → Modelos de base de datos
/schemas → Validación de datos (Pydantic)
/database → Configuración de DB


---

## ⚙️ Instalación

1. Clonar el repositorio:

git clone <repo-url>
cd gas-control-backend


2. Crear entorno virtual:

python -m venv venv


3. Activar entorno:

Windows:

venv\Scripts\activate


4. Instalar dependencias:

pip install -r requirements.txt


---

## ▶️ Ejecución


uvicorn main:app --reload


Servidor disponible en:

http://127.0.0.1:8000


---

## 🧪 Documentación API

FastAPI genera documentación automática en:


http://127.0.0.1:8000/docs


---

## 📦 Módulos actuales

- ✅ Clientes
- ⏳ Pedidos (en desarrollo)
- ⏳ Inventario (en desarrollo)
- ⏳ Dashboard (en desarrollo)

---

## 🔮 Futuras mejoras

- Autenticación con JWT
- Integración con mapas para optimización de rutas
- Dashboard financiero avanzado
- Migración a PostgreSQL en producción
- Dockerización del sistema

---

## 💡 Decisiones técnicas

- Uso de SQLite para desarrollo rápido
- Arquitectura desacoplada para facilitar escalabilidad
- Uso de ORM (SQLAlchemy) para abstracción de base de datos

---

## 👨‍💻 Autor

Desarrollado por Carlos Hernández