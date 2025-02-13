pipeline {
    agent any

    environment {
        // SonarQube token from Jenkins credentials.
        SONARQUBE_TOKEN = credentials('sonarqube_scan')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/MrGolbez/devsecops_project.git'
            }
        }

        stage('Build') {
            steps {
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
                // Run tests using pytest and generate a coverage report.
                sh '''
                    cd ${WORKSPACE}
                    export PYTHONPATH=${WORKSPACE}
                   pytest tests/test_math_utils.py --maxfail=1 --disable-warnings -q --cov=src --cov-report=xml
                   '''
            }
            post {
                success { echo 'Tests passed and coverage report generated.' }
                failure { echo 'Tests failed.' }
            }
        }

        stage('SonarQube Analysis') {
            steps {
                // Use withSonarQubeEnv to set environment variables for SonarQube.
                withSonarQubeEnv('My_SonarQube_Server') {
                    sh '''
                        sonar-scanner \
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
                // Build a Python package; ensure a valid setup.py exists.
                sh 'python3 setup.py sdist bdist_wheel'
                // Archive the artifacts from the dist folder.
                archiveArtifacts artifacts: 'dist/*', fingerprint: true
            }
            post {
                success { echo 'Artifact generation succeeded.' }
                failure { echo 'Artifact generation failed.' }
            }
        }

        stage('Send Slack Notification') {
            steps {
                // Send Slack notification using the Slack plugin.
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
