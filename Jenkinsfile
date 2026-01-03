pipeline {
    agent any

    environment {
        // This ensures the Allure tool you configured in 'Global Tool Configuration' is available
        ALLURE_HOME = tool name: 'allure', type: 'ru.yandex.qatools.allure.jenkins.AllureInstallation'
        PATH = "${env.ALLURE_HOME}/bin:${env.PATH}"
    }

    stages {
        stage('Checkout') {
            steps {
                // SCM checkout is automatic in "Pipeline from SCM" mode
                checkout scm
            }
        }

        stage('Setup Environment & Install Dependencies') {
            steps {
                sh '''
                    # Check if python exists in the container
                    python3 --version
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
                    # We add '|| true' so the pipeline doesn't stop if tests fail, 
                    # allowing the Allure report to still be generated.
                    pytest -alluredir=Reports/allure-results -m sanity || true
                '''
            }
        }

       stage('Generate Allure Report') {
            steps {
                // This step triggers the plugin directly
                // It will automatically use the tool named 'allure' if configured
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