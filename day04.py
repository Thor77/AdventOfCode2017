from collections import Counter


def part1(lines):
    valid_passphrases = 0
    for line in lines:
        line_split = line.split()
        if len(line_split) == len(set(line_split)):
            valid_passphrases += 1
    return valid_passphrases


def part2(lines):
    valid_passphrases = 0
    for line in lines:
        line_split = line.split()
        if len(line_split) == len(set(line_split)):
            non_duplicate_words = []
            [
                non_duplicate_words.append(word_set)
                for word_set in map(Counter, line_split)
                if word_set not in non_duplicate_words
            ]
            if len(non_duplicate_words) == len(line_split):
                valid_passphrases += 1
    return valid_passphrases
