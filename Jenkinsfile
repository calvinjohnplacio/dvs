pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/calvinjohnplacio/dvs.git'
        GIT_CREDENTIALS_ID = 'github-pat'
        GIT_BRANCH = 'main'
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: "${env.GIT_BRANCH}",
                    url: "${env.GIT_REPO_URL}",
                    credentialsId: "${env.GIT_CREDENTIALS_ID}"
            }
        }

        stage('Setup Python') {
            steps {
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install selenium
                '''
            }
        }

        stage('Run Test') {
            steps {
                sh '''
                . venv/bin/activate
                python test.py
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                sudo rsync -av --delete ./ /var/www/html/
                sudo chown -R www-data:www-data /var/www/html/
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD SUCCESS ✔"
        }
        failure {
            echo "CI/CD FAILED ❌"
        }
    }
}
