pipeline {
    agent any

    environment {
        PYTHON_HOME = "C:\\Users\\C S Rahav\\python-3.13.1-amd64.exe"
        PATH = "${PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/rahavcs/Go-Nexturn-Assignments.git'
            }
        }

        stage('Set up Python Environment') {
            steps {
                bat 'if exist venv rmdir /s /q venv'  // Clean up any previous virtual environment
                bat '"C:\\Users\\C S Rahav\\python-3.13.1-amd64.exe" -m venv venv'  // Create new virtual environment
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt'  // Install dependencies
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat 'venv\\Scripts\\activate && pytest tests/'
            }
        }

        stage('Start Gunicorn') {
            steps {
                bat 'venv\\Scripts\\activate && gunicorn -b 127.0.0.1:8000 app:app'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'curl http://127.0.0.1:8000 || exit 1'  // Check if the Flask app is accessible
            }
        }
    }
}
