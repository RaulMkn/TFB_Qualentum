pipeline {
    agent {
        docker {
            image 'my-custom-python-docker'  // Usar tu imagen personalizada
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'  // Montar el socket de Docker
        }
    }

    environment {
        FLASK_ENV = "testing"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/RaulMkn/TFB_Qualentum'
            }
        }

        stage('Install dependencies') {
            steps {
                // Aquí ya no necesitas instalar Docker, ya está en la imagen personalizada
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh '. venv/bin/activate && pip install flake8'
                sh '. venv/bin/activate && flake8 app || exit 1'
            }
        }

        stage('Run tests') {
            steps {
                sh '. venv/bin/activate && pip install pytest pytest-cov'
                sh '. venv/bin/activate && pytest --cov=app --maxfail=3 tests/'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    // Construcción de la imagen Docker
                    docker.build('myapp')
                }
            }
        }

        stage('Push Docker image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Subir la imagen a Docker Hub con las credenciales almacenadas en Jenkins
                    docker.withRegistry('', 'dockerhub-creds') {
                        docker.image('myapp').push()
                    }
                }
            }
        }
    }
}
