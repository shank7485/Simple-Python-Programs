# Enter your code here. Read input from STDIN. Print output to STDOUT

num = int(raw_input())
num_string = raw_input()
num_string = num_string.split()
T = ()
T = list(T)

for i in xrange(0,num):
     T.append(int(num_string[i]))

T = tuple(T)
print hash(T)