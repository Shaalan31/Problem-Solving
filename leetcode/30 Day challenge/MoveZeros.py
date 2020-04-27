class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i=0
        count=0
        while(count!=len(nums)):
            count +=1
            if nums[i] == 0:
                del nums[i]
                nums.append(0)
                i-=1
            i+=1
