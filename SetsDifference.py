number1 = int(raw_input())
set1 = raw_input()
number2 = int(raw_input())
set2 = raw_input()

set1 = set1.split()
set1 = list(map(int,set1))
set1 = set(set1)

set2 = set2.split()
set2 = list(map(int,set2))
set2 = set(set2)

diff1 = set1.difference(set2)
diff2 = set2.difference(set1)

final_set = diff1.union(diff2)
final_set = list(final_set)
final_set.sort()

for i in range(0,len(final_set)):
    print final_set[i]