class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_finish(k):
            return sum([ceil(pile / k) for pile in piles]) <= h

        left = ceil(sum(piles) / h)
        right = max(piles)
        if can_finish(left):
            return left

        while left <= right:
            mid = (left + right) // 2
            if can_finish(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
        