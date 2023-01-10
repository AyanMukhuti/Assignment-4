num=int(input("Enter marks:"))
if num<0 or num>100:
    print("Enter valid marks.")
else:
    if num<25:
        print("Grade=F")
    if num<=45 and num>25:
        print("Grade=E")
    if num<=50 and num>45:
        print("Grade=D")
    if num<=60 and num>50:
        print("Grade=C")
    if num<=80 and  num>60:
        print("Grade=B")
    if num>80:
        print("Grade=A")
