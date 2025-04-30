pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'your-username/healthcare-management'  // Docker Image name
        DOCKER_REGISTRY = 'docker.io'  // or your custom Docker registry
        DOCKER_TAG = "latest"
        REPO_URL = 'https://github.com/vedantgurav9/Healthcare-management.git'
        REGISTRY_CREDENTIALS = 'docker-credentials-id'  // Jenkins credentials ID for Docker registry login
    }

    stages {
        stage('Checkout Code') {
            steps {
                // Clone the Git repository
                git url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Setup Python environment and install dependencies
                    sh 'python3 -m venv venv'
                    sh './venv/bin/pip install --upgrade pip'
                    sh './venv/bin/pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Run tests (pytest or unittest)
                    sh './venv/bin/pytest tests/'  // Adjust the test directory as per your setup
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh "docker build -t ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG} ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Log into Docker registry
                    withCredentials([usernamePassword(credentialsId: "${REGISTRY_CREDENTIALS}", usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                    }
                    
                    // Push the Docker image to DockerHub (or other registry)
                    sh "docker push ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}"
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                script {
                    // SSH into your server or use any deployment mechanism
                    // For example, deploying to a remote server:
                    sh """
                        ssh user@your-server-ip 'docker pull ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}'
                        ssh user@your-server-ip 'docker run -d --restart always --name healthcare-management ${DOCKER_REGISTRY}/${DOCKER_IMAGE}:${DOCKER_TAG}'
                    """
                }
            }
        }
    }

    post {
        always {
            // Clean up actions (e.g., remove containers or images)
            cleanWs()
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed!'
        }
    }
}
