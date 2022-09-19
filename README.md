# Deployment 1: Flask App
Spin up an EC2 instance to launch Jenkins and setup the pipeline to ensure that a multibranch pipeline (source repo found on GitHub) builds successfully. Then deploy the Flask application manually using AWS Elastic Beanstalk.

#### Detailed steps found here: [Deployment1_AssignmentInstruction.pdf](https://github.com/cadenhong/kl_wk9_deployment1/files/9601373/Deployment1_AssignmentInstruction.pdf)

## Setup
1. Install Jenkins on an EC2
2. Install Virtual Environment
3. Connect GitHub to Jenkins Server

## Tasks
- Create a multibranch build on Jenkins
- Scan repository to trigger a build on Jenkins
- Compress the application files found on GitHub repo then deploy to AWS Elastic Beanstalk
- Document the steps taken, observations, and areas of improvement (see [Deployment1_Documentation.docx](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/Deployment1_Documentation.docx))
- Diagram the pipeline of the deployment (see [Deployment1_Diagram.png](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/Deployment1_Diagram.png))

## Files and Folders
- [static](https://github.com/cadenhong/kl_wk9_deployment1/tree/main/static): Contains CSS and JS files for the application
- [templates](https://github.com/cadenhong/kl_wk9_deployment1/tree/main/templates): Contains HTML files for the application
- [Deployment1_Diagram.png](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/Deployment1_Diagram.png): Diagram of the pipeline
- [Deployment1_Documentation.docx](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/Deployment1_Documentation.docx): Notes and observations made during deployment
- [Jenkinsfile](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/Jenkinsfile): Contains definition of Jenkins pipeline
- [Pipfile](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/Pipfile): Used by the Pipenv virtual environment to manage project dependencies
- [Pipfile.lock](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/Pipfile.lock): Based on packages present in Pipfile, determines which specific versions should be used
- [application.py](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/application.py): Flask application
- [myapp.zip](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/myapp.zip): Compressed file containing everything from the repo for the application - is used to upload to AWS to create the application using Elastic Beanstalk
- [requirements.txt](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/requirements.txt): Lists all dependencies needed for the Flask application - also used in Jenkinsfile for the Build stage
- [test_app.py](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/test_app.py): Imports the `greet` function from application.py to perform a quick test
- [urls.json](https://github.com/cadenhong/kl_wk9_deployment1/blob/main/urls.json): Used in Flask app, keeps track of urls and their short names

## Tools
- Jenkins
- GitHub
- Python
- Flask
- AWS EC2
- AWS Elastic Beanstalk
- Diagrams.net
