class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        months=[31,28,31,30,31,30,31,31,30,31,30,31]
        def convert(date):
            month,day=map(int,date.split("-"))
            return sum(months[:month-1])+day
        a1=convert(arriveAlice)
        a2=convert(leaveAlice)
        b1=convert(arriveBob)
        b2=convert(leaveBob)
        start=max(a1,b1)
        end=min(a2,b2)
        if start<=end:
            return end-start+1
        return 0        