
def handle_value(type, value, new_value):
    if value is None:
        value = new_value
    elif type == 0:
        value += new_value
    elif type == 1:
        value *= new_value
    elif type == 2:
        value = min(value, new_value)
    elif type == 3:
        value = max(value, new_value)
    elif type == 5:
        if value > new_value:
            value = 1
        else:
            value = 0
    elif type == 6:
        if value < new_value:
            value = 1
        else:
            value = 0
    elif type == 7:
        if value == new_value:
            value = 1
        else:
            value = 0

    return value


def parse_next_packet(bits):
    version = bits[0:3]
    type = bits[3:6]
    version = int(version, 2)
    type = int(type, 2)
    value = None

    if type == 4:
        literal = ""
        offset = 6
        while True:
            is_last = int(bits[offset:offset+1]) == 0
            val = bits[offset+1:offset+5]
            literal += val
            offset += 5
            if is_last:
                value = int(literal, 2)
                break
        L = offset
    else:
        I = int(bits[6:7])
        if I:
            num_subpackets = int(bits[7:18], 2)
            L = 18
            for _ in range(num_subpackets):
                _, new_L, v = parse_next_packet(bits[L:])
                value = handle_value(type, value, v)
                L += new_L
        else:
            subpacket_length = int(bits[7:22], 2)
            L = 22 + subpacket_length
            sub_bits = bits[22:L]
            while len(sub_bits):
                sub_bits, _, v = parse_next_packet(sub_bits)
                value = handle_value(type, value, v)

    return bits[L:], L, value


def solve(line):
    bin_length = len(line)*4
    spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=bin_length, type='b')
    hex = int(line, 16)
    bits = format(hex, spec)
    val = None

    while len(bits) > 7:
        bits, L, val = parse_next_packet(bits)

    return val


if __name__ == "__main__":
    with open('./input', 'r') as f:
        line = f.read().strip()
        print(solve(line))
