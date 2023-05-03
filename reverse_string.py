# Write a Python program to reverse a given string.
# The program should print the reversed string.

def rev_string(text):
    
    text_rev = ''

    for character in text:
        # appending character in reverse order
        text_rev = character + text_rev
        # testing process
        # print(text_rev)

    return text_rev

# calling rev_string function passing input value
print(rev_string(text = raw_input("Enter a string: ")))
