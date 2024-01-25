# Armstrong Numbers :
def Armstrong(n):
    s = str(n)
    m = len(s)
    ams = sum(int(i)**m  for i in s)
    if ams == n :
        return True
    else :
        return False


n = int(input())
print(Armstrong(n)) 
