pipeline {
    agent any

    environment {
        FLASK_ENV = "testing"
        VENV = ".venv"
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
                sh 'python3 -m venv $VENV'
                sh '. $VENV/bin/activate && pip install --upgrade pip'
                sh '. $VENV/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                sh '. $VENV/bin/activate && pip install flake8'
                sh '. $VENV/bin/activate && flake8 app || exit 1'
            }
        }

        stage('Run tests') {
            steps {
                sh '. $VENV/bin/activate && pip install pytest pytest-cov'
                sh '. $VENV/bin/activate && pytest --cov=app --maxfail=3 tests/'
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
