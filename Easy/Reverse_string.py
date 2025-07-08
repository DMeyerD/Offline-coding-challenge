
string = "Python"
def reverse_string(string):
    reverse = ""
    for i in string:
        reverse = i + reverse
    return reverse
print(reverse_string(string)) # returns "nohtyP"
