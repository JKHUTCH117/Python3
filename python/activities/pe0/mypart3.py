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


  1 #!/usr/bin/env python3
  2 
  3 def guess_number(n):
  4 
  5 
  6     while True:
  7         u = int(input('Guess a number between 0-100 '))
  8         if u == n:
  9            print('WIN')
 10            break
 11         elif u < n:
 12             print('too low')
 13         elif u > n:
 14             print('too high')
 15 
 16 
 17 guess_number(23)
