def palindromeOrNot(string):
    palindrome = string[::-1]

    print(palindrome)
    if palindrome in string:
        return True
    else:
        return False

string = "radar"
is_palindrome = palindromeOrNot(string)
print(is_palindrome)


