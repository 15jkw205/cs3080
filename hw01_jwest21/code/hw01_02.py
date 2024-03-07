'''
Problem #2
'''

import random
import math

inside_circle = 0
num_trials = int(input("Enter how many runs to make: "))

for i in range(num_trials):

    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if math.sqrt(x**2 + y**2) <= 1:
        inside_circle += 1

pi_estimate = (inside_circle / num_trials) * 4
error_percentage = ((pi_estimate - math.pi) / math.pi) * 100

print("\nESTIMATE OF PI")
print(f"NUMBER of runs: {num_trials}")
print(f"Estimate of pi: {pi_estimate: .8f}")
print(f"Error: {error_percentage: f} %")

