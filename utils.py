def first_unique_char(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for i in range(len(counts)):
        if counts[i] == 1:
            return i
    
    return -1
