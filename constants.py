import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as numpy
import random as random
import constants as c
import solution as solution

timevalue = 100000
sleepTime = 1/6000

amplitude_Front = numpy.pi / 4
frequency_Front = 1
phaseOffset_Front = 0

amplitude_Back = numpy.pi / 4
frequency_Back = 1
phaseOffset_Back = numpy.pi / 4

numberofGenerations = 1

populationSize = 1
iterations = 5000
maxForce = 10000
#numSensorNeurons = 8
#numMotorNeurons = 8

motorJointRange = 0.75

seed = 1