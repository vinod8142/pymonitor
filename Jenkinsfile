pipeline{

agent any

stages{

stage("build"){
  when {
                changelog ".*test.*"
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
