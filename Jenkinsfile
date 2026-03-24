pipeline {
    agent any // On reste sur l'agent principal pour simplifier le partage de fichiers

    environment {
        DOCKER_IMAGE = "product-app:latest"
    }

    stages {
        stage('Installation & Tests') {
            steps {
                script {
                    // On lance les tests dans un conteneur python éphémère
                    docker.image('python:3.10').inside('-u root') {
                        sh 'pip install -r requirements.txt'
                        sh 'pip install pytest-cov'
                        sh 'pytest --cov=backend --cov-report=xml:coverage.xml --cov-report=term-missing backend/tests/'
                        sh 'radon cc backend -a'
                    }
                }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'
                    withSonarQubeEnv('SonarQube') {
                        // On laisse le scanner lire sonar-project.properties
                        sh "${scannerHome}/bin/sonar-scanner"
                    }
                }
            }
        }

        stage('Docker Build') {
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
