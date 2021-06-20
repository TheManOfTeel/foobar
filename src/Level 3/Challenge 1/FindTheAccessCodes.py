# Find the number of luckky triples in the list
def solution(l):
    c = [0] * len(l)
    count = 0
    for i in range(0,len(l)):
        j = 0
        for j in range(0, i):
            if l[i] % l[j] == 0:
                c[i] = c[i] + 1
                count = count + c[j]
    return count

# Test function
def main():
    print(solution([1, 2, 3, 4, 5, 6]))

# Run test
main()