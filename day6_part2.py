input_data = open('day6_input.txt').read()

# input_data = """eedadn
# drvtee
# eandsr
# raavrd
# atevrs
# tsrnev
# sdttsa
# rasrtv
# nssdts
# ntnada
# svetve
# tesnvt
# vntsnd
# vrdear
# dvrsen
# enarar"""

char_counts = {}

for line in input_data.strip().split('\n'):
    for char_idx in range(len(line.strip())):
        if char_idx not in char_counts:
            char_counts[char_idx] = {}

        if line[char_idx] in char_counts[char_idx]:
            char_counts[char_idx][line[char_idx]] += 1
        else:
            char_counts[char_idx][line[char_idx]] = 1

for position in sorted(char_counts):
    print(sorted(char_counts[position], key=lambda x: char_counts[position][x], reverse=False)[0], end='')
