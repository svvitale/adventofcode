"""
--- Part Two ---

With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right
software. However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master
cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector
ID. A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
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
