__author__ = 'mohan'

'''
Create a function named divisors that takes an integer and returns an array with all of the integer's divisors(except for 1 and the number itself). If the number is prime return the string '(integer) is prime' (use Either String a in Haskell).

Example:

divisors(12); #should return [2,3,4,6]
divisors(25); #should return [5]
divisors(13); #should return "13 is prime"
You can assume that you will only get positive integers as inputs.
'''

def divisors(integer):
    divisor_list = [i for i in range(2, integer+1/2) if integer%i == 0]
    return divisor_list if divisor_list else "%s is prime" % integer


# Sol 1:
def divisors_2(n):
    return [i for i in xrange(2, n) if not n % i] or '%d is prime' % n


# Rating:  249


# Sol 2:
def divisors_1(num):
    l = [a for a in range(2, num) if num % a == 0]
    if len(l) == 0:
        return str(num) + " is prime"
    return l


# Rating:  166



# Sol 4:
def divisors_4(n):
    import math
    o = [i for i in range(2, int(math.ceil(n / 2) + 1)) if n % i == 0]
    return o if len(o) > 0 else "%d is prime" % n


# Rating:  15


# Sol 5:
def divisors_11(integer):
    return [n for n in range(2, integer) if integer % n == 0] or '{} is prime'.format(integer)


# Rating:  12


# Sol 6:
def divisors_3(integer):
    a = []
    for i in range(2, integer):
        if integer % i == 0:
            a.append(i)
    return a if a else str(integer) + " is prime"


# Rating:  10


# Sol 7:
def divisors_5(n):
    result = [i for i in range(2, n) if n % i == 0]
    return result if result else str(n) + ' is prime'


# Rating:  6


# Sol 8:
def divisors_6(n):
    divs = set()

    for t in range(2, int(n ** 0.5) + 1):
        div, mod = divmod(n, t)

        if mod == 0:
            divs.add(t)
            divs.add(div)

    return '{:d} is prime'.format(n) if len(divs) == 0 else sorted(list(divs))


# Rating:  5


# Sol 9:
def divisors_10(integer):
    divs = [i for i in range(2, integer) if integer % i == 0]

    if not divs:
        return '%d is prime' % integer
    else:
        return divs


# Rating:  4


# Sol 10:
def divisors_7(integer):
    divisors = filter(lambda x: integer % x == 0, range(2, integer // 2 + 1))
    return divisors if divisors else "{0} is prime".format(integer)


# Rating:  3


# Sol 11:
def divisors_8(integer):
    import math
    divisors = []
    for pos_div in range(2, int(math.floor(integer / 2)) + 1):
        if integer % pos_div == 0:
            divisors.append(pos_div)
    if len(divisors) == 0:
        return str(integer) + " is prime"
    return divisors


# Rating:  3



# Sol 13:
def divisors_12(n):
    return [i for i in range(2, int((n / 2)) + 1) if not n % i] or '{} is prime'.format(n)


# Rating:  2


# Sol 14:
def divisors_17(i):
    y = [x for x in range(2, i / 2 + 1) if i % x == 0]
    return y if y else "{} is prime".format(i)


# Rating:  2


# Sol 15:
def divisors_13(integer):
    lst = [x for x in range(2, integer) if integer % x == 0]
    if len(lst) == 0:
        return str(integer) + ' is prime'
    return lst


# Rating:  1


# Sol 16:
def divisors_14(integer):
    divisors = [divisor for divisor in xrange(2, integer) if integer % divisor == 0]
    return divisors if len(divisors) > 1 else '%d is prime' % integer


# Rating:  1


# Sol 17:
def divisors_15(integer):
    # It can save half the memory, for only need to test half
    results = [divisor for divisor in range(2, integer) if integer % divisor == 0]
    return results if results else str(integer) + " is prime"


# Rating:  1


# Sol 18:
def divisors_18(integer):
    result = [x for x in range(2, integer - 1) if integer % x == 0]
    return '{0} is prime'.format(integer) if len(result) == 0 else result


# Rating:  1


# Sol 19:
def divisors_19(integer):
    c = [i for i in range(2, integer) if integer % i == 0]
    if (len(c) != 0):
        return c
        print (c)
    else:
        g = str(integer) + " is prime"
        return g


# Rating:  1
input = 15
print divisors(input)
print divisors_1(input)
print divisors_2(input)
print divisors_3(input)
print divisors_4(input)
print divisors_5(input)
print divisors_6(input)
print divisors_7(input)
print divisors_8(input)
print divisors_10(input)
print divisors_11(input)
print divisors_12(input)
print divisors_13(input)
print divisors_14(input)
print divisors_15(input)
print divisors_17(input)
print divisors_18(input)
print divisors_19(input)

