num=int(input("Enter number:"))
if num>1:
    for i in range(2,num//2):
        if(num%i==0):
            print(num,"is not a Prime number")
            break
    else:
            print(num,"is a Prime number")
else:
    print(num,"is not a Prime number")
