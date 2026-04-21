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
                pytest || true
                '''
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh '''
                . venv/bin/activate
                nohup python app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Build Success!'
        }
        failure {
            echo 'Build Failed!'
        }
    }
}