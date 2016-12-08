"""
--- Part Two ---

You notice that the screen is only capable of displaying capital letters; in the font it uses, each letter is 5 pixels
wide and 6 tall.

After you swipe your card, what code is the screen trying to display?
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

for row in grid:
    for idx, col in enumerate(row):
        if col == 1:
            print('#', end='')
        else:
            print(' ', end='')

        if idx % 10:
            print('   ', end='')


    print(repr(row))
