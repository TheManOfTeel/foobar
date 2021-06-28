import numpy as np

# Find all distinct directions that you can shoot your trainer using mirrors
def solution(dimensions, your_position, trainer_position, distance):
    mirrored = [
        mirror_translation(your_position, dimensions, distance),
        mirror_translation(trainer_position, dimensions, distance)
        ]
    hits = set()
    angles_dict = {}
    for i in range(0, len(mirrored)):
        for j in mirrored[i][0]:
            for k in mirrored[i][1]:
                # Calculate angle from ray to point
                beam = np.arctan2((your_position[1] - k), (your_position[0] - j))
                # Calculate the distance between you and your target
                distance_from_target = np.sqrt(np.square(your_position[0] - j) + np.square(your_position[1] - k))
                if [j, k] != your_position and distance >= distance_from_target:
                    if((beam in angles_dict and angles_dict[beam] > distance_from_target) or beam not in angles_dict):
                        if i == 0:
                            # Add to the dictionary
                            angles_dict[beam] = distance_from_target
                        else:
                            # Add to the dictionary
                            angles_dict[beam] = distance_from_target
                            # It's a hit
                            hits.add(beam)
    # The number of beams that hit the trainer and are unique
    return len(hits)

# Create the array of mirrors given a position, dimensions of the room, and the max distance the beam can travel
def mirror_translation(node, dimensions, distance):
    mirror_translations = []
    for i in range(len(node)):
        mirrored_pts = []
        for j in range(-(distance // dimensions[i]) - 1, (distance // dimensions[i] + 2)):
            mirrored_pts.append(mirror_coordinates(j, node[i], dimensions[i]))
        mirror_translations.append(mirrored_pts)
    return mirror_translations

# Manipulate the input coordinates to get the mirror of a set of coordinates
def mirror_coordinates(mirror, coordinates, dimensions):
    mirrored_coordinates = coordinates
    mirror_rotation = [2 * coordinates, 2 * (dimensions - coordinates)]
    if(mirror < 0):
        for i in range(mirror, 0):
            mirrored_coordinates -= mirror_rotation[(i + 1) % 2]
    else:
        for i in range(mirror, 0, -1):
            mirrored_coordinates += mirror_rotation[i % 2]
    return mirrored_coordinates

# Test function
def main():
    print(solution([3,2], [1,1], [2,1], 4))

# Run test
main()