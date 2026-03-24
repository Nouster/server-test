pipeline {
    agent {
        docker { 
            image 'python:3.10'
            args '-u root' 
        }
    }

    environment {
        DOCKER_IMAGE = "product-app:latest"
    }

    stages {
        stage('Installation') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Tests & Couverture') {
            steps {
                sh 'pytest --cov=backend --cov-report=xml --cov-report=term-missing backend/tests/'
            }
        }

        stage('Analyse Complexité (Radon)') {
            steps {
                sh 'radon cc backend -a'
            }
        }

        stage('Docker Build') {
            agent any // On repasse sur l'agent principal pour construire l'image finale
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
