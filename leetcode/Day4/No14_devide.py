class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def commonLongestPrefix(left,right):
            length=min(len(left),len(right))
            for i in range(length):
                if left[i]!=right[i]:
                    return left[:i]
            return left[:length]
        def longestCommonPrefix(strs,start,end):
            if start==end:
                return strs[start]
            else:
                mid=(start+end)//2
                left_longest=longestCommonPrefix(strs,start,mid)
                right_longest=longestCommonPrefix(strs,mid+1,end)
                return commonLongestPrefix(left_longest,right_longest)
        if strs==None or len(strs)==0:
            return ""
        return longestCommonPrefix(strs,0,len(strs)-1)
#分治，但是速度比之前的暴力法慢