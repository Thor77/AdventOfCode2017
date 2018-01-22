def part1(instructions):
    instructions = list(map(int, instructions))
    steps = 0
    index = 0
    while index < len(instructions):
        current_step = instructions[index]
        # increase step at current index
        instructions[index] += 1
        # jump to next step
        index += current_step
        steps += 1
    return steps


def part2(instructions):
    instructions = list(map(int, instructions))
    steps = 0
    index = 0
    while index < len(instructions):
        current_step = instructions[index]
        if current_step >= 3:
            # decrease current step
            instructions[index] -= 1
        else:
            # increase current step
            instructions[index] += 1
        # jump to next step
        index += current_step
        steps += 1
    return steps
