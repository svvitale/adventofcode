"""
--- Part Two ---

Apparently, the file actually uses version two of the format.

In version two, the only difference is that markers within decompressed data are decompressed. This,
the documentation explains, provides much more substantial compression capabilities, allowing many-gigabyte files to
be stored in only a few kilobytes.

For example:

- (3x3)XYZ still becomes XYZXYZXYZ, as the decompressed section contains no markers.
- X(8x2)(3x3)ABCY becomes XABCABCABCABCABCABCY, because the decompressed data from the (8x2) marker is then further
    decompressed, thus triggering the (3x3) marker twice for a total of six ABC sequences.
- (27x12)(20x12)(13x14)(7x10)(1x12)A decompresses into a string of A repeated 241920 times.
- (25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN becomes 445 characters long.

Unfortunately, the computer you brought probably doesn't have enough memory to actually decompress the file; you'll
have to come up with another way to get its decompressed length.

What is the decompressed length of the file using this improved format?
"""
import re

# input_data = '(3x3)XYZ'
# input_data = 'X(8x2)(3x3)ABCY'
# input_data = '(27x12)(20x12)(13x14)(7x10)(1x12)A'
# input_data = '(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
# input_data = '(3x3)ABC(2x3)XY(5x2)PQRST(3x3)ABC(2x3)XY(5x2)PQRST(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN'
input_data = open('day9_input.txt').read()

marker_regex = re.compile(r'\((\d+)x(\d+)\)')


def get_decompressed_length(segment):

    segment_match = marker_regex.search(segment)

    if segment_match:
        segment_length = 0
        str_to_repeat_end_idx = 0

        while segment_match:
            segment_length += segment_match.span()[0] - str_to_repeat_end_idx

            length_to_repeat = int(segment_match.group(1))
            repetitions = int(segment_match.group(2))

            str_to_repeat_start_idx = segment_match.span()[1]
            str_to_repeat_end_idx = str_to_repeat_start_idx + length_to_repeat

            subsegment = segment[str_to_repeat_start_idx:str_to_repeat_end_idx]
            subsegment_length = get_decompressed_length(subsegment)
            segment_length += repetitions * subsegment_length

            segment_match = marker_regex.search(segment, str_to_repeat_end_idx)

        # Add the remainder
        segment_length += len(segment) - str_to_repeat_end_idx
    else:
        segment_length = len(segment)

    return segment_length

print(get_decompressed_length(input_data))
