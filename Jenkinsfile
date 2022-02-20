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
            
        stage('Docker Login'){
            steps{
                sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR $DOCKERHUB_CREDENTIALS_PSW'                
            }
        }
        
        stage('Docker Image Upload'){
            steps{
                sh 'docker push mustafaboyar/python-webapp:latest'                
            }    
        }
    }
    post{
        always{
            sh 'docker logout'
        }
    }
}