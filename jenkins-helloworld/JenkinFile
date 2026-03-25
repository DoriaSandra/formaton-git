node {
    stage('clone') {
        sh "rm -rf jenkins-helloworld papa papa1 papa2 test-formation-git-fork-flow wookie.py"
        git 'https://github.com/DoriaSandra/formaton-git.git'
    }

    stage('Build') {
        sh '''
            cd jenkins-helloworld
            javac Main.java
        '''
    }

    stage('Run') {
        sh '''
            cd jenkins-helloworld
            java Main
        '''
    }
}
