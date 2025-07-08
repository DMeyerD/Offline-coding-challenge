#Write a function that checks whether a given string is a palindrome. 
# A palindrome is a word or phrase that reads the same forwards and backwards — ignoring case and spaces.

x = "nurses run"
def is_palindrome(x):
    y = ""
    x = str.lower(x)
    x = str.replace(x , " ", "")
    for i in x:
        y = i + y
    if y == x:
        print(y)
        print("True")
    else:
        print(y)
        print("False")
is_palindrome(x)

# This one wasn’t too bad, but you can see that I misunderstood how to use the str methods.
# I now understand that I should call them on the string itself — for example, x.lower() instead of str.lower(x).