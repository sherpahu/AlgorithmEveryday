class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)==0:
            return True
        stack=[]
        stack.append(s[0])
        for bracket in s[1:]:
            if bracket=='(' or bracket=='[' or bracket=='{':
                stack.append(bracket)
            elif bracket==')':
                if len(stack)==0 or stack.pop()!='(':
                    return False
            elif bracket==']':
                if len(stack)==0 or stack.pop()!='[':
                    return False
            elif bracket=='}':
                if len(stack)==0 or stack.pop()!='{':
                    return False
            else:
                return False
        if len(stack)!=0:
            return False
        return True