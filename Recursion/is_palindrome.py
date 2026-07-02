def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return True
    return is_palindrome(s[1:-1])
text = input("enter a string: ")
if is_palindrome(text):
    print("palindrome")
else:
    print("not a palindrome")
