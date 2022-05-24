  1 *Practical Exercise 0-2*
  2 
  3 ---
  4 
  5 FizzBuzz is an interview question that is said to filter out 99.5% of programming job candid    ates.
  6 
  7 ---
  8 
  9 *Deliverable*
 10 
 11 Modify deliverable.py so that it takes a number from the user and prints it (the number) if     it isn't divisible by 3 or 5. For multiples of 3 print 'fizz' instead. For multiples of 5 pr    int 'buzz' instead. For multiples of 3 and 5 print 'fizzbuzz'.
 12 
 13 ---
 14 
 15 .deliverable.py
 16 ----
 17 include::deliverable.py[]
 18 ----
 19 
 20 ---
 21 
 22 *END*
~                
  '''
  FAILED
  #!/usr/bin/env python3
  2 
  3 x = input('Enter number: ')
  4 
  5 print(x)
  6 
  7 a = x % 3
  8 b = x % 5
  9 
 10 print(a)
 11 print(b)
 12 
 13 if a == b:
 14     print('fizzbuzz')
 15 elif a <= 0:
 16     print('fizz')
 17 elif b <= 0:
 18     print('buzz')
 19     
 20 else:
 21     pass
 22 
 23 if a <= 0:
 24     print('fizz')
 25 
 26 if b <= 0:
 27     print('buzz')
 28
 PASSED
 '''
 1 #!/usr/bin/env python3
  2 
  3 x = int(input('Enter number: '))
  4 '''
  5 print(x)
  6 a = x % 3
  7 b = x % 5
  8 print(a)
  9 print(b)
 10 '''
 11 if x%3 == 0 and x%5 == 0:
 12     print('fizzbuzz')
 13 elif x%3 <= 0:
 14     print('fizz')
 15 elif x%5 <= 0:
 16     print('buzz')
 17     
 18 else:
 19     print(x)
 20     
 21 '''
 22 if a <= 0:
 23     print('fizz')
 24 
 25 if b <= 0:
 26     print('buzz')
 27 '''

 
