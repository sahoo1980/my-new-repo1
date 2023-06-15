import os
import subprocess

def download_code (github_repo,destination):
    subprocess.run(['git', 'clone', github_repo,destination])
def build_docker_image (image_name,dockerfile_path):
    subprocess.run(['docker', 'build', '-t', image_name, '-f', dockerfile_path, '.'])
def push_to_gcr(image_name,gcr_path):
    subprocess.run(['docker', 'tag', image_name, gcr_path])
    subprocess.run(['docker', 'push', gcr_path])

#Define above parameters
github_repo = 'https://github.com/sahoo1980/my-new-repo1.git'
destination_folder = 'repo'
docker_image_name = 'my-image:1.0'
dockerfile_path = 'D:\\Papa\MyPrograms\\My-Terraform\\Usecase5-github-build-gcr-deployment\\dockerfile'
gcr_image_tag = '1.0'
gcr_path = 'gcr.io/learned-vault-387908/my-image/python:1.0'

#Download code from github
download_code (github_repo,destination_folder)

#Build the docker image
build_docker_image (docker_image_name,dockerfile_path)

#Authenication to GCP
subprocess.run(['gcloud', 'auth', 'configure-docker'])

#Push the image to GCR
push_to_gcr(docker_image_name,gcr_path)
