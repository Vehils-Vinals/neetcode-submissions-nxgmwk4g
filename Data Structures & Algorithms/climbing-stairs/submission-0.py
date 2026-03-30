class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1 or n==0:
            return 1
        total = [1]*(n+1)
        for i in range(2, n+1):
            total[i] = total[i-1] + total[i-2]
        return total[-1]