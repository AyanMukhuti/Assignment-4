import random
i=0
while i<10:
    i=i+1
    a,b=random.randint(1,10),random.randint(1,10)
    q1=print("Question number 1:",a,"x",b)
    res1=int(input("Enter result:"))
    if res1==a*b:
        print("Correct")
    else:
        print("Wrong")
