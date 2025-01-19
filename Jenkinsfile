pipeline {
    agent any

    environment {
        NODE_VERSION = '18.x'
        DEPLOY_DIR = 'D:\\react'
        GITHUB_REPO = 'https://github.com/rahavcs/Assignments.git'
    }

    tools {
        nodejs 'Node-18'
    }

    stages {
        stage('Checkout') {
            steps {
                cleanWs()
                echo 'Cloning repository...'
                git branch: 'main', url: "${GITHUB_REPO}"
            }
        }

        // Commented out as no package.json exists
        // stage('Install Dependencies') {
        //     steps {
        //         echo 'Installing dependencies...'
        //         sh 'npm install'
        //     }
        // }

        // Add custom build steps here if needed
        stage('Build') {
            steps {
                echo 'Building application...'
                // Replace with actual build commands if necessary
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'sudo mkdir -p ${DEPLOY_DIR}'
                sh 'sudo rm -rf ${DEPLOY_DIR}/*'
                sh 'sudo cp -r build/* ${DEPLOY_DIR}/'
                sh 'sudo chown -R jenkins:jenkins ${DEPLOY_DIR}'
                sh 'sudo chmod -R 755 ${DEPLOY_DIR}'
            }
        }

        stage('Post-Deployment Test') {
            steps {
                echo 'Testing deployed application...'
                sh 'sleep 10'
                script {
                    def response = sh(
                        script: 'curl -s -o /dev/null -w "%{http_code}" http://localhost',
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
            cleanWs()
        }
    }
}

    }
}
