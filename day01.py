from run import single


@single
def part1(line):
    final_sum = 0
    for i, digit in enumerate(line):
        if i > len(line):
            continue
        previous_digit = line[i - 1]
        if previous_digit == digit:
            final_sum += int(digit)
    return final_sum


@single
def part2(line):
    final_sum = 0
    half_len = int(len(line) / 2)
    for i, digit in enumerate(line):
        halfway_around_digit = line[(i + half_len) % len(line)]
        if halfway_around_digit == digit:
            final_sum += int(digit)
    return final_sum
