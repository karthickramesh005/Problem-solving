# Palindrome
def Palidrome(n):
    s = str(n)
    a = s[::-1]
    if int(a) == n :
        return "Yes"
    else :
        return "No"

n = int(input("Enter a number : "))
print(Palidrome(n))
