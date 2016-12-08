"""
--- Part Two ---

Then, you notice the instructions continue on the back of the Recruiting Document. Easter Bunny HQ is actually at the
first location you visit twice.

For example, if your instructions are R8, R4, R4, R8, the first location you visit twice is 4 blocks away, due East.

How many blocks away is the first location you visit twice?
"""
import sys

input_data = "R4, R4, L1, R3, L5, R2, R5, R1, L4, R3, L5, R2, L3, L4, L3, R1, R5, R1, L3, L1, R3, L1, R2, R2, L2, " \
             "R5, L3, L4, R4, R4, R2, L4, L1, R5, L1, L4, R4, L1, R1, L2, R5, L2, L3, R2, R1, L194, R2, L4, R49, " \
             "R1, R3, L5, L4, L1, R4, R2, R1, L5, R3, L5, L4, R4, R4, L2, L3, R78, L5, R4, R191, R4, R3, R1, L2, " \
             "R1, R3, L1, R3, R4, R2, L2, R1, R4, L5, R2, L2, L4, L2, R1, R2, L3, R5, R2, L3, L3, R3, L1, L1, R5, " \
             "L4, L4, L2, R5, R1, R4, L3, L5, L4, R5, L4, R5, R4, L3, L2, L5, R4, R3, L3, R1, L5, R5, R1, L3, R2, " \
             "L5, R5, L3, R1, R4, L5, R4, R2, R3, L4, L5, R3, R4, L5, L5, R4, L4, L4, R1, R5, R3, L1, L4, L3, L4, " \
             "R1, L5, L1, R2, R2, R4, R4, L5, R4, R1, L1, L1, L3, L5, L2, R4, L3, L5, L4, L1, R3"

current_direction = 0
x = 0
y = 0
locations_visited = set()

def check_for_hq():
    if (x, y) in locations_visited:
        final_distance = abs(x) + abs(y)
        print('Final coordinates are {}, {}.  Taxi distance of {} from start'.format(x, y, final_distance))
        sys.exit(0)
    else:
        locations_visited.add((x, y))

for instruction in input_data.split(', '):
    direction = instruction[0]
    distance = int(instruction[1:])

    # Suss out our direction
    if direction == 'R':
        current_direction += 1
    else:
        current_direction -= 1

    if current_direction == -1:
        current_direction = 3

    if current_direction == 4:
        current_direction = 0

    # Walk
    if current_direction == 0:
        # Part 2
        for step in range(distance):
            y += 1
            check_for_hq()
    elif current_direction == 1:
        # Part 2
        for step in range(distance):
            x += 1
            check_for_hq()
    elif current_direction == 2:
        # Part 2
        for step in range(distance):
            y -= 1
            check_for_hq()
    elif current_direction == 3:
        # Part 2
        for step in range(distance):
            x -= 1
            check_for_hq()

final_distance = abs(x) + abs(y)
print('Final coordinates are {}, {}.  Taxi distance of {} from start'.format(x, y, final_distance))
sys.exit(0)