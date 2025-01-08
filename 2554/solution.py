from typing import List

class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        counted = 0
        total = 0
        for i in range(1, maxSum):
            if i in banned:
                continue
            if total + i > maxSum or counted == n:
                break
            total = total + i
            counted += 1
        return counted