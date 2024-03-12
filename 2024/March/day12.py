import numpy as np

class Solution:
    def genFibNum(self, a, b, c, n, m):
        # code here 
        if n<=2:
            return 1
        res = np.array([
            [1,0,0],
            [0,1,0],
            [0,0,1]
        ])
        gen_fib_matrix = np.array([
            [a, b, c],
            [1, 0, 0],
            [0, 0, 1]
        ])
        
        n -= 2
        while n:
            if n & 1:
                res = np.matmul(res,gen_fib_matrix)%m
            gen_fib_matrix = np.matmul(gen_fib_matrix, gen_fib_matrix) % m
            n >>= 1
        return sum(res[0]) % m
