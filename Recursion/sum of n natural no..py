#WARF to find the sum of first n natural numbers
def _sum_(n):
    if n == 0:
       return 0
    else:
        return n + _sum_(n-1)

print(_sum_(5))