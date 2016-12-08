"""
--- Part Two ---

Of course, that would be the message - if you hadn't agreed to use a modified repetition code instead.

In this modified code, the sender instead transmits what looks like random data, but for each character, the character
they actually want to send is slightly less likely than the others. Even after signal-jamming noise, you can look at the
letter distributions in each column and choose the least common letter to reconstruct the original message.

In the above example, the least common character in the first column is a; in the second, d, and so on. Repeating this
process for the remaining characters produces the original message, advent.

Given the recording in your puzzle input and this new decoding methodology, what is the original message that Santa is
trying to send?
"""
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
