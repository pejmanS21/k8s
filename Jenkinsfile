pipeline {
    agent any
    environment {
        VERSION = '0.1.0'
    }
    stages {
        stage("build") {
            agent { docker { image 'python:3.9-slim' } }
            steps {
                sh 'python3 -V'
                sh 'python3 test_jenkins.py'
            }
        }
        
        stage("test") {
            when {
                expression {
                    BRANCH_NAME == "dev"
                }
            }
            steps {
                echo 'Test Stage'
            }
        }

        stage("deploy") {
            steps {
                echo 'Deploy Stage'
                echo "deploying app:${VERSION}"
            }
        }
    }
    post {
        always {
            // do no matter what
            echo "always job"
        }
        success {
            // if job successful
            echo "success job"
        }
        failure {
            // if job failed
            echo "failure job"
        }
    }
}
