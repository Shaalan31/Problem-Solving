class Solution:
    def countElements(self, arr: List[int]) -> int:
        arr = sorted(arr)
        sum=0
        count = 1
        value=arr[0]
        for i in range(1,len(arr)):
            if value == arr[i]:
                count+=1
                continue
            else:
                if value == arr[i]-1:
                    sum+=count
                count = 1
                value = arr[i]
        return sum