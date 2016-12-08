"""
--- Day 8: Two-Factor Authentication ---

You come across a door implementing what you can only assume is an implementation of two-factor authentication after a long game of requirements telephone.

To get past the door, you first swipe a keycard (no problem; there was one on a nearby desk). Then, it displays a code on a little screen, and you type that code on a keypad. Then, presumably, the door unlocks.

Unfortunately, the screen has been smashed. After a few minutes, you've taken everything apart and figured out how it works. Now you just have to work out what the screen would have displayed.

The magnetic strip on the card you swiped encodes a series of instructions for the screen; these instructions are your puzzle input. The screen is 50 pixels wide and 6 pixels tall, all of which start off, and is capable of three somewhat peculiar operations:

rect AxB turns on all of the pixels in a rectangle at the top-left of the screen which is A wide and B tall.
rotate row y=A by B shifts all of the pixels in row A (0 is the top row) right by B pixels. Pixels that would fall off the right end appear at the left end of the row.
rotate column x=A by B shifts all of the pixels in column A (0 is the left column) down by B pixels. Pixels that would fall off the bottom appear at the top of the column.
For example, here is a simple sequence on a smaller screen:

rect 3x2 creates a small rectangle in the top-left corner:

###....
###....
.......
rotate column x=1 by 1 rotates the second column down by one pixel:

#.#....
###....
.#.....
rotate row y=0 by 4 rotates the top row right by four pixels:

....#.#
###....
.#.....
rotate column x=1 by 1 again rotates the second column down by one pixel, causing the bottom pixel to wrap back to the top:

.#..#.#
#.#....
.#.....
As you can see, this display technology is extremely powerful, and will soon dominate the tiny-code-displaying-screen
market. That's what the advertisement on the back of the display tries to convince you, anyway.

There seems to be an intermediate check of the voltage used by the display: after you swipe your card, if the screen did
 work, how many pixels should be lit?
"""
import re

cmd_parser = re.compile(r'((?P<rect>rect) (?P<width>\d+)x(?P<height>\d+))|'
                        r'((?P<rotate>rotate) (?P<direction>row|column) (x|y)=(?P<r1>\d+) by (?P<r2>\d+))')


def rotate(list_obj, count):
    return list_obj[-count:] + list_obj[:-count]

# input_data = """rect 3x2
# rotate column x=1 by 1
# rotate row y=0 by 4
# rotate column x=1 by 1"""
#
# grid_size = (7, 3)

input_data = open('day8_input.txt').read()
grid_size = (50, 6)

# Create a fixed size deque for each display row and initialize with 0's
grid = [[0 for _ in range(grid_size[0])] for _ in range(grid_size[1])]

for line in input_data.strip().split('\n'):
    # Parse the command
    match = cmd_parser.match(line)

    if match.group('rect'):
        for row in range(int(match.group('height'))):
            for col in range(int(match.group('width'))):
                grid[row][col] = 1
    elif match.group('rotate'):
        rotation_count = int(match.group('r2'))

        if match.group('direction') == 'row':
            row = int(match.group('r1'))
            grid[row] = rotate(grid[row], rotation_count)
        elif match.group('direction') == 'column':
            column = int(match.group('r1'))
            column_values = rotate([row_data[column] for row_data in grid], rotation_count)
            for idx, row in enumerate(grid):
                row[column] = column_values[idx]

pixel_count = 0

for row in grid:
    pixel_count += row.count(1)

print(pixel_count)