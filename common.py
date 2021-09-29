def common(a,b):
    a1=set(a)
    b1=set(b)
    if(a1&b1):
        print(a1 & b1)
    else:
        print("no common elements")
a1= [1,1,2,3,5,8,13,21,34,55,89]
b1= [1,2,3,4,5,6,7,8,9,10,11,12,13]
common(a1,b1)