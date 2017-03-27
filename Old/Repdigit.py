__author__ = 'Shashank'

#To get output Triangle like
#1
#22
#333
#444
#5555

for i in range(1,int(input())):
    print(i*(((10**i)-1)//9))

