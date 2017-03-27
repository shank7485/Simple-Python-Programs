__author__ = 'Shashank'

number = int(input())

dict = {}
#lst = []

for i in range(0,number):
    sentence = input()
    sentence = sentence.split()
    dict[sentence[0]] = int(sentence[1]) + int(sentence[2]) + int(sentence[3])

search = input()

print(dict[search])

if search in dict:
    print('Average of %s is %d' % (search,((dict[search])//3)))
else:
    print('%s not found' %(search))



