pipeline {
    agent any

    environment {
        PYTHON_HOME = "C:\\Users\\C S Rahav\\python-3.13.1-amd64.exe"
        PATH = "${PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/rahavcs/Go-Nexturn-Assignments.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                bat '"C:\\Users\\C S Rahav\\python-3.13.1-amd64.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install --upgrade pip && pip install -r requirements.txt'
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests/'
            }
        }

        stage('Start Gunicorn') {
            steps {
                bat 'venv\\Scripts\\activate && gunicorn -w 4 -b 0.0.0.0:8000 app:app'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'curl http://localhost:8000 || exit 1'
            }
        }
    }
}
