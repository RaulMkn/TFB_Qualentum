
# 🏁 Reto Final DevOps – Qualentum Bootcamp

Este proyecto es una API RESTful básica para la gestión de datos de ejemplo (CRUD), desarrollada con **Flask** y gestionada bajo un enfoque **DevOps** integral: testing automatizado, contenedores Docker, integración continua con Jenkins y cumplimiento de buenas prácticas de desarrollo.

---

## 🚀 Tecnologías utilizadas

- **Python 3.11**
- **Flask**
- **SQLAlchemy**
- **Pytest**
- **Docker**
- **Jenkins**
- **Flake8**

---

## ⚙️ Estructura de entornos

El proyecto está preparado para ejecutarse en tres entornos distintos:

| Entorno     | FLASK_ENV     | Base de datos                      |
|-------------|---------------|------------------------------------|
| Development | `development` | SQLite persistente (`dev.db`)     |
| Testing     | `testing`     | SQLite en memoria (`:memory:`)    |
| Production  | `production`  | Se define mediante `DATABASE_URI` |

---

## 🧪 Testing

Se utilizan `pytest` y `pytest-cov` para verificar el correcto funcionamiento de la API y generar reportes de cobertura.

### 🔧 Ejecutar tests localmente

1. Instala las dependencias:

```bash
pip install -r requirements.txt
```

2. Ejecuta los tests en entorno de testing:

```bash
FLASK_ENV=testing pytest --cov=app tests/
```

---

## 🐳 Docker

La aplicación está dockerizada para facilitar su ejecución y despliegue en distintos entornos.

### 🔨 Construir la imagen

```bash
docker build -t myapp .
```

### ▶️ Ejecutar contenedor en modo desarrollo

```bash
docker run -e FLASK_ENV=development -p 5000:5000 myapp
```

Luego accede a [http://localhost:5000/data](http://localhost:5000/data) o ejecuta:

```bash
curl -X POST -H "Content-Type: application/json"   -d '{"name": "Test"}' http://localhost:5000/data
```

---

## 🧪 Verificación de configuración

### ✅ 1. Docker funcionando correctamente

```bash
docker build -t myapp .
docker run -e FLASK_ENV=development -p 5000:5000 myapp
```

### ✅ 2. Tests funcionando correctamente

```bash
FLASK_ENV=testing pytest --cov=app tests/
```

### ✅ 3. Jenkins funcionando localmente

#### a) Levantar Jenkins en contenedor

```bash
docker run -u root --rm -d -p 8080:8080 -p 50000:50000   -v jenkins_home:/var/jenkins_home   -v /var/run/docker.sock:/var/run/docker.sock   jenkins/jenkins:lts
```

Abre Jenkins en [http://localhost:8080](http://localhost:8080)

#### b) Configurar un nuevo pipeline

1. Crea un nuevo **Job** de tipo **Pipeline**.
2. Marca la opción **"Pipeline script from SCM"** si el repositorio está en Git.
3. O pega directamente el contenido del `Jenkinsfile`.
4. Asegúrate de definir la variable `FLASK_ENV=testing`.

---

## 📁 Estructura del repositorio

```text
reto_final/
├── app/              # Código fuente
├── tests/            # Tests unitarios
├── Dockerfile        # Imagen para contenedor
├── Jenkinsfile       # Pipeline declarativa
├── requirements.txt  # Dependencias
├── run.py            # Punto de entrada principal
└── README.md         # Documentación del proyecto
```

---

## 📚 Endpoints disponibles

| Método | Ruta    | Descripción             |
|--------|---------|-------------------------|
| GET    | /data   | Obtener todos los datos |
| POST   | /data   | Crear nuevo dato        |

---

## 📥 Instalación local (sin Docker)

1. Clona el repositorio:

```bash
git clone https://github.com/tuusuario/reto_final.git
cd reto_final
```

2. Instala las dependencias:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. Ejecuta la app:

```bash
FLASK_ENV=development python run.py
```

---

## 🧾 Requisitos

- Python >= 3.10
- Docker (opcional, pero recomendado)
- Jenkins (local o en servidor)
  - Plugins necesarios: **Pipeline**, **Git**, **Docker Pipeline**
- Credenciales DockerHub (solo si se realiza push de imágenes)

---

## 🧠 Buenas prácticas aplicadas

- Uso de `flake8` para asegurar estilo de código.
- Cobertura de pruebas con `pytest-cov`.
- Separación clara de entornos (dev, test, prod).
- Uso de `Dockerfile` limpio y optimizado.
- Integración continua con `Jenkinsfile` declarativo.

---

## 👨‍💻 Autor

Proyecto realizado por **Tu Nombre** como entrega final del Bootcamp DevOps de Qualentum.

- GitHub: [https://github.com/tuusuario](https://github.com/tuusuario)
- LinkedIn: [https://linkedin.com/in/tuusuario](https://linkedin.com/in/tuusuario)

---

## 📚 Recursos útiles

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pytest](https://docs.pytest.org/)
- [Docker](https://docs.docker.com/)
- [Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/)
- [PEP8 – Guía de estilo de Python](https://peps.python.org/pep-0008/)
