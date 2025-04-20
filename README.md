
# 🧱 Arquitectura de la Solución

## 📜 Descripción de la Arquitectura del Sistema
El proyecto está organizado como una aplicación web en **Flask** con conexión a base de datos PostgreSQL y una pipeline creada con Jenkins para la automatización de tests. La estructura principal es:

```
TFB_Qualentum/
├── app/                  # Código fuente de la aplicación Flask
│   ├── __init__.py       # Inicializa la app y configura extensiones
│   ├── models.py         # Definición de modelos con SQLAlchemy
│   └── routes.py         # Endpoints RESTful y lógica de rutas
├── tests/                # Pruebas unitarias y de integración
│   ├── test_models.py    # Pruebas para los modelos
│   └── test_routes.py    # Pruebas para las rutas
├── Jenkinsfile           # Pipeline CI/CD para Jenkins
├── job.xml               # Configuración del job de Jenkins
├── dockerfile            # Define la imagen Docker de la aplicación
├── manage.py             # Script de gestión para tareas administrativas
├── pytest.ini            # Configuración de pytest
├── requirements.txt      # Dependencias de Python
├── run.py                # Punto de entrada principal de la aplicación
└── README.md             # Documentación del proyecto
```

- **Flask App**: En `app/__init__.py` se crea la instancia de Flask y se inicializa SQLAlchemy.
- **Modelos de datos**: `app/models.py` define las entidades y relaciones.
- **Rutas/Controladores**: `app/routes.py` expone los endpoints de la API.

## Requisitos previos

- Docker instalado en tu máquina
- Python 3.8 o superior
- Credenciales de acceso a la base de datos (solicitar al equipo)

### 🔧 Componentes Principales

1. **Aplicación Web en Python**: La aplicación principal que será desplegada en producción.  
2. **Entorno de Desarrollo Local**: Basado en Docker para garantizar consistencia entre desarrolladores.  
3. **Base de Datos Online**: Hosteada en Render, permite acceso colaborativo en tiempo real.  
4. **Pipeline CI/CD**: Implementada con Jenkins para automatización de pruebas y despliegues.  
5. **Gestión de Configuración**: Uso de variables de entorno para manejar credenciales y configuraciones sensibles.

---

## 🧭 Diagrama de Arquitectura General  
![General Diagram](images/GeneralDiagram.png)

---

## 💻 Tecnologías Utilizadas

- **Docker**: Para entornos de desarrollo consistentes.  
- **Render**: Servicio de base de datos online para desarrollo colaborativo.  
- **Jenkins**: Para la automatización del ciclo CI/CD.  
- **Python/Flask**: Framework principal para la aplicación web.

---

## ☁️ Arquitectura Cloud (AWS)

Aunque el desarrollo se realiza localmente, la solución está diseñada para escalar hacia AWS utilizando los siguientes servicios:

### 🔌 Servicios AWS Propuestos

1. **EC2**: Para alojar la aplicación en contenedores Docker.  
2. **RDS**: Base de datos gestionada en producción.  
3. **Elastic Load Balancing**: Distribución de tráfico entre instancias.  
4. **CloudWatch**: Monitoreo y gestión de logs.  
5. **ECS/EKS**: Orquestación de contenedores.  
6. **S3**: Almacenamiento de artefactos y copias de seguridad.

![AWS Diagram](images/AWSDiagram.png)


---

# 🔄 Ciclo de Vida del Proyecto

## 🧩 Modelo de Desarrollo

### 1. Flujo de Trabajo (Git Flow simplificado)

#### 🔄 Trabajo sobre la rama `develop`

Todos los desarrolladores deben partir siempre de `develop`:

```bash
git fetch origin
git checkout develop
```

#### 🌱 Creación de ramas de feature

Las nuevas funcionalidades o correcciones se desarrollan a partir de `develop`, siguiendo la convención `feature/<descripcion-corta>`:

```bash
git checkout -b feature/nombre-breve develop
```

#### 📝 Commits

- Commits **atómicos** (un cambio por commit).
- Mensajes **claros**, en **estilo imperativo** y en **inglés**.  
  Ejemplo: `Add login validation for empty fields`

#### 🚫 Push directo a `main` o `develop`

- Todos los cambios deben pasar por un **Pull Request (PR)** revisado y aprobado.

#### ✅ Antes de abrir un PR

1. Actualiza tu rama con los últimos cambios de `develop`:  
   ```bash
   git pull origin develop
   ```

2. Ejecuta todos los tests y asegúrate de que pasen correctamente.  
3. Verifica que la cobertura de pruebas no disminuya.

#### 👁️ Revisión de Código

- Etiqueta al menos **un revisor**.  
- Añade una **descripción breve** del cambio en el PR.

#### 🔀 Merge de PRs

- Usa la estrategia **Squash and Merge** para un historial limpio.

---

### 2. Entornos

- **Local**: Docker + Render para desarrollo colaborativo.  
- **Staging**: Réplica del entorno de producción.  
- **Producción**: Desplegado en AWS.

---

### 3. Pruebas

- **Tests unitarios** con cobertura superior al 80%.  
- **Tests de integración** usando la base de datos real.  
- **Linting** con `flake8`, siguiendo la guía PEP8.

---

# ⚙️ Operaciones

## 1. Despliegue

- Estrategia **Blue-Green** en EC2 usando **Ansible** *(plan futuro)*.  
- **Rollback automático** si fallan los health checks.

## 2. Monitorización

- Uso de **CloudWatch** para métricas y logs.  
- Configuración de **alertas**.

---

# 💻 Implementación Actual Detallada

## 1. Entorno Local de Desarrollo

### 🔧 Configuración

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/RaulMkn/TFB_Qualentum.git
   cd TFB_Qualentum
   ```

2. Crear archivo `.env` basado en `.env.example`:
   ```ini
   DB_URL=postgresql://usuario:contraseña@host:5432/nombre_db
   FLASK_APP=app.py
   ```

3. Construir y levantar el contenedor Docker:
   ```bash
   docker build -t tfb_app .
   docker run -d --name tfb_app -p 5000:5000 --env-file .env tfb_app
   ```

   - La aplicación estará disponible en `http://localhost:5000`.
   - Para detenerla: `docker stop tfb_app && docker rm tfb_app`.

## Ejecución de tests

Todas las pruebas se ejecutan con **pytest** y generan reporte de cobertura.

- Para ejecutar pruebas locales:
  ```bash
  pytest --cov=app tests/
  ```

- Para generar reporte HTML de cobertura:
  ```bash
  pytest --cov-report html --cov=app tests/
  ```

> **Tip**: Asegúrate de que el contenedor Docker esté corriendo y la variable `DB_URL` apunte a una base de datos de test limpia.

## Normas de colaboración

Para mantener un flujo de trabajo ordenado y colaborativo:

1. Trabaja siempre sobre la rama `develop`:
   ```bash
   git fetch origin
   git checkout develop
   ```

2. Crea ramas de feature siguiendo el patrón:
   ```bash
   git checkout -b feature/<descripcion-corta> develop
   ```

3. Realiza commits atómicos con mensajes claros (imperativos, en inglés).

4. No hacer push directo a `main` ni `develop`. Los PR deben revisarse y aprobarse antes de merge.

5. Antes de abrir un PR:
   - Actualiza la rama con `develop`: `git pull origin develop`.
   - Verifica que todos los tests pasen.
   - Asegúrate de que la cobertura de tests no disminuya.

6. Revisión de código:
   - Etiqueta a al menos un revisor.
   - Describe brevemente qué hace el cambio.

7. Merge:
   - Se realizará mediante **Squash and Merge** para mantener un historial limpio.

---

## 2. Pipeline CI con Jenkins

### 🔹 Levantar Jenkins con Docker

```bash
docker run -d   --name jenkins   -p 8080:8080   -p 50000:50000   -v jenkins_home:/var/jenkins_home   jenkins/jenkins:lts
```

- Acceder vía navegador: `http://localhost:8080`
- Contraseña inicial:
  ```bash
  docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
  ```

---

### 🔹 Exponer Jenkins con Ngrok

```bash
ngrok http 8080
```

- Usa la URL proporcionada por Ngrok (ej. `https://a1b2c3d4.ngrok.io`)

---

### 🔹 Descargar Jenkins CLI

```bash
curl -O http://localhost:8080/jnlpJars/jenkins-cli.jar
```

```bash
java -jar jenkins-cli.jar -s http://localhost:8080/ help
```

---

### 🔹 Crear un Job desde el CLI usando `job.xml`

```bash
java -jar jenkins-cli.jar -s http://localhost:8080 create-job qualentum-ci < job.xml
```

Con autenticación:

```bash
java -jar jenkins-cli.jar -s http://localhost:8080 -auth raulmkn:miToken123 create-job qualentum-ci < job.xml
```

---

### 🔹 Configurar el Webhook en GitHub

1. Ir a **Settings > Webhooks > Add webhook**  
2. Completar:
   - Payload URL: `https://<tu-url-ngrok>/github-webhook/`
   - Content type: `application/json`
   - Events: `Just the push event` o `Send me everything`

---

### 🔹 Conectar el Webhook con Jenkins

1. Edita el job `qualentum-ci`.  
2. Marca la opción: **GitHub hook trigger for GITScm polling**

---

### 🔹 Etapas del Pipeline

1. **Clone**: Clona el repositorio desde GitHub.  
2. **Test**: Ejecuta los tests unitarios con `pytest`.  
3. **Lint**: Aplica `flake8` sobre el directorio `app/` (cumplimiento de PEP8).  
4. **Build**: Construye una imagen Docker usando el `Dockerfile`.  
5. **Push**: Publica la imagen a Docker Hub si estás en `develop`, `master` o `main`.

---

![Jenkins Diagram](images/JenkinsFlowDiagram.png)


---
# ❗ Problemas y Soluciones

### 🌍 Jenkins Local + Webhooks

- **Problema**: Jenkins no accesible desde internet.  
- **Solución**: Usar **Ngrok** para exponer el puerto 8080.

### 🧵 Base de Datos Compartida

- **Problema**: Contenedor local no permite colaboración.  
- **Solución**: Usar **Render.com** para compartir la base de datos.

### 🔐 Variables Sensibles

- **Problema**: Credenciales expuestas en el código.  
- **Solución**: `.env` ignorado por Git y compartido de forma segura.

---

## 📊 Diagramas Adicionales

![General Diagram](images/DevSec.png)
