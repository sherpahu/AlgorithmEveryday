import re
class Solution:
    def myAtoi(self, str: str) -> int:
        numStr=re.findall(r'^[+-]?\d+',(str.strip()))
        try:
            return min(max(int(numStr[0]),-1*2**31),2**31-1)#numStr是一个list，int（）中只能传入str
        except: #有可能numStr为空，此时返回零，而不应该报错
            return 0