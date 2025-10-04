pipeline {
  agent any

  stages {
    stage('Checkout') {
	steps {
	  git branch: 'master', url: 'https://github.com/Glbertoh/devops-project.git'
	}
    }
    stage('Test') {
	steps {
	  sh 'pytest || echo "No tests yet"'
	}
    }
    stage('Build') {
	steps {
	  sh 'docker build -t localhost:5000/devops-project:latest .'
	}
    }
    stage('Push to local registry') {
	sh -docker push localhost:5000/devops-project:latest
    }
    stage('Deploy') {
	steps {
	  sh 'ansible-playbook -i ansible/inventory.ini ansible/playbook.yml'
	}
    }
  }
}		
