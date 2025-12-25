class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        a = 0
        dec = 0

        happiness.sort(reverse=True)
        for i in range(k):
            a += max(0, happiness[i]-dec)
            dec += 1

        return a
