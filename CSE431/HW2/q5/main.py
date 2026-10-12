# 8 mb bit array
num_bytes = 3 * 1024 * 1024
num_bits = num_bytes * 8
bit_array = bytearray(num_bytes)
bits_to_flip = 6

def get_bit_positions(item: str, bit_to_flip: int) -> list[int]:
    """
     returns different bit positions (switch numbers) for a given item.
    """
    positions = []
    for i in range(bit_to_flip):
        salted_input = (item, i)
        # a hash for the position of a bit
        bit_hash = abs(hash(salted_input)) # a big number, ensure its also positive for indexing
        # ensure > bit size wraps around via mod
        bit_index = bit_hash % num_bits
        positions.append(bit_index)
    return positions

def add_to_bloom(item: str):
    bit_positions = get_bit_positions(item, bits_to_flip)
    for bit_index in bit_positions:
        # get the byte containing our bit
        byte_index = bit_index // 8
        # bit index within a byte (offset)
        bit_offset = bit_index % 8

        # new bit as a byte
        mask = 1 << bit_offset # give something like 00001000
        # adds the new bit to the existing byte
        bit_array[byte_index] |= mask

def contains_key(item: str) -> bool:
    bit_positions = get_bit_positions(item, bits_to_flip)
    for bit_index in bit_positions:
        byte_index = bit_index // 8
        bit_offset = bit_index % 8

        # check byte to make sure the expected bit for this item is flipped
        if (bit_array[byte_index] & (1 << bit_offset)) == 0:
            return False
    return True

num_tests = int(input())
for _ in range(num_tests):
    add_to_bloom(input())
num_tests = int(input())
matches = 0
for _ in range(num_tests):
    if contains_key(input()):
        matches += 1
print(matches)