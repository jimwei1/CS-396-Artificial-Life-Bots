import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random as random
import constants as c

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        self.objects = p.loadSDF("world.sdf")
        
    # def get_link_location(self, link_id):
    #     posAndOrientation = p.getBasePositionAndOrientation(self.objects[link_id])
    #     position = posAndOrientation[0]
    #     xPosition = position[0]
    #     yPosition = position[1]
    #     height = position[2]
    #     return_tuple = (xPosition, yPosition, height)
    #     return return_tuple

