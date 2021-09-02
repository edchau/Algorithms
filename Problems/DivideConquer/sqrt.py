"""
Find sqrt of integers
Binary Search
"""
def square_root(num):
    return binary_search(num, 0, num)


def binary_search(n, left, right):
    if left >= right:
        return -1

    mid = (left + right) // 2
    square = mid * mid

    if square == n:
        return mid
    elif square > n:
        return binary_search(n, left, mid)
    elif square < n:
        return binary_search(n, mid, right)
    
print(square_root(16))
print(square_root(25))


def square_root_decimal(num):
    for i in range(num):
        square = i * i
        if square == num:
            return i
        elif square > num:
            return binary_search_dec(num, i-1, i)
    return -1

def binary_search_dec(n, left, right):
    if left >= right:
        return -1

    mid = (left + right) / 2
    square = mid * mid

    if square == n or abs(n-square) < .00001:
        return mid
    elif square > n:
        return binary_search_dec(n, left, mid)
    elif square < n:
        return binary_search_dec(n, mid, right)

    
print(square_root_decimal(16))
print(square_root_decimal(17))