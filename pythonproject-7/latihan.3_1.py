import random
n=int(input("Masukan nilai n :"))
a=0
for x in range (n):
    i=random.uniform(.0,.5)
    a+=1
    print ("data ke :" ,a ,"==>",i)