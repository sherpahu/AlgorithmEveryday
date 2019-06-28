class Solution:
    def longestPalindrome(self, s: str) -> str:
        def kuosan(left,right,s):
            cnt=0
            left-=1
            right+=1
            while left>=0 and right<len(s) and s[left]==s[right]:
                cnt+=1
                left-=1
                right+=1
            return cnt
        left=0
        right=len(s)-1
        cnt=0
        flag=False
        for i in range(len(s)):
            len1=kuosan(i,i,s)
            #print(len1)
            if len1*2+1>cnt:
                flag=True
                left=i-len1
                right=i+len1
                cnt=right-left+1
                #print(cnt)
            if i+1<len(s) and s[i]==s[i+1]:
                len2=kuosan(i,i+1,s)
                #print(len2)
                if len2*2+2>cnt:
                    flag=True
                    left=i-len2
                    right=i+1+len2
                    cnt=right-left+1
        if flag:
            return s[left:right+1]
        else:
            return ""
            
            
        
        '''
        def isCycle(s):
            if len(s)==1 or len(s)==0:
                return True
            else:
                if s[0]==s[-1]:
                    return isCycle(s[1:-1])
                else:
                    return False
        uni=set(s)
        longest=''
        for substr in uni:
            lpos=s.find(substr)
            rpos=s.rfind(substr)
            if isCycle(s[lpos:rpos+1]) and (rpos+1-lpos)>len(longest):
                longest=s[lpos:rpos+1]
        return longest
        '''
        