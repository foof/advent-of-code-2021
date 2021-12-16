
version_sum = 0


def parse_next_packet(bits):
    global version_sum
    version = bits[0:3]
    type = bits[3:6]
    version_sum += int(version, 2)
    version = int(version, 2)
    type = int(type, 2)

    if type == 4:
        literal = ""
        offset = 6
        while True:
            is_last = int(bits[offset:offset+1]) == 0
            val = bits[offset+1:offset+5]
            literal += val
            offset += 5
            if is_last:
                break
        L = offset
    else:
        I = int(bits[6:7])
        if I:
            num_subpackets = int(bits[7:18], 2)
            L = 18
            for _ in range(num_subpackets):
                _, new_L = parse_next_packet(bits[L:])
                L += new_L
        else:
            subpacket_length = int(bits[7:22], 2)
            L = 22 + subpacket_length
            sub_bits = bits[22:L]
            while len(sub_bits):
                sub_bits, _ = parse_next_packet(sub_bits)

    return bits[L:], L


def solve(line):
    bin_length = len(line)*4
    spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=bin_length, type='b')
    hex = int(line, 16)
    bits = format(hex, spec)

    while len(bits) > 7:
        bits, L = parse_next_packet(bits)

    return version_sum


if __name__ == "__main__":
    with open('./input', 'r') as f:
        line = f.read().strip()
        print(solve(line))
