# Missing Number
def missingNumber( nums,l):
        """
        :type nums: List[int]
        :rtype: int
        """
     
        e = l * (l + 1) // 2
        a = sum(nums)
        return e - a

arr = list(map(int,input().split()))
n = len(arr)
print(missingNumber(arr, n))
