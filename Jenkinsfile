pipeline {
    agent any

    // Environment variables
    environment {
        NODE_VERSION = '18.x'  // Specify Node.js version
        DEPLOY_DIR = 'D:\\react'  // Deployment directory (use double backslashes)
        GITHUB_REPO = 'https://github.com/rahavcs/Assignments.git'  // Replace with your repo
    }

    // Tool configurations
    tools {
        nodejs 'Node-18'  // Make sure this matches your Jenkins NodeJS installation name
    }

    stages {
        stage('Checkout') {
            steps {
                // Clean workspace before checking out code
                cleanWs()
                echo 'Cloning repository...'
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat 'npm install'
            }
        }

        stage('Lint') {
            steps {
                echo 'Running ESLint...'
                bat 'npm run lint || exit /b 0'  // Prevent pipeline failure on lint warnings
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'npm test -- --watchAll=false'
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                bat 'npm run build'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Create deployment directory if it doesn't exist
                bat "if not exist ${DEPLOY_DIR} mkdir ${DEPLOY_DIR}"
                
                // Remove old deployment files
                bat "rmdir /S /Q ${DEPLOY_DIR}\\*"
                
                // Copy new build files
                bat "xcopy /E /I /Y build\\* ${DEPLOY_DIR}\\"
            }
        }

        stage('Post-Deployment Test') {
            steps {
                echo 'Testing deployed application...'
                // Wait for application to be ready
                bat 'timeout /t 10 /nobreak >nul'
                
                // Test if the application is accessible
                script {
                    def response = bat(
                        script: 'powershell -Command "(Invoke-WebRequest -Uri http://localhost -UseBasicParsing).StatusCode"',
                        returnStdout: true
                    ).trim()
                    
                    if (response != "200") {
                        error "Deployment verification failed. HTTP status code: ${response}"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed! Check the logs for details.'
        }
        always {
            // Clean workspace after pipeline completion
            cleanWs()
        }
    }
}
