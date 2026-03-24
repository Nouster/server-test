pipeline {
    agent {
        docker { 
            image 'python:3.10'
            args '-u root' 
        }
    }

    environment {
        DOCKER_IMAGE = "product-app:latest"
        SONAR_SCANNER_HOME = tool 'SonarScanner' // Nom à vérifier dans Administrer Jenkins > Global Tool Configuration
    }

    stages {
        stage('Installation') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Tests & Couverture') {
            steps {
                sh 'pip install pytest-cov'
                sh 'pytest --cov=backend --cov-report=xml:coverage.xml --cov-report=term-missing backend/tests/'
            }
        }

        stage('Analyse Complexité (Radon)') {
            steps {
                sh 'radon cc backend -a'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') { // 'SonarQube' est le nom configuré dans Jenkins
                        sh "${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=product-api \
                            -Dsonar.sources=backend \
                            -Dsonar.python.coverage.reportPaths=coverage.xml \
                            -Dsonar.host.url=${SONAR_HOST_URL}"
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
