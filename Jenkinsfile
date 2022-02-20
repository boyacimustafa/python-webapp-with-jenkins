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
                sh 'docker login -u $DOCKERHUB_CREDENTIALS_USR -p $DOCKERHUB_CREDENTIALS_PSW'                
            }
        }
        
        stage('Docker Image Upload'){
            steps{
                sh 'docker push mustafaboyar/python-webapp:latest'                
            }    
        }

        stage('Stop Remove if previous container running'){
            steps{
                sh 'docker ps -f name=mypythonContainer -q | xargs --no-run-if-empty docker container stop'
                sh 'docker container ls -a -fname=mypythonContainer -q | xargs -r docker container rm'                
            }    
        }

        stage('Run Docker Container'){
            steps{
                sh 'docker run -d -p 5000:5000 --rm --name mypythonContainer mustafaboyar/python-webapp'                
            }    
        }
        
    }
    post{
        always{
            sh 'docker logout'
        }
    }
}