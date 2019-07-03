import sys
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_sum=sys.maxsize
        nums.sort()
        for left in range(len(nums)-2):
            mid=left+1
            right=len(nums)-1
            delta=target-nums[left]
            while mid<right:
                delta_all=target-nums[left]-nums[mid]-nums[right]
                if abs(delta_all)<abs(target-min_sum):
                    min_sum=nums[left]+nums[mid]+nums[right]
                    
                if delta_all==0:
                    return nums[left]+nums[mid]+nums[right]
                elif delta_all>0:
                    mid+=1
                    while mid<right and nums[mid]==nums[mid-1]:mid+=1
                else:
                    right-=1
                    while mid<right and nums[right]==nums[right+1]:right-=1
        return min_sum
                    