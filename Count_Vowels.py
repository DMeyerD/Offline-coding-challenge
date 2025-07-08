# Write a function that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string. The function should be case-insensitive.
import array
test = "Hello World"
vowels = ['a', 'e', 'i', 'o', 'u']


def count_vowels(test):
    counted_vowels = 0
    for i in str.lower(test):
        
        if i in vowels:
            counted_vowels += 1 
    return counted_vowels
print(count_vowels(test))