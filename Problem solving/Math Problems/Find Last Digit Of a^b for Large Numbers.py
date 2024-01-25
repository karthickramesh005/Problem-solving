# Find Last Digit Of a^b for Large Numbers :
import math
def lastdigit(a,b):
    A = int(a)
    B = int(b)
    ans = pow(A,B,10)
    return ans
    

a,b = map(str,input().split())
ans = lastdigit(a,b)
print(ans)
