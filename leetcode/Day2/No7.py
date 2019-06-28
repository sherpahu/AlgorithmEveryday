class Solution:
    def reverse(self, x: int) -> int:
        s=''
        if x<0:
            s='-'
            x=-x
        absNumStr=str(x)
        rev=absNumStr[::-1]
        s+=rev
        num=int(s)
        if num<-1*2**31 or num>2**31-1:
            return 0
        else:
            return num
        