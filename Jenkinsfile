pipeline {
    agent any

    environment {
        IMAGE_NAME = 'health-monitor'
    }

    stages {
        stage('Checkout Code') {
            steps {
                git 'https://github.com/vedantgurav9/Healthcare-management.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Installing Python dependencies...'
                bat '''
                    python -m venv venv
                    call venv\\Scripts\\activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo 'Running tests...'
                bat '''
                    call venv\\Scripts\\activate
                    python -m unittest discover
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-credentials', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    echo 'Pushing Docker image to Docker Hub...'
                    bat '''
                        docker login -u %DOCKER_USER% -p %DOCKER_PASS%
                        docker tag %IMAGE_NAME% %DOCKER_USER%/%IMAGE_NAME%
                        docker push %DOCKER_USER%/%IMAGE_NAME%
                    '''
                }
            }
        }

        stage('Deploy Docker Container') {
            steps {
                echo 'Deploying Docker container...'
                bat '''
                    docker rm -f health-monitor-container || echo Container does not exist
                    docker run -d --name health-monitor-container -p 5000:5000 %IMAGE_NAME%
                '''
            }
        }
    }

    post {
        always {
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
