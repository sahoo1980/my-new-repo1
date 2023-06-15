import subprocess

#Execute the deploy.py script to build the docker image, tag and push to the GCR.
subprocess.run(['python', 'deploy.py'])

#Execute the below terraform commands to build the deployment
#subprocess.run(['terraform', 'fmt'])
#subprocess.run(['terraform', 'init'])
#subprocess.run(['terraform', 'plan'])
#subprocess.run(['terraform', 'apply'])


