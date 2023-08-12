# LabDockerfiles
Dockerfiles for Lab usage.

## How to use?
Fork and clone the repository.

Copy the template `./Dockerfile` to `./IMAGE_NAME/TAG/Dockerfile` (e.g. `./anaconda3/2023.07-1/Dockerfile`) and modify the Dockerfile, add desired configurations.

After the modification of Dockerfile is completed, create merge request to `kuromesi/LabDockerfiles:dev`, if merged, the image would be built and pushed to `kuromesi/IMAGE_NAME:TAG`