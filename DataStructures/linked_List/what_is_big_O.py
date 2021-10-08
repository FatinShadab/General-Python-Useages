'''
I) What is Big O ???
    Big O notation describes the complexity of your code using algebraic terms.

    Big O notation is used to measure how running time or 
    space requirements for your program grows as input size grows.
    
_______________________

II) Relation between time and size ?(time complexity)
    the Relation between run-time and input-size is Linear.
*** equation --> time = a*n + b 

            | /
      time  |/
            |_________
              size(n)

The fastest grownig term of the equation(time= a*n + b) is
*** (time = a*n) *** and a & b is a consonant. If we remove 
the coefficients we will get *** {time = O(n)} ***

________________________

III) Big O in Binarysearch ??
    if iteration is 'k'
    and array size is 'n'

    So, 
        k = n/2^k

    if n = 1 then,
      or,  1 = n/2^k
      or,  n = 2^k
      or,  log[2]n = log[2]2^k
      or,  log[2]n = k * log[2]2

***   So, k = log[2]n 

***   And the complexitys is O(logn)

_______________________
'''


# Ex. of Run-time = O(1) (constant time) (eq: T = c)
def Do_nothing(given_arr):
    total = 0
    return total

# Ex. of Run-time = O(n) (linear time) (eq: T = an + b)
def Sum_all(given_arr):
    total_sum = 0
    for i in given_arr:
        total_sum += 1
    return total_sum

# Ex. of Run-time = O(n^2) (quadratic time) (eq: T = an^2 + bn + c)
def dind_sum_2d(array_2d):
    total = 0
    for row in array_2d:
        for ele in row:
            total += ele
    return total