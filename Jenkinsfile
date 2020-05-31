pipeline {
    agent { docker { image 'python:3-alpine' } }
	triggers {
        githubPush()
    }
    stages {
        stage('install deps') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
		    			sh 'pip3 install -r requirements.txt --user'
                }
            }
        }
        stage('Test') {
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
					sh 'python3 manage.py test -v 3'
		    }
			}
        }
    }
}
