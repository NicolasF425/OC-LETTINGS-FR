Worflow github
==============


File : .github/workflows/django.yml

Need folowingsecrets in github (Setting -> Secrets and variables -> Actions then Environment secrets):
- DOCKER_PASSWORD
- DOCKER_USERNAME
- RENDER_API_KEY
- RENDER_SERVICE_ID
- SECRET_KEY


job 1 : build
-------------

Build an environnement
Test the code


job 2 : Docker
--------------

Create Docker image and push on dockerhub


job 3 : deployment on Render
----------------------------

Deploy the docker image on render.
The image can be run on Render

