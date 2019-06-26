class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        if m==0:
            if n%2==0:
                return ((nums2[n//2]+nums2[n//2-1])/2.0)
            else:
                return (nums2[n//2])/1.0
        elif n==0:
            if m%2==0:
                return ((nums1[m//2]+nums1[m//2-1])/2.0)
            else:
                return (nums1[m//2])/1.0
        else:
            nums=sorted(list(nums1+nums2))
            numsLen=len(nums)
            if numsLen%2==0:
                return (nums[numsLen//2]+nums[numsLen//2-1])/2.0
            else:
                return (nums[numsLen//2])/1.0