class Solution:
    def climbStairs(self, n: int) -> int:
        m = n -1
        if n == 0 : 
            return 0
        elif n == 1 : 
            return 1
        else :
            phi =  (1 + sqrt(5))/2
            phi_ = (1 - sqrt(5))/2
            Fibo_n = round(1/sqrt(5) * (phi**n - phi_**n))
            Fibo_m = round(1/sqrt(5) * (phi**m - phi_**m))
            return Fibo_n + Fibo_m
        
        