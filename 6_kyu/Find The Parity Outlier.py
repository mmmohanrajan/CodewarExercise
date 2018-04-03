__author__ = 'mohan'

'''
You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160
'''

def find_outlier(integers):
    even = True if len(filter(lambda x: x % 2 == 0, integers[:3])) >= 2 else False
    for i in integers:
        if even and not i % 2 == 0:
            return i
        if not even and i % 2 == 0:
            return i

## other solution

# def find_outlier(int):
#     odds = [x for x in int if x%2!=0]
#     evens= [x for x in int if x%2==0]
#     return odds[0] if len(odds)<len(evens) else evens[0]

# def find_outlier(integers):
#     parity = [n % 2 for n in integers]
#     return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

# def find_outlier(integers):
#     odd = filter(lambda x: x % 2 == 1, integers)
#     even = filter(lambda x: x % 2 == 0, integers)
#     return odd[0] if len(odd) == 1 else even[0]

find_outlier([1,2,1])