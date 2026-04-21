pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '''
                    . venv/bin/activate
                    pytest
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                    pkill -f app.py || true
                    . venv/bin/activate
                    nohup python app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Build Success!'
            mail to: 'you@gmail.com',
                 subject: "Build Success",
                 body: "Build passed successfully."
        }

        failure {
            echo 'Build Failed!'
            mail to: 'you@gmail.com',
                 subject: "Build Failed",
                 body: "Check Jenkins logs for details."
        }
    }
}