from utils import first_unique_char


def tests():
    test1 = "leetcode"
    test2 = "Lolwhato"
    test3 = "adadbcbbc"
    expected1 = 0
    expected2 = 1
    expected3 = -1

    test1Result = first_unique_char(test1)
    if (test1Result == expected1):
        print("Test 1 passed")
    else: print("Test 1 failed")

tests()