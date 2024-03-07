# Monte Carlo Simulation
import random

# Input from user (width, height, number of runs)
w = float(input("width: "))
l = float(input("length: "))
runs = int(input("runs: "))

# For each run:
total = 0.0
for i in range(runs):

    # Pick two random points in the rectangle
    x1 = l * random.random()
    y1 = w * random.random()

    x2 = l * random.random()
    y2 = w * random.random()

    # Calculate the distance between the points
    dist = ( (x2-x1)**2 + (y2-y1)**2 )**0.5

    # Update a running total of the distances
    total += dist

# Calculate the average distance
avg_dist = total / runs

# Output a Report
print(avg_dist)