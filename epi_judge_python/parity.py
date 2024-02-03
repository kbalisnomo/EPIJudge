from test_framework import generic_test


def parity(x: int) -> int:
    length = 64
    while (length > 1):
        length //= 2
        x ^= x >> length
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))