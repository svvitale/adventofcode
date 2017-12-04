"""
--- Part Two ---

"Great work; looks like we're on the right track after all. Here's a star for your effort." However, the program seems a little worried. Can programs be worried?

"Based on what we're seeing, it looks like all the User wanted is some information about the evenly divisible values in the spreadsheet. Unfortunately, none of us are equipped for that kind of calculation - most of us specialize in bitwise operations."

It sounds like the goal is to find the only two numbers in each row where one evenly divides the other - that is, where the result of the division operation is a whole number. They would like you to find those numbers on each line, divide them, and add up each line's result.

For example, given the following spreadsheet:

5 9 2 8
9 4 7 3
3 8 6 5
In the first row, the only two numbers that evenly divide are 8 and 2; the result of this division is 4.
In the second row, the two numbers are 9 and 3; the result is 3.
In the third row, the result is 2.
In this example, the sum of the results would be 4 + 3 + 2 = 9.

What is the sum of each row's result in your puzzle input?
"""
import re

input_data = open('day2_input.txt').read().replace('\r', '').strip()

sum_of_even_division = 0

for row in input_data.split('\n'):

    numeric_columns = list(map(int, re.split(r'\s+', row)))
    found = False

    for divisor in numeric_columns:
        for multiple in numeric_columns:
            if multiple != divisor and multiple % divisor == 0:
                sum_of_even_division += (multiple // divisor)
                print("{} / {}".format(multiple, divisor))
                found = True
                break

        if found:
            break

print(sum_of_even_division)
