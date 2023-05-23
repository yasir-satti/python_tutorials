# Create a function that takes a string as an argument and returns a 
# coded (h4ck3r 5p34k) version of the string.
#
# Example: hacker_speak("anddigital is cool") ➞ "4ndd1g1t4l 15 c00l"
#
# In order to work properly, the function should replace all "a"s with 4, "e"s with 3, "i"s with 1, "o"s with 0, and "s"s with 5.

def string_coder(string):
    if type(string) == str:
        if string != '':
            string = (string.lower()).replace('a', '4')
            string = (string.lower()).replace('e', '3')
            string = (string.lower()).replace('i', '1')
            string = (string.lower()).replace('o', '0')
            string = (string.lower()).replace('s', '5')
        else:
            string = 'You typed empty string!'
    else:
        string = 'Input is not a string!'
    return string

result = string_coder('anddigital is cool')
print(result)