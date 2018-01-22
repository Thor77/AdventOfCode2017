from run import single


def parse_banks(banks_input):
    return list(map(lambda bi: int(bi), banks_input.strip().split()))


@single
def part1(banks_input):
    banks = parse_banks(banks_input)
    previous_states = [banks.copy()]
    steps = 0
    while True:
        banks_max = max(banks)
        index_of_next_max = banks.index(banks_max)
        # set bank with max value to zero
        banks[index_of_next_max] = 0
        # distribute blocks from max bank across all banks
        for i in range(1, banks_max + 1):
            banks[(index_of_next_max + i) % len(banks)] += 1
        steps += 1
        if banks in previous_states:
            break
        else:
            previous_states.append(banks.copy())
    return steps


@single
def part2(banks_input):
    banks = parse_banks(banks_input)
    previous_states = [banks.copy()]
    cycles = 0
    found = False
    while True:
        banks_max = max(banks)
        index_of_next_max = banks.index(banks_max)
        # set bank with max value to zero
        banks[index_of_next_max] = 0
        # distribute blocks from max bank across all banks
        for i in range(1, banks_max + 1):
            banks[(index_of_next_max + i) % len(banks)] += 1
        cycles += 1
        if banks in previous_states:
            if found:
                break
            # found banks-setup causing loop
            found = True
            previous_states = []
            cycles = -1
        else:
            previous_states.append(banks.copy())
    return cycles
