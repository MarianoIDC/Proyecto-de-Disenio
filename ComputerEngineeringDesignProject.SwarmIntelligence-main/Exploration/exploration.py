# Import libraries
import random
import math
import time
import numpy as np
import pybullet as p
import pybullet_data
import tkinter
from tkinter import *
from tkinter import messagebox
from constants import *

# Particle class definition
class Particle:
    
    def __init__(self, positionX, positionY):

        self.positionX = positionX
        self.positionY = positionY
        self.positionZ = DRONE_Z_POSITION
        self.bestPositionX = positionX
        self.bestPositionY = positionY
        self.velocityX = 0.0
        self.velocityY = 0.0
        self.rayFrom = []
        self.rayTo = []

        # Fitness criteria
        f1 = (self.positionX - PI) ** 2
        f2 = (self.positionY - EULER) ** 2
        f3 = np.sin(3 * self.positionX + FIRST_PARAMETER)
        f4 = np.sin(4 * self.positionY + SECOND_PARAMETER)

        self.fitness = f1 + f2 + f3 + f4

        self.orientation = DRONE_ORIENTATION

        particlePosition = [self.positionX, self.positionY, self.positionZ]

        self.drone = p.loadURDF(DRONE_URDF, particlePosition, self.orientation)

    def getPositionX(self):

        return self.positionX

    def getPositionY(self):
    
        return self.positionY

    def getFitness(self):
        
        return self.fitness

    # Update position function definition
    def updatePosition(self):

        for i in range(NUMBER_RAYS):
            
            self.rayFrom.append([self.positionX, self.positionY, self.positionZ])

            self.rayTo.append([math.sin(2. * math.pi * float(i) / NUMBER_RAYS) + self.positionX,
                               math.cos(2. * math.pi * float(i) / NUMBER_RAYS) + self.positionY,
                               self.positionZ])

        for j in range(NUMBER_RAYS):
            
            results = p.rayTestBatch(self.rayFrom, self.rayTo, j + 1)

        hitFlag = False

        counter = 0

        for k in range(NUMBER_RAYS):
            
            hitObject = results[k][0]

            if(hitObject >= 0):

                hitFlag = True

                counter += 1
                
        if(hitFlag == False):

            self.positionX += self.velocityX
            self.positionY += self.velocityY

            newPosition = [self.positionX, self.positionY, self.positionZ]

            p.resetBasePositionAndOrientation(self.drone, newPosition, self.orientation)

        else:

            # Logic of collision detection

            pass

        self.rayFrom = []
        self.rayTo = []

    # Update fitness function definition
    def updateFitness(self):

        f1 = (self.positionX - PI) ** 2
        f2 = (self.positionY - EULER) ** 2
        f3 = np.sin(3 * self.positionX + FIRST_PARAMETER)
        f4 = np.sin(4 * self.positionY + SECOND_PARAMETER)

        newFitness = f1 + f2 + f3 + f4

        # update fitness
        if(newFitness < self.fitness):
    
            self.fitness = newFitness

        # update best positions X and Y
        else:
            
            self.bestPositionX = self.positionX
            self.bestPositionY = self.positionY

    # Update velocity function definition
    def updateVelocity(self, bestParticle):    

        r1 = random.uniform(0, MAX_WEIGHT)
        r2 = random.uniform(0, MAX_WEIGHT)
        w = random.uniform(MIN_WEIGHT, MAX_WEIGHT)
        c1 = COGNITIVE_PARAMETER
        c2 = SOCIAL_PARAMETER

        inertiaX = w * self.velocityX
        cognitiveX = c1 * r1 * (self.bestPositionX - self.positionX)
        socialX = c2 * r2 * (bestParticle.getPositionX() - self.positionX)

        self.velocityX = inertiaX + cognitiveX + socialX

        inertiaY = w * self.velocityY
        cognitiveY = c1 * r1 * (self.bestPositionY - self.positionY)
        socialY = c2 * r2 * (bestParticle.getPositionY() - self.positionY)

        self.velocityY = inertiaY + cognitiveY + socialY

# Swarm class definition
class Swarm:

    def __init__(self, population):

        self.swarm = []

        # Create swarm  
        for p in range(population):

            posX = random.uniform(MIN_POSITION, MAX_POSITION)
            posY = random.uniform(MIN_POSITION, MAX_POSITION)

            newParticle = Particle(posX, posY)

            self.swarm.append(newParticle)

        self.bestParticle = self.swarm[0]

        # Update best particle
        swarmFitness = []

        for p in self.swarm:            

            swarmFitness.append(p.getFitness())

        bestParticleIndex = np.argmin(swarmFitness)

        # Global best particle position
        self.bestParticle = self.swarm[bestParticleIndex]

    def getSwarm(self):

        return self.swarm
    
    def getBestParticle(self):

        return self.bestParticle

    # Update swarm fitness function definition
    def updateSwarmFitness(self):

        for p in self.swarm:

            p.updateFitness()

    # Update best particle function definition
    def updateBestParticle(self):

        swarmFitness = []

        for p in self.swarm:

            swarmFitness.append(p.getFitness())

        bestParticleIndex = np.argmin(swarmFitness)

        # Global best particle position
        self.bestParticle = self.swarm[bestParticleIndex]
        
# PSO function definition
def pso(swarm):

    iterations = 0

    # Infinite loop
    while True:

        # Stop if the average fitness value reached a predefined success criterion
        if np.average(swarm.getBestParticle().getFitness()) <= MAX_ITERATION:

            break

        else:

            for p in swarm.getSwarm():
                
                # Update the velocity of each particle
                p.updateVelocity(swarm.getBestParticle())

                # Update the position of each particle
                p.updatePosition()

            # Update fitness for each particle
            swarm.updateSwarmFitness()

        # Update the best particle
        swarm.updateBestParticle()

        time.sleep(0.15)

        iterations += 1

    globalBestPosition = [swarm.getBestParticle().getPositionX(), swarm.getBestParticle().getPositionY()]
    bestFitnessValue = swarm.getBestParticle().getFitness()
    
    return [globalBestPosition, bestFitnessValue, iterations]

# Create wall function definition
def createWall(dimensions, color, basePosition, baseOrientation):

    boxCollisionId = p.createCollisionShape(shapeType = p.GEOM_BOX, halfExtents = dimensions)

    boxVisualId = p.createVisualShape(shapeType = p.GEOM_BOX, halfExtents = dimensions, rgbaColor = color)

    p.createMultiBody(MASS, boxCollisionId, boxVisualId, basePosition, baseOrientation)

# Create environment function definition
def createEnvironment():

    # Plane ----------------------------------------------------------------------------------------------------

    createWall(PLANE_DIMENSIONS, PLANE_COLOR, PLANE_POSITION, PLANE_ORIENTATION)

    # Vertical ----------------------------------------------------------------------------------------------------

    # Length 2 --------------------------------------------------

    dimensions = [2, 2.25, 0.25]

    basePosition = [-9.75, 6, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    # Length 4 --------------------------------------------------

    dimensions = [2, 4.25, 0.25]

    basePosition = [-11.75, 18, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    basePosition = [1, 18, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    basePosition = [-14, -18, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    basePosition = [12, -9, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    # Length 7 --------------------------------------------------

    dimensions = [2, 7.25, 0.25]

    basePosition = [4, -15, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    basePosition = [13, 15, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    # Length 9 --------------------------------------------------

    dimensions = [2, 9.25, 0.25]

    basePosition = [-6, -12.50, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    # Length 22 --------------------------------------------------

    dimensions = [2, 22.25, 0.25]

    basePosition = [-22, 0, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    basePosition = [22, 0, 2]

    createWall(dimensions, WALL_COLOR, basePosition, VERTICAL_ORIENTATION)

    # Horizontal ----------------------------------------------------------------------------------------------------

    # Length 1 --------------------------------------------------

    dimensions = [0.25, 1.25, 2]

    basePosition = [-13, -14, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    # Length 2 --------------------------------------------------

    dimensions = [0.25, 2.25, 2]

    basePosition = [-9.75, 14, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    basePosition = [-4, -3, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    # Length 3 --------------------------------------------------

    dimensions = [0.25, 3.25, 2]

    basePosition = [10, 8, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    # Length 4 --------------------------------------------------

    dimensions = [0.25, 4.25, 2]

    basePosition = [-5.75, 4, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    basePosition = [-18, 0, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    basePosition = [-18, -7, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    # Length 5 --------------------------------------------------

    dimensions = [0.25, 5.25, 2]

    basePosition = [17, -13, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    # Length 6 --------------------------------------------------

    dimensions = [0.25, 6.25, 2]

    basePosition = [-15.75, 8, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    basePosition = [16, 1, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    # Length 22 --------------------------------------------------

    dimensions = [0.25, 22.25, 2]

    basePosition = [0, 22, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

    basePosition = [0, -22, 2]

    createWall(dimensions, WALL_COLOR, basePosition, HORIZONTAL_ORIENTATION)

# Tkinter main window
class Window(tkinter.Tk):

    def __init__(self):

        tkinter.Tk.__init__(self)
        
        self.title("Drones con Inteligencia de Enjambre")
        self.geometry("400x200")
        
        self.label = Label(self, text = "Indique la cantidad\nde drones a simular", fg ='#4285f4', font = ("Serif", 14))
        self.label.place(x = 100, y = 20)

        self.entryPopulation = Entry(self, width = 20, justify = CENTER, font = ("Serif", 14))
        self.entryPopulation.place(x = 75, y = 80)
        
        self.buttonStart = Button(self, text = "Iniciar", fg = "white", bg = "#4285f4", font = ("Serif", 14),
                                  width = 15, heigh = 1, command = self.startSimulation)
        self.buttonStart.place(x = 100, y = 120)

    def startSimulation(self):
        
        # Population size
        population = int(self.entryPopulation.get())

        # Close Tkinter window
        self.destroy()

        # Pybullet GUI preparation
        p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())

        p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0)
        p.configureDebugVisualizer(p.COV_ENABLE_MOUSE_PICKING, 0)

        p.setRealTimeSimulation(1)
        p.setGravity(0, 0, GRAVITY)

        createEnvironment()

        time.sleep(3)

        # Swarm initialization
        swarm = Swarm(population)

        # Run PSO algorithm
        statistics = pso(swarm)

        time.sleep(3)

        p.disconnect()

        messagebox.showinfo("Estadisticas", "Cantidad de drones: " + str(population) + "\n\n" + 
                                            "Mejor posicion global:\n(" + str(statistics[0][0]) + ", " + str(statistics[0][1]) + ")\n\n" + 
                                            "Mejor valor de fitness: " + str(statistics[1]) + "\n\n" +
                                            "Numero de iteraciones: " + str(statistics[2]))

# Tkinter main window loop
Window().mainloop()
