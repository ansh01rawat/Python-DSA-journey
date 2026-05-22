class Solution:
    def isHappy(self, n: int) -> bool:
        hashset = set()
        while n not in hashset:
            hashset.add(n)
            n = self.sumofsquares(n)
            if n == 1:
                return True
        return False
    def sumofsquares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            output += digit ** 2
            n = n//10
        return output