pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root -v /var/run/docker.sock:/var/run/docker.sock'  // Montar el socket Docker del host
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
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh '. venv/bin/activate && pip install flake8'
                sh '. venv/bin/activate && flake8 app || exit 1'  // Corrección: Llamada de flake8 con la activación del entorno
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
                        docker.image('myapp').push()  // Push de la imagen
                    }
                }
            }
        }
    }
}
