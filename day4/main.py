from collections import defaultdict

if __name__ == "__main__":

    test_scratchcards = ['Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
                    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
                    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
                    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
                    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
                    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11']

    with open('input.txt') as f:
        scratchcards = f.readlines()

    points = 0
    winning_instances = defaultdict(int)

    for idx, scratchcard in enumerate(scratchcards):
        winning_instances[idx] += 1
        left, right = scratchcard.split('|')

        left = left.split()[2:]
        right = right.split()
        matches = list(set(left).intersection(right))
        if matches:
            points += 2 ** (len(matches)-1)
        for key in range(len(matches)):
            winning_instances[idx+1+key] += winning_instances[idx]

    print(f'Part 1: {points}')
    print(f'Part 2: {sum(winning_instances.values())}')