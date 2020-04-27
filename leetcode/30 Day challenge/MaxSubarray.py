class Solution:
    def maxSubArray(self, nums):
        sum = nums[0]
        max_sum = nums[0]
        # print('input ',nums[0],'sum ',sum)
        for i in range(1,len(nums)):
            sum += nums[i]
            if(nums[i]>sum):
                sum=nums[i]
            if(sum > max_sum):
                max_sum = sum
                # print('input ',nums[i],'sum ',sum)
                continue
            if(sum < 0 and max_sum>0):
                sum= max(0,nums[i])
                # print('input ',nums[i],'sum ',sum)
                continue
            sum= max(sum,nums[i])
            # print('input ',nums[i],'sum ',sum)
        return max_sum
