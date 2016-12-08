"""
--- Day 6: Signals and Noise ---

Something is jamming your communications with Santa. Fortunately, your signal is only partially jammed, and protocol in situations like this is to switch to a simple repetition code to get the message through.

In this model, the same message is sent repeatedly. You've recorded the repeating message signal (your puzzle input), but the data seems quite corrupted - almost too badly to recover. Almost.

All you need to do is figure out which character is most frequent for each position. For example, suppose you had recorded the following messages:

eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar
The most common character in the first column is e; in the second, a; in the third, s, and so on. Combining these characters returns the error-corrected message, easter.

Given the recording in your puzzle input, what is the error-corrected version of the message being sent?
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
    print(sorted(char_counts[position], key=lambda x: char_counts[position][x], reverse=True)[0], end='')
