pipeline{
agent any
  
    environment {
        ENV = "testin"
    }

stages{

stage("build"){
  when {
                environment(name: "ENV", value: "testing")
            }
steps{
echo "something build"
}
}
stage("test"){
steps{
echo "something test"
}
}
stage("deploy"){
steps{
echo "something deploy"
}
}
}
}
