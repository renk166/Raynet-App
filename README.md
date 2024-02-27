This repo contains files needed to create an API using Python and Flask, in order to count webpage hits. The application is bundled into docker file. The backend database is Redis.


Details
The app is written in Python, using Flask framework

app.py is the actual app code
requirements.txt are the dependencies required to run the app
Dockerfile is used to build docker container

Building/testing steps
Download/pull this repository: git clone https://github.com/renk166/Raynet-App.git

Go to the newly created directory cd Raynet-app

Install docker 
apt install docker.io

Install python and flask
apt install python3-pip
pip install Flask

Install Dependencies to Enable apt Over HTTPS
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

Add Docker's Official GPG Key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Add Docker Repository
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

Update package lists
sudo apt update

Install docker 
sudo apt install -y docker-ce

Verify Docker Installation
sudo docker --version

Start and Enable Docker Service
sudo systemctl start docker
sudo systemctl enable docker

Build docker ???


