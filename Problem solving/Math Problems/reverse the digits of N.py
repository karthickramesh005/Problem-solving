# Given N,  reverse the digits of N. :
def reverse(n):
    r = str(n)
    R = r[::-1]
    N = int(R)
    return N


n = int(input())
ans = reverse(n)
print(ans)
