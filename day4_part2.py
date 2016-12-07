# aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z, which are listed alphabetically.
# a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
# not-a-real-room-404[oarel] is a real room.
# totally-real-room-200[decoy] is not.

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


def decrypt(room_name, sector_id):
    shift_count = int(sector_id) % 26

    for char in room_name:
        if char == '-':
            print(' ', end='')
        else:
            new_letter_ord = ord(char) + shift_count
            if new_letter_ord > ord('z'):
                new_letter_ord -= 26
            print(chr(new_letter_ord), end='')

    print('', sector_id)


for line in input_data.strip().replace('\r', '').split('\n'):
    room_name, sector_id, checksum = re.match(r'(.*)-(\d+)\[(.*)\]', line.strip()).groups()

    occurrences = {}

    for char in room_name.replace('-', ''):
        if char not in occurrences:
            occurrences[char] = 1
        else:
            occurrences[char] += 1

    if calc_checksum(occurrences) == checksum:
        # Real room, now decrypt the name
        decrypt(room_name, sector_id)
