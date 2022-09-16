pipeline {
    agent any
    environment {
        VERSION = '0.1.0'
        SERVER_CREDENTIALS = credentials('credential_id')   // credential binding plugin
    }
    stages {
        stage("build") {
            agent { docker 'python:3.9-slim' }
            steps {
                echo 'Build Stage'
                echo "Building ${VERSION}"
                if (env.BRANCH_NAME == 'dev') {
                    sh 'python3 -V'
                    sh 'python3 test_jenkins.py'
                }
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
                echo "Deploying into ${SERVER_CREDENTIALS}"
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
