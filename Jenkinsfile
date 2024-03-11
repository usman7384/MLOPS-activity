pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                script {
                    git 'https://github.com/usman7384/MLOPS-activity.git'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Execute test.py') {
            steps {
                script {
                    sh 'python test.py'
                }
            }
        }

       stage('Deploying') {
    steps {
        script {
            def branchName = sh(script: 'git rev-parse --abbrev-ref HEAD', returnStdout: true).trim()
            
            if (branchName == 'main') {
                echo 'Deploying to production'
                // Deployment commands for production environment
                sh '''
                    echo "Deployment to production started"
                    git pull origin main  # Ensure the latest changes from main branch are pulled
                    # Add any necessary deployment commands here
                    git add .
                    git commit -m "Deployment to production"
                    git push origin main  # Push changes to the main branch
                '''
            } else {
                echo 'Deploying to UAT'
                // Deployment commands for UAT environment
                sh '''
                    echo "Deployment to UAT started"
                    # Add your deployment commands here
                '''
            }
        }
    }
}

    }
}
