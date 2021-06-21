from fractions import Fraction
import numpy as np

# Feed the arrays in, break them down, get the probabilities as fractions
def solution(m):
    # Stop here if there is no need to process
    if len(m) < 2:
        return [1,1]

    r_submatrix, q_submatrix = split_matrix(m)
    f_submatrix = np.linalg.inv(np.subtract(np.identity(len(q_submatrix)), q_submatrix))
    fr_submatrix = np.dot(f_submatrix, r_submatrix)
    return decimal_to_fraction(fr_submatrix[0])

def split_matrix(m):
    terminal_rows = set()
    for nth_row in range(len(m)):
        if sum(m[nth_row]) == 0:
            terminal_rows.add(nth_row)
    r_submatrix = []
    q_submatrix = []
    for nth_row in range(len(m)):
        if nth_row not in terminal_rows:
            row_total = float(sum(m[nth_row]))
            r_tmp = []
            q_tmp = []
            for nth_col in range(len(m[nth_row])):
                if nth_col in terminal_rows:
                    r_tmp.append(m[nth_row][nth_col] / row_total)
                else:
                    q_tmp.append(m[nth_row][nth_col] / row_total)
            r_submatrix.append(r_tmp)
            q_submatrix.append(q_tmp)
    return r_submatrix, q_submatrix

def decimal_to_fraction(l):
    return_array = []
    denominators = []
    for num in l:
        frac = Fraction(num).limit_denominator()
        return_array.append(frac.numerator)
        denominators.append(frac.denominator)
    lcd = 1
    for denom in denominators:
        lcd = np.lcm(lcd, denom)
    for num_i in range(len(return_array)):
        return_array[num_i] *= int(lcd / denominators[num_i])
    return_array.append(lcd)
    return return_array

# Test function
def main():
    print(solution([[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]))

# Run test
main()