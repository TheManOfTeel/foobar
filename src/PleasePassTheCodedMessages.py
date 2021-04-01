from itertools import combinations


# Find largest number divisible by 3
def solution(l):
    l.sort(reverse=True)
    for i in reversed(range(1, len(l) + 1)):
        for tup in combinations(l, i):
            if sum(tup) % 3 == 0:
                return int(''.join(map(str, tup)))
    return 0


# Test function
def main():
    print(solution([3, 1, 4, 1, 5, 9]))


# Run test
main()
