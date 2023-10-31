import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class Particle:
    def __init__(self, dim, bounds):
        self.position = np.random.uniform(bounds[0], bounds[1], dim)
        self.velocity = np.random.uniform(-1, 1, dim)
        self.best_position = np.copy(self.position)
        self.best_fitness = float('inf')

    def update_velocity(self, inertia, cognitive_coeff, social_coeff, global_best_position):
        inertia_term = inertia * self.velocity
        cognitive_term = cognitive_coeff * np.random.rand() * (self.best_position - self.position)
        social_term = social_coeff * np.random.rand() * (global_best_position - self.position)
        self.velocity = inertia_term + cognitive_term + social_term

    def update_position(self, bounds):
        self.position += self.velocity
        self.position = np.clip(self.position, bounds[0], bounds[1])

    def evaluate_fitness(self, terrain):
        # Evaluate fitness based on terrain coverage
        # Replace this with your own terrain coverage evaluation function
        # Here, we assume a simple 2D terrain with a peak at (3, 3)
        terrain_peak = np.array([3, 3])
        self.best_fitness = np.linalg.norm(self.position - terrain_peak)

class Swarm:
    def __init__(self, num_particles, dim, bounds):
        self.num_particles = num_particles
        self.particles = [Particle(dim, bounds) for _ in range(num_particles)]
        self.global_best_position = self.get_global_best_position()

    def get_global_best_position(self):
        best_particle = min(self.particles, key=lambda particle: particle.best_fitness)
        return np.copy(best_particle.best_position)

    def update_particles(self, terrain, inertia, cognitive_coeff, social_coeff):
        for particle in self.particles:
            particle.evaluate_fitness(terrain)
            if particle.best_fitness < particle.best_fitness:
                particle.best_fitness = particle.best_fitness
                particle.best_position = np.copy(particle.position)

        self.global_best_position = self.get_global_best_position()

        for particle in self.particles:
            particle.update_velocity(inertia, cognitive_coeff, social_coeff, self.global_best_position)
            particle.update_position(bounds)

def plot_terrain_coverage(swarm, terrain):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x, y = np.meshgrid(np.linspace(bounds[0][0], bounds[1][0], 100), np.linspace(bounds[0][1], bounds[1][1], 100))
    z = terrain(x, y)

    ax.plot_surface(x, y, z, alpha=0.5, cmap='viridis')

    positions = np.array([particle.best_position for particle in swarm.particles])
    ax.scatter(positions[:, 0], positions[:, 1], [terrain(pos[0], pos[1]) for pos in positions], c='r', marker='o')

    plt.show()

def terrain(x, y):
    # Example terrain function, replace with your own
    return np.sin(np.sqrt(x**2 + y**2))

if __name__ == "__main__":
    num_particles = 30
    dim = 2
    bounds = [(-5, -5), (5, 5)]
    num_iterations = 100
    inertia = 0.5
    cognitive_coeff = 1.5
    social_coeff = 2.0

    swarm = Swarm(num_particles, dim, bounds)

    for _ in range(num_iterations):
        swarm.update_particles(terrain, inertia, cognitive_coeff, social_coeff)

    best_solution = swarm.get_global_best_position()
    best_fitness = terrain(best_solution[0], best_solution[1])

    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)

    plot_terrain_coverage(swarm, terrain)
