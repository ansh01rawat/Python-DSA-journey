#menu function

def check_prime(n):
    if n == 2 or n== 3 or n== 5 or n== 7:
        return True
    elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    else:
        return True

def find_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * find_factorial(n-1)

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print("1 -> Check Prime")
print("2 -> Find factorial")
print("3 -> Fibonacci")
print("4 -> exit")
print("the number should be between 1 and 4 ")
m = int(input("enter the desired function number: "))

if m == 1:
    n = int(input("enter the number: "))
    print(check_prime(n))
elif m == 2:
    n = int(input("enter the number: "))
    print(find_factorial(n))
elif m == 3:
    n = int(input("enter the number: "))
    print(fib(n))
elif m == 4:
    print("exit")



