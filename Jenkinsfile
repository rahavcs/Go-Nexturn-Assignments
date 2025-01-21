pipeline {
    agent any

    environment {
        VIRTUAL_ENV = 'venv'
        FLASK_APP = 'app:app' // Adjust to your application file
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/rahavcs/Assignments.git'
            }
        }

        stage('Set Up Python Virtual Environment') {
            steps {
                bat 'python -m venv $VIRTUAL_ENV'  // Create virtual environment
                bat '$VIRTUAL_ENV\\Scripts\\activate.bat'  // Activate the virtual environment
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '$VIRTUAL_ENV\\Scripts\\pip install -r requirements.txt'  // Install requirements
            }
        }

        stage('Run Unit Tests') {
            steps {
                bat '$VIRTUAL_ENV\\Scripts\\pytest'  // Run tests using pytest
            }
        }

        stage('Configure and Start Gunicorn') {
            steps {
                bat '$VIRTUAL_ENV\\Scripts\\gunicorn -b 127.0.0.1:8000 app:app'  // Start Gunicorn
            }
        }

        stage('Post-Deployment Check') {
            steps {
                script {
                    try {
                        // Run a curl command to check if the app is running
                        def response = bat(script: 'curl -s http://127.0.0.1:8000', returnStdout: true).trim()
                        echo "Response: ${response}"
                    } catch (Exception e) {
                        error "Deployment failed: ${e}"
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Cleaning up after deployment.'
            bat 'taskkill /IM gunicorn.exe /F || echo "Gunicorn not running"'  // Kill Gunicorn process
        }
    }
}
