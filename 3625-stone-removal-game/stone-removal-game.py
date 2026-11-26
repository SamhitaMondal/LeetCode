class Solution:
    def canAliceWin(self, n: int) -> bool:
        remove=10
        turns=0
        while(n>=remove):
            n-=remove
            turns+=1
            remove-=1
        return turns%2==1
            