# Challenge: FizzBuzz Lite
# Task:
# Write a function that takes a number n and prints all numbers from 1 to n. But:
    # If the number is divisible by 3, print "Fizz" instead.
    # If the number is divisible by 5, print "Buzz" instead.
    # If the number is divisible by both, print "FizzBuzz".
    # Otherwise, just print the number itself.


n = 30

def fizzbuzz (n):
    for i in range(n-n+1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 5 == 0:
            print("buzz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)
fizzbuzz(n)

# This challenge tripped me up on the range function — I was starting at index 0.
# While I understood this, it took a deeper reading of the documentation to realize
# I can manipulate this within the range function.
# After completing this challenge, I realized I’ve overcomplicated the use of range(n - n + 1),
# but I will leave it as-is since this is the code I came up with without the help of AI or the internet.