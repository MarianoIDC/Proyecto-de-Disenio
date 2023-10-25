import numpy as np


class Particle:

    def __init__(self, dim):
        self.position = np.random.rand(dim)
        self.velocity = np.random.rand(dim)
        self.best_position = self.position
        self.best_fitness = float('inf')

    def update_velocity(self, inertia, cognitive_coeff, social_coeff, global_best_position):
        inertia_term = inertia * self.velocity
        cognitive_term = cognitive_coeff * np.random.rand() * (self.best_position - self.position)
        social_term = social_coeff * np.random.rand() * (global_best_position - self.position)
        self.velocity = inertia_term + cognitive_term + social_term

    def update_position(self):
        self.position += self.velocity

class Swarm:
    def __init__(self, num_particles, dim):
        self.num_particles = num_particles
        self.particles = [Particle(dim) for _ in range(num_particles)]
        self.global_best_position = self.get_global_best_position()

    def get_global_best_position(self):
        best_particle = min(self.particles, key=lambda particle: particle.best_fitness)
        return best_particle.best_position

    def update_particles(self, inertia, cognitive_coeff, social_coeff):
        for particle in self.particles:
            fitness = self.evaluate(particle.position)
            if fitness < particle.best_fitness:
                particle.best_fitness = fitness
                particle.best_position = particle.position

        self.global_best_position = self.get_global_best_position()

        for particle in self.particles:
            particle.update_velocity(inertia, cognitive_coeff, social_coeff, self.global_best_position)
            particle.update_position()

    def evaluate(self, position):
        # The objective function to be minimized
        # Replace this with your own objective function
        return sum(position**2)

def particle_swarm_optimization(num_particles, dim, num_iterations, inertia, cognitive_coeff, social_coeff):
    swarm = Swarm(num_particles, dim)

    for _ in range(num_iterations):
        swarm.update_particles(inertia, cognitive_coeff, social_coeff)

    best_solution = swarm.get_global_best_position()
    best_fitness = swarm.evaluate(best_solution)

    return best_solution, best_fitness

if __name__ == "__main__":
    NUM_PARTICLES = 30
    dim = 2
    num_iterations = 100
    inertia = 0.5
    cognitive_coeff = 1.5
    social_coeff = 2.0

    best_solution, best_fitness = particle_swarm_optimization(NUM_PARTICLES, dim, num_iterations, inertia, cognitive_coeff, social_coeff)

    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
