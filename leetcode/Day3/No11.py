class Solution:
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        rst=0
        while i<j:
            rst=max(rst,min(height[i],height[j])*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return rst