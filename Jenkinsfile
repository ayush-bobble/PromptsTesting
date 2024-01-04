pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                script {
                    checkout(
                        [
                            $class: 'GitSCM',
                            branches: [[name: '*/main']],
                            doGenerateSubmoduleConfigurations: false,
                            extensions: [],
                            submoduleCfg: [],
                            userRemoteConfigs: [[credentialsId: 'ee89bfbe-0c17-482f-bb0a-29a7f33ef69d', url: 'https://github.com/ayush-bobble/PromptsTesting.git']]
                        ]
                    )
                }
            }
        }

        stage('Run ads_keywords.py') {
            steps {
                script {
                    sh 'python3 ads_keyword.py'
                }
            }
        }
    }

    post {
        always {
            // Clean up or post-build actions if needed
            echo 'This block is optional and can be used for clean-up actions.'
        }
    }
}
