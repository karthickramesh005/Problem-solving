# GCD of two numbers :

def gcd(a,b):
    while b :
        a,b = b,a % b
    return a

a = int(input("Enter a first value : "))
b = int(input("Enter a second value : "))
p = gcd(a,b)
print(p)
