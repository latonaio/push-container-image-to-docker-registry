import docker
import os
import pathlib
import pycurl
import subprocess

class DockerController:
    def __init__(self):
        self.client= docker.from_env()

    def build(self, path, tag, arg=None, rm=True):
        build_script = "{}/docker-build.sh".format(path)
        if os.path.exists(build_script):
            os.chdir(path)
            subprocess.call(
                "./docker-build.sh",
                shell=True
            )
        else:
            try:
                build_result = self.client.images.build(
                    path=path, 
                    tag=tag, 
                    arg=arg, 
                    rm=rm,
                )
                return build_result
            except docker.errors.BuildError as e:
                print(e)
                print("Failed to build image")
                return False
        
    def check_exist_image(self, image_name):
        try:
            return self.client.images.get(image_name)
        except docker.errors.ImageNotFound as e:
            print(e)
            print("Failed to get image")
            return None

    def remove_image(self, image):
        tag = image.tags[0]
        self.client.images.remove(tag)

    def push(self, image, tag=None):
        try:
            return self.client.images.push(image, tag)
        except Exception as e:
            print(e)
            print("Failed to push image")
            return None

    def rename_image(
            self, 
            repository: str, 
            dest: str, 
            tag: str = None) -> str:
        old_image = "{}:{}".format(repository, tag)
        new_image = "{}/{}:{}".format(dest, repository, tag)
        try:
            subprocess.call(
                ["docker", "tag", old_image, new_image]
            )
        except Execption as e:
            print(e)
        return new_image
