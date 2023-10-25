"""
Source1: https://towardsdatascience.com/swarm-intelligence-coding-and-visualising-particle-swarm-optimisation-in-python-253e1bd00772
Source2: https://nathanrooy.github.io/posts/2016-08-17/simple-particle-swarm-optimization-with-python/
Source3: https://machinelearningmastery.com/a-gentle-introduction-to-particle-swarm-optimization/
Source4: https://gist.github.com/StuartGordonReid/7cff466efcad23e1deaf
Source5: https://gist.github.com/btbytes/79877
"""

# Import libraries
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from constants import *

# Particle class definition
class Particle:
    
    def __init__(self, positionX, positionY):

        self.positionX = positionX
        self.positionY = positionY
        self.bestPositionX = positionX
        self.bestPositionY = positionY
        self.velocityX = 0.0
        self.velocityY = 0.0

        # Fitness criteria
        f1 = (self.positionX - PI) ** 2
        f2 = (self.positionY - EULER) ** 2
        f3 = np.sin(3 * self.positionX + FIRST_PARAMETER)
        f4 = np.sin(4 * self.positionY + SECOND_PARAMETER)

        self.fitness = f1 + f2 + f3 + f4

    def getPositionX(self):

        return self.positionX

    def getPositionY(self):
    
        return self.positionY

    def getFitness(self):
        
        return self.fitness

    # Update position function definition
    def updatePosition(self):

        self.positionX += self.velocityX
        self.positionY += self.velocityY

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

        # update best particle
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
def pso(swarm, gif):

    # Animation image placeholder
    images = []

    # Loop for the number of generation
    for g in range(GENERATION):

        # Stop if the average fitness value reached a predefined success criterion
        if np.average(swarm.getBestParticle().getFitness()) <= MAX_ITERATION:

            break

        else:

            for p in swarm.getSwarm():

                # Update the velocity of each particle
                p.updateVelocity(swarm.getBestParticle())

                # Update the position of each particle
                p.updatePosition()
            
            # Add plot for each generation (within the generation for-loop)
            image = gif.scatter3D([i.getPositionX() for i in swarm.getSwarm()],
                                  [j.getPositionY() for j in swarm.getSwarm()],
                                  [k.getFitness() for k in swarm.getSwarm()], c = "b")
            images.append([image])

            # Update fitness for each particle
            swarm.updateSwarmFitness()

        # Update the best particle
        swarm.updateBestParticle()

    # Print the results
    print("Global Best Position: ", [swarm.getBestParticle().getPositionX(), swarm.getBestParticle().getPositionY()])
    print("Best Fitness Value: ", swarm.getBestParticle().getFitness())
    print("Number of Generation: ", g)

    return images

# Fitness criteria function definition
def fitnessCriteria(x, y):

    f1 = (x - PI) ** 2
    f2 = (y - EULER) ** 2
    f3 = np.sin(3 * x + FIRST_PARAMETER)
    f4 = np.sin(4 * y + SECOND_PARAMETER)

    z = f1 + f2 + f3 + f4

    return z

# Plotting preparation
figure = plt.figure(figsize=(8, 8))

gif = figure.add_subplot(111, projection="3d")
gif.set_xlabel("x")
gif.set_ylabel("y")
gif.set_zlabel("z")

x = np.linspace(MIN_POSITION, MAX_POSITION, 80)
y = np.linspace(MIN_POSITION, MAX_POSITION, 80)

X, Y = np.meshgrid(x, y)
Z = fitnessCriteria(X, Y)

gif.plot_wireframe(X, Y, Z, color = "r", linewidth = 0.2)

# Population size
population = 10

# Swarm initialization
swarm = Swarm(population)

# Run PSO algorithm
images = pso(swarm, gif)

# Generate the animation and save it
animated_image = animation.ArtistAnimation(figure, images, interval = 125, blit = True)

# Show animation
plt.show()
