from solution import Solution

s = Solution()

def test_case_1():
    banned = [1, 6, 5]
    n = 5
    maxSum = 6
    val = s.maxCount(banned, n, maxSum)
    print(val)

def test_case_2():
    banned = [11]
    n = 7
    maxSum = 50
    val = s.maxCount(banned, n, maxSum)
    print(val)

test_case_1()
test_case_2()