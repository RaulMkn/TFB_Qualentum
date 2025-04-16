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
                sh 'python -m venv venv'
                sh '. venv/bin/activate && pip install --upgrade pip'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh 'pip install flake8'
                sh 'flake8 app || exit 1'
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
                    docker.withRegistry('', 'dockerhub-creds') {
                        docker.image('myapp').push()
                    }
                }
            }
        }
    }
}
