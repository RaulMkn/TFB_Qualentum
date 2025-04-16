pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/RaulMkn/TFB_Qualentum'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Construir la imagen de Docker
                    sh 'docker build -t my-custom-python-docker .'
                }
            }
        }

        stage('Run Docker Image') {
            steps {
                script {
                    // Ejecutar el contenedor sin TTY
                    sh 'docker run --rm my-custom-python-docker'
                }
            }
        }

        stage('Push Docker image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    // Realizar login y subir la imagen a Docker Hub
                    docker.withRegistry('', 'dockerhub-creds') {
                        docker.image('my-custom-python-docker').push()
                    }
                }
            }
        }
    }
}
