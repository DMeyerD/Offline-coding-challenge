
string = "Python"
def reverse_string(string):
    reverse = ""
    char =""
    for i in string:
        reverse = i + reverse
    return reverse
print(reverse_string(string)) # returns "nohtyP"
