"""
--- Day 2: Corruption Checksum ---

As you walk through the door, a glowing humanoid shape yells in your direction. "You there! Your state appears to be idle. Come help us repair the corruption in this spreadsheet - if we take another millisecond, we'll have to display an hourglass cursor!"

The spreadsheet consists of rows of apparently-random numbers. To make sure the recovery process is on the right track, they need you to calculate the spreadsheet's checksum. For each row, determine the difference between the largest value and the smallest value; the checksum is the sum of all of these differences.

For example, given the following spreadsheet:

5 1 9 5
7 5 3
2 4 6 8
The first row's largest and smallest values are 9 and 1, and their difference is 8.
The second row's largest and smallest values are 7 and 3, and their difference is 4.
The third row's difference is 6.
In this example, the spreadsheet's checksum would be 8 + 4 + 6 = 18.

What is the checksum for the spreadsheet in your puzzle input?
"""
import re

input_data = open('day2_input.txt').read().replace('\r', '').strip()

checksum = 0

for row in input_data.split('\n'):

    current_min = current_max = None

    for column in re.split(r'\s+', row):
        value = int(column)

        if current_min is None:
            current_min = current_max = value

        if value < current_min:
            current_min = value

        if value > current_max:
            current_max = value

    checksum += (current_max - current_min)

print(checksum)
