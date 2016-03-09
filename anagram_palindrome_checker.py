def finder(input):
    """
    HackerRank: Algorithms::Strings::Game of Thrones - I
    Checks if 'input' has an anagram which is a palindrome
    """
    lst = [0] * 26

    for i in range(0, len(input)):
        char_index = ord(input[i]) - ord('a')
        lst[char_index] += 1

    count = 0

    for i in range(0, len(lst)):
        if lst[i] % 2 == 1:
            count += 1

    if count > 1:
        return "NO"
    else:
        return "YES"

print finder(raw_input())
