pipeline {
    agent any

    // Environment variables
    environment {
        NODE_VERSION = '18.x'  // Node.js version
        DEPLOY_DIR = 'D:\\react'  // Deployment directory
        GITHUB_REPO = 'https://github.com/rahavcs/Assignments.git'  // Repository URL
    }

    // Tool configurations
    tools {
        nodejs 'Node-18'  // NodeJS installation in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs()  // Clean workspace
                echo 'Cloning repository...'
                git branch: 'main', url: "${GITHUB_REPO}"  // Clone repository
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing dependencies...'
                bat 'npm install'  // Install dependencies on Windows
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                bat 'npm run build'  // Build the application
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                bat 'mkdir "%DEPLOY_DIR%"'  // Create deployment directory
                bat 'rmdir /S /Q "%DEPLOY_DIR%"'  // Remove old deployment files
                bat 'xcopy /E /I /H /Y build\\* "%DEPLOY_DIR%\\\\"'  // Copy new build files
            }
        }

        stage('Post-Deployment Test') {
            steps {
                echo 'Testing deployed application...'
                bat 'timeout /t 10'  // Wait for 10 seconds
                script {
                    def response = bat(
                        script: 'curl -s -o nul -w "%{http_code}" http://localhost',
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
            cleanWs()  // Clean workspace after pipeline completion
        }
    }
}
