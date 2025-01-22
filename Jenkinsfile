pipeline {
    agent any

    // Environment variables
    environment {
        NODE_VERSION = '18.x'  // Specify Node.js version
        DEPLOY_DIR = 'D:\\react'  // Deployment directory (escape backslashes)
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
                bat 'npm install'  // Use 'bat' for Windows
            }
        }

        stage('Lint') {
            steps {
                echo 'Running ESLint...'
                bat 'npm run lint || exit 0'  // Use 'exit 0' instead of 'true' in Windows batch
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                bat 'npm test -- --watchAll=false'  // Run tests in CI mode
            }
        }

        stage('Build') {
            steps {
                echo 'Building application...'
                bat 'npm run build'  // Use 'bat' for Windows
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Create deployment directory if it doesn't exist
                bat 'mkdir "%DEPLOY_DIR%"'  // Use 'mkdir' for Windows
                bat 'rmdir /S /Q "%DEPLOY_DIR%"'  // Remove old deployment files
                
                // Copy new build files
                bat 'xcopy /E /I /H /Y build\\* "%DEPLOY_DIR%\\\\"'
                
                // Set proper permissions (if applicable)
                bat 'icacls "%DEPLOY_DIR%" /grant Jenkins:F /T'  // Adjust permissions if needed
            }
        }

        stage('Post-Deployment Test') {
            steps {
                echo 'Testing deployed application...'
                // Wait for application to be ready
                bat 'timeout /t 10'  // Wait for 10 seconds
                
                // Test if the application is accessible
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
            // Clean workspace after pipeline completion
            cleanWs()
        }
    }
}
