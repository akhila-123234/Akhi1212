pipeline {
    agent any
    options {
        // Timeout counter starts AFTER agent is allocated
        timeout(time: 1, unit: 'SECONDS')
    }
    stages {
        stage('build') {
            steps {
                echo 'the application is building'
            }
        }
 stage('test') {
            steps {
                echo 'the application is testing'
            }
        }
 stage('deploye') {
            steps {
                echo 'the application is deploye'
            }
        }
}
}
