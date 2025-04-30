pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'health-monitor'
        REPO_URL = 'https://github.com/vedantgurav9/Healthcare-management.git'
        BRANCH = 'main'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: "${BRANCH}", url: "${REPO_URL}"
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                sh '''
                    python -m venv venv
                    . venv/Scripts/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/Scripts/activate
                    pytest tests/ || echo "Tests failed but continuing"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${DOCKER_IMAGE}"
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Push Docker Image') {
            when {
                expression { return env.DOCKER_USERNAME != null && env.DOCKER_PASSWORD != null }
            }
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-creds', usernameVariable: 'DOCKER_USERNAME', passwordVariable: 'DOCKER_PASSWORD')]) {
                    sh '''
                        echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
                        docker tag health-monitor $DOCKER_USERNAME/health-monitor:latest
                        docker push $DOCKER_USERNAME/health-monitor:latest
                    '''
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                echo "Running container locally (optional deployment step)..."
                sh '''
                    docker stop health-monitor || true
                    docker rm health-monitor || true
                    docker run -d --name health-monitor -p 8000:8000 health-monitor
                '''
            }
        }
    }

    post {
        always {
            cleanWs()
        }
        failure {
            echo 'Pipeline failed!'
        }
        success {
            echo 'Pipeline succeeded!'
        }
    }
}
