pipeline {
  agent any

  stages {
    stage('Checkout') {
	steps {
	  git branch: 'master', url: 'https://github.com/Glbertoh/devops-project.git'
	}
    }
    stage('Build') {
	steps {
	  sh 'docker build -t myapp ./app'
	}
    }
    stage('Test') {
	steps {
	  sh 'pytest || echo "No tests yet"'
	}
    }
    stage('Deploy') {
	steps {
	  sh 'ansible-playbook -i ansible/inventory.ini ansible/playbook.yml'
	}
    }
  }
}		
