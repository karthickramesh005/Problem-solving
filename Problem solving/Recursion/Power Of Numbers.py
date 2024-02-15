# Power Of Numbers
import math
def power(N,R):
        #Your code here
        #m = 10 ** 9 + 7
        k = pow(N,R)
        return k
    
N = int(input("Enter a number : "))
R = int(input("Enter a pow number : "))
result = power(N,R)
print(result)
