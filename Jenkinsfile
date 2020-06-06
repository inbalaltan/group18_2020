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
					sh 'echo y | python3 manage.py makemigrations --merge'
					sh 'python3 manage.py makemigrations --merge'
					sh 'python3 manage.py migrate'
					sh 'python3 manage.py test --cover-tests'
					sh 'python3 -m pyflakes home/'
					sh 'python3 -m pyflakes mifga/'
					sh 'python3 -m pyflakes Users/'
		    }
			}
        }
    }
}
