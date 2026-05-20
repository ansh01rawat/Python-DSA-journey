#WAF to find factorial of a number through recursion
def fact(n):
    if n == 0 or n == 1:
       return 1
    else:
        return n * fact(n-1)

print(fact(5))