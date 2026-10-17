class Solution:
    def elevatorRequests(self, n: int, requests: list[int]) -> int:
        lift=0
        ans=0
        for i in requests:
            lift=abs(i-lift)
            ans+=lift
            lift=i
        return(ans)