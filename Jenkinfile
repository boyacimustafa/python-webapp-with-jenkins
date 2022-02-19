pipeline {
    agent any

    environment{
        DOCKERHUB_CREDENTIALS = credentials('jenkins-dockerhub')
    }

    stages {
        stage('Docker Image Build'){
            steps{
                sh 'docker build -t mustafaboyar/python-webapp:latest .'                
            }
            
        }
    }
}
