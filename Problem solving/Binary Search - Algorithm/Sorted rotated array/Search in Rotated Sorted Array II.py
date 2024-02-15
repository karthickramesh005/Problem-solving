# Search in Rotated Sorted Array II

def search(arr, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        n = len(arr)
        for i in range(n):
            if arr[i] == arr[target] :
                return True
            else :
                return False

arr = list(map(int,input("Enter a array values : ").split()))
x = int(input("Enter : "))
print(search(arr, target))
