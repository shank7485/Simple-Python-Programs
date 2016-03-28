"""
HackerRank: Algorithms::Strings::Two Strings
"""


def checker(string1, string2):
    lst1 = [0]*26
    lst2 = [0]*26

    flag = False

    for char in string1:
        lst1[ord(char) - ord('a')] += 1

    for char in string2:
        lst2[ord(char) - ord('a')] += 1

    for i in range(0, len(lst1)):
        if lst1[i] and lst2[i] != 0:
            flag = True
            break

    if flag == True:
        print "YES"
    else:
        print "NO"
        
        
N = int(raw_input())
for i in xrange(N):
    string1 = raw_input()
    string2 = raw_input()
    checker(string1, string2)
