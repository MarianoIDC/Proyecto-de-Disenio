"""
Source: https://towardsdatascience.com/swarm-intelligence-coding-and-visualising-particle-swarm-optimisation-in-python-253e1bd00772
Ken Moriwaki
Jun 15, 2022
"""

"""
Number of particles         : i
Number of dimensions        : n
Fitness function            : f(x_i)
Particles                   : x_i = (x_i1, x_i2, ..., x_in)
Current velocity            : v_i = (v_i1, v_i2, ..., v_in)
Individual particle's best  : p_i = (p_i1, p_i2, ..., p_in)
Global particles' best      : p_g = (p_g1, p_g2, ..., p_gn)
Inertia component           : w * v_i(t)
Cognitive component         : c_1 * r_1 * (p_i - x_i(t))
Social component            : c_2 * r_2 * (g_i - x_i(t))
Velocity adjustment         : v_i(t+1) = Inertia + Cognitive + Social
Position adjustment         : x_i(t+1) = x_i(t) + v_i(t+1)
"""

# Import libraries
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

# Fitness function definition
def fitnessFunction(x, y, xDestination, yDestination):

    aux1 = x - xDestination
    aux2 = y - yDestination
    z = (aux1 ** 2) + (aux2 ** 2)

    return z

# Velocity update
def velocityUpdate(particle, velocity, particleBest, globalBest):

    # Define weights
    minWeight = 0.5
    maxWeight = 1.0
    c = 0.1

    # Initialise new velocity array
    particleLength = len(particle)
    newVelocity = np.array([0.0 for i in range(particleLength)])

    # Randomly generate r1, r2 and inertia weight from normal distribution
    r1 = random.uniform(0, maxWeight)
    r2 = random.uniform(0, maxWeight)
    w = random.uniform(minWeight, maxWeight)
    c1 = c
    c2 = c

    # Calculate new velocity
    for i in range(particleLength):

        newVelocity[i] = w * velocity[i] + c1 * r1 * (particleBest[i] - particle[i]) + c2 * r2 * (globalBest[i] - particle[i])
        
    return newVelocity

# Position update
def positionUpdate(particle, velocity):

    # Move particles by adding velocity
    newParticle = particle + velocity

    return newParticle

# PSO main function
def pso(population, dimension, minPosition, maxPosition, generation, iterMax, xDestination, yDestination, ax):
    
    # Population
    particles = [[random.uniform(minPosition, maxPosition) for j in range(dimension)] for i in range(population)]

    # Particle's best position
    particleBestPosition = particles

    # Fitness
    particleBestFitness = [fitnessFunction(p[0], p[1], xDestination, yDestination) for p in particles]

    # Index of the best particle
    globalBestIndex = np.argmin(particleBestFitness)

    # Global best particle position
    globalBestPosition = particleBestPosition[globalBestIndex]

    # Velocity (starting from 0 speed)
    velocity = [[0.0 for j in range(dimension)] for i in range(population)]

    # Animation image placeholder
    images = []

    # Loop for the number of generation
    for t in range(generation):

        # Stop if the average fitness value reached a predefined success criterion
        if np.average(particleBestFitness) <= iterMax:

            break

        else:

            for n in range(population):

                # Update the velocity of each particle
                velocity[n] = velocityUpdate(particles[n], velocity[n], particleBestPosition[n], globalBestPosition)

                # Move the particles to new position
                particles[n] = positionUpdate(particles[n], velocity[n])

            # Add plot for each generation (within the generation for-loop)
            image = ax.scatter3D([particles[n][0] for n in range(population)],
                                 [particles[n][1] for n in range(population)],
                                 [fitnessFunction(particles[n][0], particles[n][1], xDestination, yDestination)
                                  for n in range(population)], c = "b")
            images.append([image])

            # Calculate the fitness value
            particleBestFitness = [fitnessFunction(p[0], p[1], xDestination, yDestination) for p in particles]

            # Find the index of the best particle
            globalBestIndex = np.argmin(particleBestFitness)

        # Update the position of the best particle
        globalBestPosition = particleBestPosition[globalBestIndex]

    # Print the results
    print("Global Best Position: ", globalBestPosition)
    print("Best Fitness Value: ", min(particleBestFitness))
    print("Average Particle Best Fitness Value: ", np.average(particleBestFitness))
    print("Number of Generation: ", t)

    return images

# Set PSO parameters
population = 10
dimension = 2
minPosition = -1000.0
maxPosition = 1000.0
generation = 400
iterMax = 10e-4

# Set Fitness parameters
xDestination = 500
yDestination = 100

# Plotting preparation
figure = plt.figure(figsize=(8, 8))

ax = figure.add_subplot(111, projection="3d")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")

x = np.linspace(minPosition, maxPosition, 80)
y = np.linspace(minPosition, maxPosition, 80)

X, Y = np.meshgrid(x, y)
Z = fitnessFunction(X, Y, xDestination, yDestination)

ax.plot_wireframe(X, Y, Z, color = "r", linewidth = 0.2)

# Run PSO algorithm
images = pso(population, dimension, minPosition, maxPosition, generation, iterMax, xDestination, yDestination, ax)

# Generate the animation and save it
animated_image = animation.ArtistAnimation(figure, images, interval = 125, blit = True)
animated_image.save("PSO/pso.gif", writer = "pillow") 

# Show animation
plt.show()
