from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        big = 0
        small = 0
        while small < len(temperatures):
            if temperatures[small] < temperatures[big]:
                small += 1
                continue
            

        return answer



        