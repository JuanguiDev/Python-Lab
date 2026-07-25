'''
Write a program that prints the first 50 numbers of the Fibonacci sequence,
starting at 0.

The Fibonacci sequence is made up of numbers where each number is always
the sum of the two previous numbers.

0, 1, 1, 2, 3, 5, 8, 13...
'''

def fibonacci(n):
  a, b = 0, 1
  for i in range(0,n+1):
    print(a)
    c = a + b
    a = b
    b = c
    
fibonacci(50)