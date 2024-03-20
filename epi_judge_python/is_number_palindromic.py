from test_framework import generic_test

# Get the rightmost number: % 10
# Get the leftmost number: % (the place of the digit in the rightmost spot)
# Remove the rightmost number after comparison: / 10
# Remove the leftmost number after comparison: % (the place of the digit in the rightmost spot)
def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False
    div = 1
    while x >= 10 * div:
        div *= 10
    # Could also be found the following way but I don't find this intuitive (I haven't mathed in a while)
    # div = 10**int(math.log10(x))

    while x:
        right = x % 10
        left = x // div

        if left != right: return False

        # remove both digits used in comparison
        x = (x % div) // 10
        div = div / 100
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
