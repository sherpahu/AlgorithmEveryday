class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rst=[]
        #双指针，k<i<j
        nums.sort()
        for k in range(len(nums)-3+1):
            if nums[k]>0:
                break
                #k最小，nums[k]>0则不可能得到和为0，提前剪枝
            if k>0 and nums[k]==nums[k-1]:
                continue
                #避免重复
            i,j=k+1,len(nums)-1#对撞指针
            while i<j:
                s=nums[k]+nums[i]+nums[j]
                #print(s)
                if s>0:
                    j-=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                elif s<0:
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
                else:
                    rst.append([nums[k],nums[i],nums[j]])
                    j-=1
                    while i<j and nums[j]==nums[j+1]:
                        j-=1
                    i+=1
                    while i<j and nums[i]==nums[i-1]:
                        i+=1
        return rst