# Solution utilzing cellular automata theory to determine the amount of previous states possible after 1 time step
def solution(g):
    zipped = tuple(zip(*g))
    pre_imgs = get_pre_images(zipped[0])
    pre_count = dict()
    for img in pre_imgs:
        pre_count[img[0]] = 1
    for col in zipped:
        pre_imgs = get_pre_images(col)
        count = dict()
        for img in pre_imgs:
            if img[0] not in pre_count: pre_count[img[0]] = 0
            if img[1] not in count: count[img[1]] = 0
            count[img[1]] += pre_count[img[0]]
        pre_count = count
    return sum(pre_count.values())

def get_pre_images(col):
    options = ((0, 0), (0, 1), (1, 0), (1, 1))
    # Apply rules of devolving to get current
    curr_col = devolve[col[0]]
    # Generate map
    for i in range(1, len(col)):
        new = []
        for elem in curr_col:
            for option in options:
                # Apply the rules of evolution
                if evolve[(elem[i], option)] == col[i]:
                    new.append(elem + (option,))
        curr_col = tuple(new)
    body = [tuple(zip(*i)) for i in curr_col]
    return [tuple([get_bit(t) for t in tuples]) for tuples in body]

def get_bit(bits):
    return_bit = 0
    for bit in bits:
        return_bit = (return_bit << 1) | bit
    return return_bit

# Rules of evolution
evolve = {
        ((0, 0), (0, 0)): 0,
        ((0, 0), (0, 1)): 1,
        ((0, 0), (1, 0)): 1,
        ((0, 0), (1, 1)): 0,
        ((0, 1), (0, 0)): 1,
        ((0, 1), (0, 1)): 0,
        ((0, 1), (1, 0)): 0,
        ((0, 1), (1, 1)): 0,
        ((1, 0), (0, 0)): 1,
        ((1, 0), (0, 1)): 0,
        ((1, 0), (1, 0)): 0,
        ((1, 0), (1, 1)): 0,
        ((1, 1), (0, 0)): 0,
        ((1, 1), (0, 1)): 0,
        ((1, 1), (1, 0)): 0,
        ((1, 1), (1, 1)): 0
        }

# Rules of devolving
devolve = {
        0: (((0, 0),(0, 0)),
            ((0, 0), (1, 1)),
            ((0, 1), (0, 1)),
            ((0, 1), (1, 0)),
            ((0, 1), (1, 1)),
            ((1, 0), (0, 1)),
            ((1, 0), (1, 0)),
            ((1, 0), (1, 1)),
            ((1, 1), (0, 0)),
            ((1, 1), (0, 1)),
            ((1, 1), (1, 0)),
            ((1, 1), (1, 1))),
        1: (((1, 0), (0, 0)),
            ((0, 1), (0, 0)),
            ((0, 0), (1, 0)),
            ((0, 0), (0, 1)))}

# Test function
def main():
    print(solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]))

# Run test
main()
