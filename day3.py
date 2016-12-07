import re
input_data = open('day3_input.txt').read()
#input_data = ' 10 5 25 '
valid_count = 0
total = 0

# Part 1
# for line in input_data.strip().replace('\r', '').split('\n'):
#
#     a, b, c = map(int, re.split('\s+', line.strip()))
#
#     if (a + b) > c and (a + c) > b and (b + c) > a:
#         valid_count += 1
#
#     total += 1

# Part 2
def is_valid(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a

lines = input_data.strip().replace('\r', '').split('\n')

for line_idx in range(0, len(lines), 3):
    a1, b1, c1 = map(int, re.split('\s+', lines[line_idx].strip()))
    a2, b2, c2 = map(int, re.split('\s+', lines[line_idx + 1].strip()))
    a3, b3, c3 = map(int, re.split('\s+', lines[line_idx + 2].strip()))

    if is_valid(a1, a2, a3):
        valid_count += 1

    if is_valid(b1, b2, b3):
        valid_count += 1

    if is_valid(c1, c2, c3):
        valid_count += 1

print('{} / {}'.format(valid_count, total))