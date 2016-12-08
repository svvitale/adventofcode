"""
--- Day 3: Squares With Three Sides ---

Now that you can think clearly, you move deeper into the labyrinth of hallways and office furniture that makes up
this part of Easter Bunny HQ. This must be a graphic design department; the walls are covered in specifications for
triangles.

Or are they?

The design document gives the side lengths of each triangle it describes, but... 5 10 25? Some of these aren't
triangles. You can't help but mark the impossible ones.

In a valid triangle, the sum of any two sides must be larger than the remaining side. For example, the "triangle"
given above is impossible, because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""
import re
input_data = open('day3_input.txt').read()
#input_data = ' 10 5 25 '
valid_count = 0
total = 0

for line in input_data.strip().replace('\r', '').split('\n'):

    a, b, c = map(int, re.split('\s+', line.strip()))

    if (a + b) > c and (a + c) > b and (b + c) > a:
        valid_count += 1

    total += 1
