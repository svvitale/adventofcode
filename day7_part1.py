import re

input_data = open('day7_input.txt').read()

# input_data = """abba[mnop]qrst
# abcd[bddb]xyyx
# aaaa[qwer]tyui
# ioxxoj[asdfgh]zxcvbn"""


def is_abba(char_str):
    return char_str[0] == char_str[3] and char_str[1] == char_str[2] and char_str[0] != char_str[1]


def contains_abba(char_str):
    for idx in range(len(char_str) - 3):
        if is_abba(char_str[idx:idx + 4]):
            return True

    return False


tls_count = 0

for line in input_data.strip().split('\n'):
    negated = False

    for match in re.finditer(r'\[(.*?)\]', line):
        # Look for any negations first (we always need to do this)
        if contains_abba(match.group(1)):
            negated = True
            break

    if negated:
        continue

    # Now look for any possibilities
    for possible in re.sub(r'\[(.*?)\]', ',', line).split(','):
        if contains_abba(possible):
            tls_count += 1
            break

print(tls_count)

