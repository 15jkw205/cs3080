'''
Problem #3
'''

import random

total_distance = 0
num_tracks = int(input("Enter number of tracks: "))
num_trials = int(input("Enter how many runs to make: "))

for i in range(num_trials):
    starting_track = random.randint(0, num_tracks - 1)
    target_track = random.randint(0, num_tracks - 1)

    distance_moved = abs(target_track - starting_track)
    total_distance += distance_moved

average_distance = total_distance / num_trials

print("\nSIMULATION RESULTS")
print(f"Number of tracks: {num_tracks}")
print(f"Number of runs: {num_trials}")
print(f"Average distance: {average_distance: .2f} tracks")
