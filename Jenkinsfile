pipeline {
    agent none // On définit l'agent par étape

    environment {
        DOCKER_IMAGE = "product-app:latest"
    }

    stages {
        stage('Installation & Tests') {
            agent {
                docker { 
                    image 'python:3.10'
                    args '-u root' 
                }
            }
            steps {
                sh 'pip install -r requirements.txt'
                sh 'pip install pytest-cov'
                // On génère coverage.xml pour SonarQube
                sh 'pytest --cov=backend --cov-report=xml:coverage.xml --cov-report=term-missing backend/tests/'
                sh 'radon cc backend -a'
            }
        }

        stage('SonarQube Analysis') {
            agent any // On repasse sur l'agent Jenkins (qui a Java)
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=product-api \
                            -Dsonar.sources=backend \
                            -Dsonar.python.coverage.reportPaths=coverage.xml"
                    }
                }
            }
        }

        stage('Docker Build') {
            agent any
            steps {
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
    }

    post {
        success {
            echo "Pipeline terminé avec succès ! ✅"
        }
        failure {
            echo "Le pipeline a échoué. ❌"
        }
    }
}
