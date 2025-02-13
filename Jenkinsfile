pipeline {
    agent any

    environment {
        // SonarQube token from Jenkins credentials.
        SONARQUBE_TOKEN = credentials('sonar_scanner')
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Starting Checkout Stage'
                git branch: 'main', url: 'https://github.com/MrGolbez/devsecops_project.git'
            }
        }

        stage('Build') {
            steps {
                echo 'Starting Build Stage'
                // Compile all Python files to check for syntax errors.
                sh 'python3 -m compileall src/'
            }
            post {
                success { echo 'Build Success!' }
                failure { echo 'Build Failed!' }
            }
        }

        stage('Test and Code Coverage') {
            steps {
                echo 'Starting Test and Code Coverage Stage'
                sh '''
                    cd ${WORKSPACE}
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                    export PYTHONPATH=${WORKSPACE}
                    pytest tests/test_math_utils.py --max-fail=1 --disable-warnings -q --cov=src --cov-report=xml
                '''
            }
            post {
                success { echo 'Tests passed and coverage report generated.' }
                failure { echo 'Tests failed.' }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                echo 'Starting SonarQube Analysis Stage'
                withSonarQubeEnv('My SonarQube Server') {
                    sh '''
                        ${tool 'sonar_scanner'}/bin/sonar-scanner \
                            -Dsonar.projectKey=devsecops_project \
                            -Dsonar.sources=. \
                            -Dsonar.language=py \
                            -Dsonar.python.coverage.reportPaths=coverage.xml \
                            -Dsonar.login=${SONARQUBE_TOKEN}
                    '''
                }
            }
            post {
                success { echo 'SonarQube analysis completed successfully.' }
                failure { echo 'SonarQube analysis failed.' }
            }
        }

        stage('Artifact Generation') {
            steps {
                echo 'Starting Artifact Generation Stage'
                sh 'python3 setup.py sdist bdist_wheel'
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
            }
            post {
                success { echo 'Artifact generation succeeded.' }
                failure { echo 'Artifact generation failed.' }
            }
        }

        stage('Send Slack Notification') {
            steps {
                echo 'Starting Slack Notification Stage'
                slackSend channel: '#pipeline_updates',
                          message: "Build ${currentBuild.currentResult}: ${env.JOB_NAME} #${env.BUILD_NUMBER}",
                          tokenCredentialId: 'slack_token'
            }
        }
    }

    post {
        always {
            echo 'Pipeline completed.'
        }
    }
}
