import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random as random
import constants as c

from world import WORLD
from robot import ROBOT
from sensor import SENSOR

class SIMULATION:
    def __init__(self, directOrGui, solutionID):
        if directOrGui == "DIRECT":
            self.physicsClient = p.connect(p.DIRECT)
        else:
            self.physicsClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        p.setGravity(0,0,-9.8)

        self.directOrGUI = directOrGui
        self.solutionID = solutionID
        self.world = WORLD()
        self.robot = ROBOT(self.solutionID, self.world)

    def Run(self):
        sleepTime = 0
        if self.directOrGUI == "GUI":
            sleepTime = c.sleepTime
        for i in range(c.iterations):
            time.sleep(sleepTime)
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.Act(i)
        
    def __del__(self):        
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()