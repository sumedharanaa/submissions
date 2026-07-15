class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d = {}
        def res(amt):
            if amt in d: return d[amt]
            if amt == 0: return 0
            if amt < 0: return 1e9
            total_min = float('inf')
            for i in coins:
                #if this coin is picked
                total_min = min(total_min, 1 + res(amt - i))
            d[amt] = total_min
            return total_min
        answer = res(amount)
        if answer > 1e8: return -1
        return answer
