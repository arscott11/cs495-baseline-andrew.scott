from utils import first_unique_char

def tests():
    test_cases = [
        ("leetcode", 0),
        ("lolwhato", 3),
        ("adadbcbbc", -1),
        ("Lolwhato", 2)
    ]

    for i in range(len(test_cases)):
        input_str, expected = test_cases[i]  
        result = first_unique_char(input_str)
        if result == expected:
            print(f"Test {i+1} passed")
        else:
            print(f"Test {i+1} failed: got {result}, expected {expected}")

tests()