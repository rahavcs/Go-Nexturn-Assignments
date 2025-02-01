pipeline {
    agent any
    environment {
        PYTHON = '"C:\\Users\\C S Rahav\\python-3.13.1-amd64.exe"'  // Adjusted path to Python executable
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

        // Stage 2: Setup Python (Check Python version)
        stage('Setup Python') {
            steps {
                bat '${PYTHON} --version'
            }
        }

        // Stage 3: Create Virtual Environment
        stage('Create Virtual Environment') {
            steps {
                bat '${PYTHON} -m venv ${VENV_DIR}'
            }
        }

        // Stage 4: Install Dependencies
        stage('Install Dependencies') {
            steps {
                script {
                    // Activate the virtual environment and install dependencies
                    bat '.\\${VENV_DIR}\\Scripts\\activate && pip install -r requirements.txt'
                }
            }
        }

        // Stage 5: Ensure pytest is installed
        stage('Ensure pytest') {
            steps {
                script {
                    // Ensure pytest is installed
                    bat 'call ${VENV_DIR}\\Scripts\\pip install pytest'
                }
            }
        }

        // Stage 6: Run Unit Tests with pytest
        stage('Run Unit Tests') {
            steps {
                script {
                    // Run the unit tests using pytest
                    bat 'call ${VENV_DIR}\\Scripts\\pytest tests'
                }
            }
        }

        // Stage 7: Start Gunicorn server
        stage('Start Gunicorn') {
            steps {
                script {
                    // Run Gunicorn server
                    bat 'call ${VENV_DIR}\\Scripts\\${GUNICORN_CMD}'
                }
            }
        }

        // Stage 8: Post-Deployment Endpoint Check
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

