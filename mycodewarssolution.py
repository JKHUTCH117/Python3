8 kyu
Multiply
Python:
def multiply(a, b):
    return a * b
1 minute agoRefactor
def multiply(a, b):
    return    a * b
7 days agoRefactor
7 kyu
String ends with?
Python:
def solution(string, ending):
        return string.endswith(ending)
21 minutes agoRefactorDiscuss
8 kyu
Can we divide it?
Python:
def is_divide_by(number, a, b):
    if number % a == 0 and number % b == 0:
        return True
    else:
        return False
    
    return 
4 hours agoRefactorDiscuss
7 kyu
Is this a triangle?
Python:
def is_triangle(a, b, c):
    
    if (a + b > c) and (b + c > a) and (c + a > b):
        return True
    else:
        return False
16 hours agoRefactorDiscuss
8 kyu
Invert values
Python:
def invert(lst):
    return [(-i) for i in lst]
3 days agoRefactorDiscuss
6 kyu
Break camelCase
Python:
def solution(s):
    a=""
    for letter in s:
        if ord(letter) in range(65,91):
            a+=" "
        a+=letter
    return a
6 days agoRefactorDiscuss
8 kyu
You only need one - Beginner
Python:
def check(seq, elem):
    
    if elem in seq: 
        return True
    else:
        return False
6 days agoRefactorDiscuss
8 kyu
Find Maximum and Minimum Values of a List
Python:
def minimum(arr):
    return min(arr)
    

def maximum(arr):
    return max(arr)
    
6 days agoRefactorDiscuss
8 kyu
A Needle in the Haystack
Python:
def find_needle(haystack):
    index = haystack.index('needle')
    if index >= 0:
        x =  "found the needle at position " + str(index)
    return x
6 days agoRefactorDiscuss
8 kyu
Sum Arrays
Python:
def sum_array(a):
    total = sum(a)
    if total == 0:
        return 0
    else:
        return total
    
    
    
6 days agoRefactorDiscuss
8 kyu
Is he gonna survive?
Python:
def hero(bullets, dragons):
    if bullets >= dragons * 2:
        return True
    else:
        return False
6 days agoRefactorDiscuss
8 kyu
Calculate average
Python:
def find_average(numbers):
    avg = sum(numbers) / len(numbers)
    return avg
6 days agoRefactorDiscuss
8 kyu
Opposite number
Python:
def opposite(number):
    return -number
6 days agoRefactorDiscuss
8 kyu
Find the smallest integer in the array
Python:
def find_smallest_int(arr):
    return min(arr)
6 days agoRefactorDiscuss
8 kyu
Convert a Boolean to a String
Python:
def boolean_to_string(b):
    return str(b)
6 days agoRefactorDiscuss
7 kyu
Two to One
Python:
def longest(a1, a2):
    a1 = list(a1)
    a2 = list(a2)
    a3 = a1 + a2
    print(a3)
    a3 = sorted(a3)
    print(a3)
    a3 = ''.join(a3)
    print(a3)
    a3 = set(a3)
    print(a3)
    a3 = list(a3)
    print(a3)
    a3 = sorted(a3)
    a3 = ''.join(a3)
    print(a3)
    
    return a3
