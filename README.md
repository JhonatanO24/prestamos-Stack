<h1 align="center">📚 API de Préstamos - Biblioteca | FastAPI + React 📚</h1>

<p align="center">
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi" alt="FastAPI Badge"/>
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python Badge"/>
<img src="https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB Badge"/>
<img src="https://img.shields.io/badge/React-20232a?style=for-the-badge&logo=react" alt="React Badge"/>
<img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" alt="Vite Badge"/>
<img src="https://img.shields.io/badge/TailwindCSS-0f172a?style=for-the-badge&logo=tailwindcss" alt="Tailwind CSS Badge"/>
<img src="https://img.shields.io/badge/Docker-0db7ed?style=for-the-badge&logo=docker&logoColor=white" alt="Docker Badge"/>
<img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=swagger&logoColor=black" alt="Swagger Badge"/>
<img src="https://img.shields.io/badge/Pytest-0A9EDC?style=for-the-badge" alt="Pytest Badge"/>
</p>

---

## 🎯 Objetivo del Proyecto

<em>
Este proyecto fue desarrollado con el objetivo de demostrar habilidades Full Stack utilizando Python (FastAPI) en el backend, MongoDB como base de datos NoSQL y React con TailwindCSS en el frontend, integrando además Docker para facilitar el despliegue local.
</em>

---

## 📝 Descripción General

<em>
La API de Préstamos es un sistema que permite gestionar libros, usuarios y préstamos en una biblioteca.  
Incluye lógica de negocio real como el control de disponibilidad de libros, fechas de devolución, cálculo de retrasos y registro de devoluciones.  
El proyecto cuenta con una interfaz moderna, responsiva y con diseño oscuro gracias a TailwindCSS.
</em>

---

## 🚀 Funcionalidades Principales

### 1️⃣ Gestión de Libros
📚 Registro, consulta y actualización del estado de los libros (Disponible / Prestado).

---

### 2️⃣ Gestión de Usuarios
👤 Creación y administración de usuarios del sistema.

---

### 3️⃣ Préstamos con Lógica de Negocio
🧾 Registro de préstamos aplicando reglas reales:
- ✅ Validación de disponibilidad del libro
- ✅ Asignación automática de fecha de devolución
- ✅ Registro de devolución del libro
- ✅ Cambio automático de estado del libro

---

### 4️⃣ Cálculo de Retrasos
⏱️ Cálculo automático de días de retraso entre la fecha esperada y la fecha real de devolución.

---

### 5️⃣ Interfaz Frontend Moderna
🎨 Interfaz desarrollada con:
- ✅ React + Vite
- ✅ TailwindCSS
- ✅ Diseño oscuro con animaciones
- ✅ Notificaciones visuales (toasts)

---

### 6️⃣ Pruebas Unitarias con Pytest
🧪 Pruebas unitarias para validar:
- Cálculo correcto de retrasos
- Lógica de devolución

---

## 🛠 Tecnologías Utilizadas

| Tecnología         | Descripción                                       |
|--------------------|---------------------------------------------------|
| 🐍 Python 3        | Lenguaje principal del backend                    |
| ⚡ FastAPI         | Framework para construir la API REST              |
| 🍃 MongoDB         | Base de datos NoSQL                               |
| 📦 Pydantic       | Validación de datos                               |
| ⚛️ React           | Framework frontend                               |
| ⚡ Vite            | Bundler frontend rápido                          |
| 🎨 TailwindCSS    | Estilos del frontend                             |
| 🐳 Docker          | Contenedores para MongoDB                        |
| 🌐 Swagger UI     | Documentación interactiva de la API              |
| 🧪 Pytest          | Pruebas unitarias                                |

---

## 🖼️ Vista Previa del Proyecto

### 🏠 Home - Interfaz Principal

<img width="1902" height="672" alt="Captura de pantalla 2025-11-29 183938" src="https://github.com/user-attachments/assets/45cc257b-c342-4d92-895d-985476c4c8e0" />

### 📄 Documentación Swagger

<img width="1858" height="844" alt="Captura de pantalla 2025-11-29 190341" src="https://github.com/user-attachments/assets/7831000c-33b3-4901-ab99-cb13e4e7636b" />

## ⚙️ Instalación y Ejecución

### 1️⃣ Clonar el repositorio
```bash
git clone https://github.com/JhonatanO24/prestamos-Stack.git
```

## 🔧 Backend (FastAPI)

### 2️⃣ Crear entorno virtual e instalar dependencias
```bash
cd backend
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3️⃣ Levantar MongoDB con Docker
```bash
docker-compose up -d
```

### 4️⃣ Ejecutar el backend
```bash
uvicorn main:app --reload
```
Servidor activo en:
```arduino
http://localhost:8000
```
Swagger disponible en:
```bash
http://localhost:8000/docs
```

## 💻 Frontend (React + Vite)

### 5️⃣ Instalar dependencias del frontend
```bash
cd frontend
npm install
```

### 6️⃣ Ejecutar el frontend
```
npm run dev
```
Frontend activo en:
```arduino
http://localhost:5173
```

## 📁 Estructura del Proyecto

```plaintext
📦 backend/
├── main.py
├── models/
├── routes/
├── services/
├── database.py
└── requirements.txt

📦 frontend/
├── src/
│   ├── components/
│   ├── pages/
│   ├── api.js
│   ├── App.jsx
│   └── main.jsx
├── tailwind.config.js
└── vite.config.js

🐳 docker-compose.yml
```

🔥 Bt: Jhonatan :D
📌 Full Stack Developer / Backend
