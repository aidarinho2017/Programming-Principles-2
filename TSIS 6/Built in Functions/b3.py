def palindrome(s):
    a = s[::-1]
    if s == a:
        return True
    return False
print(palindrome("abcba"))
print(palindrome("that's me"))