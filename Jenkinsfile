pipeline {
    agent any

    environment {
        VENV_DIR = "venv"  
        GUNICORN_CMD = "gunicorn -b 127.0.0.1:8000 app:app"  
    }

    stages {
        // Stage 1: Checkout the Flask app from GitHub
        stage('Checkout SCM') {
            steps {
                git url: 'https://github.com/rahavcs/Go-Nexturn-Assignments.git', branch: 'main'
            }
        }

        // Stage 2: Set up Python virtual environment
        stage('Set up Virtual Environment') {
            steps {
                script {
                    // Create virtual environment
                    bat 'python -m venv ${VENV_DIR}'
                    // Ensure the virtual environment is activated
                    bat 'call ${VENV_DIR}\\Scripts\\activate.bat'
                }
            }
        }

        // Stage 3: Install dependencies
        stage('Install Dependencies') {
            steps {
                script {
                    // Install dependencies from requirements.txt
                    bat 'call ${VENV_DIR}\\Scripts\\pip install -r requirements.txt'
                }
            }
        }

        // Stage 4: Ensure pytest is installed
        stage('Ensure pytest') {
            steps {
                script {
                    // Ensure pytest is installed
                    bat 'call ${VENV_DIR}\\Scripts\\pip install pytest'
                }
            }
        }

        // Stage 5: Run Unit Tests with pytest
        stage('Run Unit Tests') {
            steps {
                script {
                    // Run the unit tests using pytest
                    bat 'call ${VENV_DIR}\\Scripts\\pytest tests'
                }
            }
        }

        // Stage 6: Start Gunicorn server
        stage('Start Gunicorn') {
            steps {
                script {
                    // Run Gunicorn server
                    bat 'call ${VENV_DIR}\\Scripts\\${GUNICORN_CMD}'
                }
            }
        }

        // Stage 7: Post-Deployment Endpoint Check
        stage('Post Deployment Check') {
            steps {
                script {
                    // Check the deployment using curl
                    bat 'curl http://127.0.0.1:8000'
                }
            }
        }
    }

    post {
        success {
            echo 'Flask application deployed successfully with Gunicorn!'
        }
        failure {
            echo 'Deployment failed!'
        }
    }
}
