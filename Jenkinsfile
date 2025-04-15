pipeline {
    agent {
        docker {
            image 'python:3.11'
            args '-u root' 
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
                sh 'pip install --upgrade pip'
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 app'
            }
        }

        stage('Run tests') {
            steps {
                sh 'pip install pytest pytest-cov'
                sh 'pytest --cov=app tests/'
            }
        }

        stage('Build Docker image') {
            steps {
                // Ejecutar fuera del contenedor Python
                script {
                    docker.image('docker:latest').inside('--privileged -v /var/run/docker.sock:/var/run/docker.sock') {
                        sh 'docker build -t myapp .'
                    }
                }
            }
        }

        stage('Push Docker image') {
            when {
                branch 'main'
            }
            steps {
                script {
                    docker.image('docker:latest').inside('--privileged -v /var/run/docker.sock:/var/run/docker.sock') {
                        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                            sh '''
                                echo "$PASS" | docker login -u "$USER" --password-stdin
                                docker tag myapp $USER/myapp
                                docker push $USER/myapp
                            '''
                        }
                    }
                }
            }
        }
    }
}
