class Solution:
    def climbStairs(self, n: int) -> int:
        soln=[0 for i in range(n+2)]
        soln[1]= 1
        soln[2]= 2  
        for i in range(3,n+1):
            soln[i]=soln[i-1]+soln[i-2]
        return soln[n]