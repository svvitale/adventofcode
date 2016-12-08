"""
--- Day 7: Internet Protocol Version 7 ---

While snooping around the local network of EBHQ, you compile a list of IP addresses (they're IPv7, of course; IPv6 is much too limited). You'd like to figure out which IPs support TLS (transport-layer snooping).

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA. An ABBA is any four-character sequence which consists of a pair of two different characters followed by the reverse of that pair, such as xyyx or abba. However, the IP also must not have an ABBA within any hypernet sequences, which are contained by square brackets.

For example:

abba[mnop]qrst supports TLS (abba outside square brackets).
abcd[bddb]xyyx does not support TLS (bddb is within square brackets, even though xyyx is outside square brackets).
aaaa[qwer]tyui does not support TLS (aaaa is invalid; the interior characters must be different).
ioxxoj[asdfgh]zxcvbn supports TLS (oxxo is outside square brackets, even though it's within a larger string).
How many IPs in your puzzle input support TLS?
"""
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

