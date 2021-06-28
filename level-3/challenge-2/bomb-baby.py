# Find the number of bomb replication cycles needed for the correct amount of bombs
def solution(x, y):
    x, y = int(x), int(y)
    cycles = 0

    while (x != 1 and y != 1):
        if x % y == 0:
            return "impossible"
        else :
            cycles = cycles + int(max(x, y) / min(x, y))
            x, y = max(x, y) % min(x, y), min(x, y)

    return str(cycles + max(x, y) - 1)

# Test function
def main():
    print(solution('4', '7'))

# Run test
main()