class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        front=0
        tail=0
        while tail<len(nums):
            nums[front]=nums[tail]
            while tail<len(nums) and nums[tail]==nums[front]:
                tail+=1
            front+=1
        return front