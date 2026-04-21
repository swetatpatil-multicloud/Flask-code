pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh 'python3 -m pip install --upgrade pip'
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'pytest'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                
                // Kill any existing running app (avoid port conflict)
                sh 'pkill -f app.py || true'
                
                // Run Flask app in background
                sh 'nohup python3 app.py > output.log 2>&1 &'
            }
        }
    }

    post {
        success {
            mail to: 'swetatpatil@gmail.com',
                 subject: 'Jenkins Build SUCCESS',
                 body: 'Your Flask CI/CD pipeline executed successfully!'
        }
        failure {
            mail to: 'swetatpatil@gmail.com',
                 subject: 'Jenkins Build FAILED',
                 body: 'Your Flask CI/CD pipeline failed. Please check Jenkins console output.'
        }
    }
}