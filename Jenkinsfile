pipeline {
    agent any

    environment {
        PYTHON_HOME = "C:\\Users\\C S Rahav\\python-3.13.1-amd64.exe"
        PATH = "${PYTHON_HOME};${env.PATH}"
    }

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    try {
                        git branch: 'main', url: 'https://github.com/rahavcs/Go-Nexturn-Assignments.git'
                    } catch (Exception e) {
                        error("Git clone failed. Verify branch name and repository URL.")
                    }
                }
            }
        }

        stage('Set up Python Environment') {
            steps {
                script {
                    // Clean up existing venv folder if it exists
                    bat 'rmdir /s /q venv'
                    
                    // Set up virtual environment and install dependencies
                    timeout(time: 3, unit: 'MINUTES') {
                        bat '"C:\\Users\\C S Rahav\\python-3.13.1-amd64.exe" -m venv venv'
                    }
                    timeout(time: 3, unit: 'MINUTES') {
                        bat 'venv\\Scripts\\activate && pip install --upgrade pip'
                    }
                    timeout(time: 5, unit: 'MINUTES') {
                        bat 'venv\\Scripts\\activate && pip install -r requirements.txt'
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    timeout(time: 3, unit: 'MINUTES') {
                        bat 'venv\\Scripts\\activate && pytest tests/'
                    }
                }
            }
        }

        stage('Start Gunicorn') {
            steps {
                script {
                    timeout(time: 3, unit: 'MINUTES') {
                        bat 'venv\\Scripts\\activate && gunicorn -w 4 -b 0.0.0.0:8000 app:app'
                    }
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    timeout(time: 2, unit: 'MINUTES') {
                        bat 'curl http://localhost:8000 || exit 1'
                    }
                }
            }
        }
    }

    post {
        always {
            // Clean up venv if it was created
            bat 'rmdir /s /q venv'
        }
    }
}
