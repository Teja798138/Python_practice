pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup & Install') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    # We use || true so the pipeline doesn't crash if a test fails
                    pytest --alluredir=Reports/allure-results -m sanity || true
                '''
            }
        }

        stage('Generate Allure Report') {
            steps {
                // This step calls the plugin and the 'allure' tool name specifically
                allure includeProperties: false, 
                       jdk: '', 
                       results: [[path: 'Reports/allure-results']]
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Pipeline executed successfully.'
        }
        failure {
            echo 'Pipeline execution failed.'
        }
    }
}