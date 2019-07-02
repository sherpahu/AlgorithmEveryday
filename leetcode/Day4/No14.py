import sys
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0:
            return ""
        l=sys.maxsize
        for s in strs:
            if l>len(s):
                l=len(s)
        for i in range(l):
            flag=True
            for s in strs:
                if strs[0][i]!=s[i]:
                    flag=False
                    break
            if flag==False:
                return s[:i]
        return s[:l]