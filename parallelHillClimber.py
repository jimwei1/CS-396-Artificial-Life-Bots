from solution import SOLUTION
import constants as c
import copy as copy

class PARALLEL_HILL_CLIMBER:

    def __init__(self) -> None: #constructor

        self.nextAvailableID = 0

        self.parent = SOLUTION(self.nextAvailableID)
        self.parents = {}

        for parent in range(c.populationSize):
            
            self.parents[parent] = SOLUTION(self.nextAvailableID)
            self.nextAvailableID += 1
        
        
    def Evolve(self):

        for i in self.parents:
            self.parents[i].Start_Simulation("DIRECT")
            #self.parent.Evaluate("GUI")

        for currentGeneration in range(0, c.numberofGenerations):
                self.Evolve_For_One_Generation()

        for i in self.parents:
            self.parents[i].Wait_For_Simulation_To_End()
            print("YYYYYYY")
            print(self.parents[i].fitness)


        if currentGeneration == c.numberofGenerations - 1:
            self.Show_Best()
    
    def Evolve_For_One_Generation(self):

        self.Spawn()
        self.Mutate()
        self.child.Start_Simulation("DIRECT")
        self.Print()
        self.Select()
        
    
    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    #def Evaluate(self):
        #pass

    def Select(self):
        intID = int(self.nextAvailableID) - 1
        print("INTID:")
        print(intID)
        print(self.parents[intID].fitness)
        print(self.child.fitness)
        if self.child.fitness >= self.parents[intID].fitness:
            self.parent = self.child

    def Print(self):
        printID = self.nextAvailableID
        print("/n")
        print("Parent Fitness: ")
        print(self.parents[printID].fitness)
        print("Child Fitness: ")
        print(self.child.fitness)
        pass

    def Show_Best(self):
        self.parent.Evaluate("GUI")
        quit()


