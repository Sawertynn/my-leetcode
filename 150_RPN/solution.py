"""
Note that:

    The valid operators are '+', '-', '*', and '/'.
    Each operand may be an integer or another expression.
    The division between two integers always truncates toward zero.
    There will not be any division by zero.
    The input represents a valid arithmetic expression in a reverse polish notation.
    The answer and all the intermediate calculations can be represented in a 32-bit integer.
"""

from typing import List


class Solution:
    operands = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: int(a / b),
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip("+-").isnumeric():  # isnumeric doesn't work with negatives
                stack.append(int(token))
                continue

            if token in self.operands:
                right = stack.pop()
                left = stack.pop()
                val = self.operands[token](left, right)
                stack.append(val)

        return stack.pop()
