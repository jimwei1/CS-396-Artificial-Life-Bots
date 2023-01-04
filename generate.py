import pyrosim.pyrosim as pyrosim



#length, width, height
x = 1
y = 1
z = 1

#pyrosim.Send_Cube(name="Box2", pos=[x +0.5 ,y,z+1] , size=[1,1,1])


"""
for i in range(5):
    for o in range (5):
        for p in range (5):
            pyrosim.Send_Cube(name="25Box", pos=[x + i*2,y + o*2,z + p*2] , size=[1,1,1])
"""

#E. Joints


def Create_World():
    pyrosim.Start_SDF("world.sdf")
    pyrosim.Send_Cube(name="Box", pos=[x+2,y+2,z] , size=[1,1,1])
    pyrosim.End()



def Create_Robot():
    pyrosim.Start_URDF("body.urdf")
    pyrosim.Send_Cube(name="Link0", pos=[0,0,0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link1", pos=[0,0,0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [0,0,1])
    pyrosim.Send_Cube(name="Link2", pos=[0,0,0.5] , size=[1,1,1])
    pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [0,0.5,0.5])
    pyrosim.Send_Cube(name="Link3", pos=[0,0.5,0] , size=[1,1,1])



    pyrosim.End()

Create_World()
Create_Robot()