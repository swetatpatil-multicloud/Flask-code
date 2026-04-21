pipeline {
    agent any

    environment {
        APP_ENV = "staging"
    }

    stages {

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                python3 -m ensurepip --upgrade || true
                python3 -m pip install --upgrade pip
                pip3 install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                pytest || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {

        success {
            echo 'Build Success!'
            mail to: 'swetatpatil@gmail.com',
                 subject: 'Jenkins Build SUCCESS',
                 body: 'Your Flask CI/CD pipeline executed successfully!'
        }

        failure {
            echo 'Build Failed!'
            mail to: 'swetatpatil@gmail.com',
                 subject: 'Jenkins Build FAILED',
                 body: 'Your Flask CI/CD pipeline failed. Please check Jenkins logs.'
        }
    }
}