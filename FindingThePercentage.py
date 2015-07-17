number = int(input())

dict = {}

for i in xrange(0,number):
    sentence = raw_input()
    sentence = sentence.split()
    dict[sentence[0]] = (float(sentence[1]) + float(sentence[2]) + float(sentence[3]))/3

search = raw_input()

total = float(dict[search])
print format(total,'0.2f')