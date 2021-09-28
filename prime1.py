n1=int(input("enter the range"))
n2=int(input())
for num range(n1,n2+1):
    if(num>1):
        for i in range(2,num):
            if(num%i!=0):
                print(num)