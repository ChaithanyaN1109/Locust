pipeline
{
    agent any
    
    stages {
        stage('pre-installation')
        {   steps
         {
            pip3 install locust
        }
        }
        stage('checkout')
        {
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/ChaithanyaN1109/Locust.git']]])
            }
        }
        stage('build')
        {
            steps{
                git 'https://github.com/ChaithanyaN1109/Locust.git' 
                bat 'locust -u 1 -r 1 -t 50s --headless --print-stats --csv run.csv --csv-full-history --host=https://jsonplaceholder.typicode.com'
            }
        }     
        
    }
}
