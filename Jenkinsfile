pipeline {
    agent any

    environment {
        GIT_REPO_URL = 'https://github.com/calvinjohnplacio/dvs.git'  // Your repo URL
        GIT_CREDENTIALS_ID = 'github-pat'  // Replace with your actual credentials ID in Jenkins
        GIT_BRANCH = 'main'  // The branch you want to checkout
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm: [
                    $class: 'GitSCM',
                    branches: [[name: "*/${env.GIT_BRANCH}"]],
                    userRemoteConfigs: [[
                        url: "${env.GIT_REPO_URL}",
                        credentialsId: "${env.GIT_CREDENTIALS_ID}"
                    ]]
                ]
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                echo "Setting up Python environment..."

                # Create virtual environment
                python3 -m venv venv

                # Activate virtual environment and install dependencies
                . venv/bin/activate
                pip install --upgrade pip
                pip install -r requirements.txt  # Install dependencies, including selenium and webdriver-manager
                '''
            }
        }

        stage('Run Selenium Test') {
            steps {
                sh '''
                echo "Running Selenium tests..."

                # Activate virtual environment before running the test
                . venv/bin/activate
                python test.py  # Run your test script
                '''
            }
        }

        stage('Deploy to Apache') {
            steps {
                sh '''
                echo "Deploying FULL PHP project to Apache..."

                # Sync all files (NEW + UPDATED + DELETED)
                sudo rsync -av -o --delete ./ /var/www/html/

                # Fix ownership
                sudo chown -R www-data:www-data /var/www/html/
                '''
            }
        }
    }

    post {
        success {
            echo "CI/CD SUCCESS ✔ Deployment completed"
        }
        failure {
            echo "CI/CD FAILED ❌ Check logs"
        }
        always {
            cleanWs()
        }
    }
}
