from itertools import permutations


def part1(lines):
    return sum(
        map(
            lambda l: max(l) - min(l),
            map(lambda l: list(map(int, l.split())), lines)
        )
    )


def part2(lines):
    final_sum = 0
    for line in map(lambda l: list(map(int, l.split())), lines):
        for digit1, digit2 in permutations(line, 2):
            if digit1 % digit2 == 0:
                final_sum += digit1 / digit2
    return int(final_sum)
