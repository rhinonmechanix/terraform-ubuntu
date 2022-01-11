1. we need to install eb cli
-> pip install --upgrade --user awsebcli

2. Or by cloning the git repo
-> git clone https://github.com/aws/aws-elastic-beanstalk-cli-setup
-> run bundled_installer inside the directory

3. Check version
-> eb --version

-----------------------------------------------------------------------------------------

1. make a particular directory for EB environment
-> mkdir Getting-started

2. Starting the EB environmnet
-> eb init
-> select region --
-> application name --
-> select Platform
-> type yes/no according to, if we need setup ssh for the instance
-> select Keypair.

3. Creating the EB application
-> eb create
-> enter environment name
-> enter DNS CNAME prefix - which sgould be unique
-> select load balancer - default is 2:
-> after installation
   -> check the application using -> eb list

4. Updating the configuration
-> eb config

5. delete the application
-> eb terminate

------------------------------------------------------

Updating the EB environment

-> aws elasticbeanstalk update-environment --environment-name my-env --version-label v2

This changes the environment "my-env" to version "v2".

--------------------------------------------------------------------------------------------------------


EB UI Deployment

1. Open Elastic beanstalk console

2. Open create new application
 a. Give application name.
 b. Give application tags -> key-value pair if have any!
 c. Choose platform and its version
 d. choose application code as sample application

3. Click create environment.

4. It will take some time to process, which will create Environment (Creating aplication_name-env)

5. After the environment was created, we will see options, if we come below, which show-
  i)   Health - to check status or performance
  ii)  Running Version - to Upload and deploy the application
  iii) platform - Platform details

6. Click Upload and deploy from Running version

from here we can deploy our application.