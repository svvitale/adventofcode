"""
--- Day 4: Security Through Obscurity ---

Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy
data, but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a
checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order,
with ties broken by alphabetization. For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x,
y, and z, which are listed alphabetically. a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are
all tied (1 of each), the first five are listed alphabetically. not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not. Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""
import re
input_data = open('day4_input.txt').read()
# input_data = """aaaaa-bbb-z-y-x-123[abxyz]
# a-b-c-d-e-f-g-h-987[abcde]
# not-a-real-room-404[oarel]
# totally-real-room-200[decoy]"""

sector_total = 0


def calc_checksum(occurrences):
    checksum = ''

    for next_char in sorted(occurrences, key=lambda c: (occurrences[c], -ord(c)), reverse=True):
        checksum += next_char
        if len(checksum) == 5:
            return checksum

    return checksum

for line in input_data.strip().replace('\r', '').split('\n'):
    room_name, sector_id, checksum = re.match(r'(.*)-(\d+)\[(.*)\]', line.strip()).groups()
    room_name = room_name.replace('-', '')

    occurrences = {}

    for char in room_name:
        if char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1

    if calc_checksum(occurrences) == checksum:
        sector_total += int(sector_id)

print('Sector total:', sector_total)
