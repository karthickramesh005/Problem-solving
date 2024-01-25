# Majority Element
from collections import Counter 
def majorityElement(nums):
        count = Counter(nums)
        return max(count.keys(),key = count.get)


arr = list(map(int,input("Enter  a array element  : ").split()))
print("Majority elements : ",majorityElement(arr))
