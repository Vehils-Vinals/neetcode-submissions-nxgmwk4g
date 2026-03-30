class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n==1:
            return 1
        minusone = 1
        minustwo = 1
        ini = 0
        for i in range(2, n+1):
            ini = minusone + minustwo
            minustwo = minusone
            minusone = ini
            print(minustwo,minusone, ini)
        return ini