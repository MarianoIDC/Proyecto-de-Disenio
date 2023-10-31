import numpy as np

# Define the environment
grid_size = 10  # Grid size (e.g., 10x10)
obstacles = [(2, 2), (4, 4), (6, 6)]  # Obstacle locations

# PSO parameters
num_particles = 30
num_dimensions = 2  # 2D space (x, y)
max_iterations = 100
c1 = 1.5  # Cognitive parameter
c2 = 1.5  # Social parameter
w = 0.7  # Inertia weight

# Initialize particles
particles = np.random.rand(num_particles, num_dimensions) * grid_size
velocities = np.zeros((num_particles, num_dimensions))
best_positions = particles.copy()
best_scores = np.full(num_particles, np.inf)

# Function to calculate the fitness of a particle
def fitness(particle):
    # Calculate the distance to obstacles
    distance_to_obstacles = [np.sqrt((particle[0] - obs[0])**2 + (particle[1] - obs[1])**2) for obs in obstacles]
    return sum(distance_to_obstacles)

# Main PSO loop
for iteration in range(max_iterations):
    for i in range(num_particles):
        particle = particles[i]
        score = fitness(particle)

        if score < best_scores[i]:
            best_scores[i] = score
            best_positions[i] = particle

        global_best = best_positions[np.argmin(best_scores)]

        # Update velocity and position
        r1, r2 = np.random.rand(2)
        velocities[i] = w * velocities[i] + c1 * r1 * (best_positions[i] - particle) + c2 * r2 * (global_best - particle)
        particles[i] += velocities[i]

        # Ensure particles stay within the grid
        particles[i] = np.clip(particles[i], 0, grid_size)

# Print the best position found
print("Best position:", global_best)