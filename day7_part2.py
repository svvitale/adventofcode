import re

input_data = open('day7_input.txt').read()

# input_data = """aba[bab]xyz
# xyx[xyx]xyx
# aaa[kek]eke
# zazbz[bzb]cdb"""


def is_aba(char_str):
    return char_str[0] == char_str[2] and char_str[0] != char_str[1]


def invert(aba):
    return aba[1] + aba[0] + aba[1]


def iter_abas(char_str):
    for idx in range(len(char_str) - 2):
        if is_aba(char_str[idx:idx + 3]):
            yield char_str[idx:idx + 3]


def is_line_ssl(line):
    # Find all super nets
    supernets = re.split(r'\[.*?\]', line)

    # Iterate over hypernets
    for match in re.finditer(r'\[(.*?)\]', line):
        # Iterate over aba sequences in the hypernets
        for aba in iter_abas(match.group(1)):
            # Iterate over the supernets to see if the bab of our aba exists there
            for supernet in supernets:
                if invert(aba) in supernet:
                    return 1

    return 0


tls_count = 0

for line in input_data.strip().split('\n'):
    tls_count += is_line_ssl(line)


print(tls_count)

