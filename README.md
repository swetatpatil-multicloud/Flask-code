# Flask Web Application: Jenkins CI/CD Pipeline
This repository contains a simple Flask web application integrated with a Jenkins CI/CD Pipeline. The goal of this project is to automate the lifecycle of the application—from dependency installation and unit testing to final deployment.

## Project Overview
The pipeline is defined in a Jenkinsfile (Declarative Pipeline) and performs the following:

Build: Sets up a virtual environment and installs dependencies.

Test: Executes unit tests using pytest to ensure code quality.

Deploy: Automatically deploys the application to a staging environment upon successful testing.

## Prerequisites
Before running the pipeline, ensure the following are configured on your Jenkins server:

Jenkins Installed: Jenkins should be running on a Linux/Windows VM or Cloud instance.

Python & Pip: Python 3.x must be installed on the Jenkins agent.

Plugins: Install the following Jenkins plugins:

Git Plugin

Pipeline

Email Extension Plugin (for notifications)

Credentials: Configure GitHub credentials in Jenkins to allow repository cloning.

## Repository Structure
app.py: The core Flask application.

test_app.py: Unit tests for the application.

requirements.txt: List of Python dependencies.

Jenkinsfile: The automation script for CI/CD.

README.md: Project documentation.

## CI/CD Pipeline Stages
### 1. Build Stage
The pipeline initializes a Python virtual environment and installs the required packages:

Bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

### 2. Test Stage
Automated tests are triggered using pytest. If any test fails, the pipeline stops immediately to prevent faulty code from reaching deployment.

Bash
pytest test_app.py

### 3. Deploy Stage
Once tests pass, the application is deployed. In this setup, the deployment is simulated by starting the Flask server or moving files to a staging directory.

### Notifications & Triggers
GitHub WebHook Trigger: The pipeline is configured to trigger automatically whenever a push is made to the main branch.

Email Alerts: Jenkins will send an automated email notification to the administrator:

### Success: When the build, test, and deployment are successful.

### Failure: If any stage fails, providing a link to the build logs.

## How to Use
Fork this repository to your own GitHub account. (However, instead of forking the repo, I have directly clone it)

In Jenkins, create a new Pipeline job.

Under Pipeline script from SCM, select Git and paste your forked repository URL.

Specify the branch as */main.

Click Save and Build Now.

##  Pipeline Execution (Screenshots)
#### I have used port 5001 instead of 5000 as port 5000 is occupied on another service.

### Before adding data: 
<img width="940" height="377" alt="image" src="https://github.com/user-attachments/assets/a4aca7b1-c7b4-458a-b92d-38984bfc3d7c" />

### Adding new record:
<img width="940" height="469" alt="image" src="https://github.com/user-attachments/assets/0d6cdd20-7a92-46b7-bebc-d3e5238541bc" />

### After adding a new record:
<img width="940" height="441" alt="image" src="https://github.com/user-attachments/assets/02c28cf8-d33d-4977-8ebf-16328dc39a4b" />

### The new records are updated in DB too:
<img width="940" height="464" alt="image" src="https://github.com/user-attachments/assets/f19b88a8-5922-422f-9b8a-de9e08f5513c" />

### Output of Python app.py file from VS code:
<img width="940" height="676" alt="image" src="https://github.com/user-attachments/assets/4140aeb4-aa19-461a-9ba8-1f54af372226" />

### Screenshot of EC2 Python app.py:
<img width="940" height="468" alt="image" src="https://github.com/user-attachments/assets/c40509d9-1467-42ae-9106-2ca98a6438c1" />

### EC2 instance screenshot:
<img width="940" height="416" alt="image" src="https://github.com/user-attachments/assets/593e725f-032d-4d58-beaa-5eead08ae48e" />
<img width="940" height="412" alt="image" src="https://github.com/user-attachments/assets/d8cf3fda-cdfa-4a61-a778-01881872076b" />

------------------------------------------------------------------------------------------------------------------------------------------------------------------

## MONGO_URI=mongodb+srv://flaskuser:*******@swetapatil.nlqpeax.mongodb.net/mydb
## SECRET_KEY=*******

------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Pipeline Stage View:

<img width="940" height="318" alt="image" src="https://github.com/user-attachments/assets/2c8e3a9f-a83c-4552-bcea-39fa75511b6f" />

<img width="940" height="399" alt="image" src="https://github.com/user-attachments/assets/2b75fbac-ee1b-47a4-ab71-5dfd3df5c0f7" />

<img width="940" height="322" alt="image" src="https://github.com/user-attachments/assets/f7389b40-1435-4cb6-ab80-67d71d66360f" />

<img width="619" height="849" alt="image" src="https://github.com/user-attachments/assets/c57419c2-3b11-419a-9246-7e23092b65bc" />

<img width="672" height="558" alt="image" src="https://github.com/user-attachments/assets/b1bcd5ac-c7df-48d6-879e-5880bd0ee00a" />

### First production release
<img width="940" height="411" alt="image" src="https://github.com/user-attachments/assets/4b0d2b8d-6afa-4cb2-aa46-f74893236e7c" />

<img width="940" height="412" alt="image" src="https://github.com/user-attachments/assets/dacd92cf-6757-453f-80a0-cc03a1e87c0d" />

<img width="940" height="394" alt="image" src="https://github.com/user-attachments/assets/8b63b366-ac36-428a-a7fa-5a7d32c8742f" />

