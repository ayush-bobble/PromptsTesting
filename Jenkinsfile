pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your repository
                git 'https://github.com/ayush-bobble/PromptsTesting.git'
            }
        }

        stage('Run ads_keywords.py') {
            steps {
                script {
                    sh 'python3 ads_keywords.py'
                }
            }
        }
    }

    post {
        always {
            // Clean up or post-build actions if needed
        }
    }
}
