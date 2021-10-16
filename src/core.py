# coding: utf-8

# Copyright (c) 2019-2020 Latona. All rights reserved.

# from aion.microservice import main_decorator, Options
# from aion.kanban import Kanban
from DockerController import controller

import os 
from aion.logger_library.LoggerClient import LoggerClient
from DockerController import controller
from StatusJsonPythonModule import RequestSession, StatusJsonRest


def main():
    statusObj = StatusJsonRest.StatusJsonRest(os.getcwd(), __file__)
    statusObj.initializeStatusJson()
    image = statusObj.getMetadataFromJson("container_image")
    docker_registry_url = statusObj.getMetadataFromJson("docker_registry_url")
#    docker_registry_url = "localhost:31112"
#    image = ["select-picture-by-time:latest"]
    dc = controller.DockerController()
    for i in image:
        n = i.split(':')
        new_image = dc.rename_image(
                n[0],
                docker_registry_url,
                n[1]
            )
        res = dc.push(
                new_image
            )
        if res == None:
            log.print("Failed to push image: {}".format(i))

if __name__ == "__main__":
    main()
