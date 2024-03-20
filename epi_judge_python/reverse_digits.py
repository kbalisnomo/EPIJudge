from test_framework import generic_test

# To extract the 1's digit % 10
# Shift other digits to right by doing: // 10
# Shift result to left by doing: * 10
def reverse(x: int) -> int:
    result, x_remainder = 0, abs(x)
    while x_remainder:
        result = result * 10 + x_remainder % 10
        x_remainder //= 10
    return -result if x < 0 else result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
