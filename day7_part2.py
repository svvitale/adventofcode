"""
--- Part Two ---

You would also like to know which IPs support SSL (super-secret listening).

An IP supports SSL if it has an Area-Broadcast Accessor, or ABA, anywhere in the supernet sequences (outside any square
bracketed sections), and a corresponding Byte Allocation Block, or BAB, anywhere in the hypernet sequences. An ABA is
any three-character sequence which consists of the same character twice with a different character between them, such as
 xyx or aba. A corresponding BAB is the same characters but in reversed positions: yxy and bab, respectively.

For example:

aba[bab]xyz supports SSL (aba outside square brackets with corresponding bab within square brackets).
xyx[xyx]xyx does not support SSL (xyx, but no corresponding yxy).
aaa[kek]eke supports SSL (eke in supernet with corresponding kek in hypernet; the aaa sequence is not related, because
the interior character must be different).
zazbz[bzb]cdb supports SSL (zaz has no corresponding aza, but zbz has a corresponding bzb, even though zaz and zbz
overlap).
How many IPs in your puzzle input support SSL?
"""
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

