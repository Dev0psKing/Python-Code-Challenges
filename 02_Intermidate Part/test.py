
def reverse_string(string):
    return (string[::-1])

def count_vowels(string):
    count = 0
    string = string.lower()
    vowel = "aeiou"

    for char in string:
        if char in vowel:
            count += 1
    print(count)
count_vowels("Hello Code World ")


def is_palindrome(string):
    string = string.replace(" ", "").lower()
    backward_string = reverse_string(string)
    
    if string == backward_string:
        print("Its a Palindrome")
    else:
        print("Not a Palindrom")
is_palindrome("MaM ")

