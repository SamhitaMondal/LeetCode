class Solution:
    def checkString(self, s: str) -> bool:
        b_seen=False
        for i in s:
            if i=='b':
                b_seen=True
            elif i=='a' and b_seen:
                return False
        return  True      
