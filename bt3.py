n=int(input("nhập số nguyên n:"))
a=0
if n>0:
 for i in range(1,n+1):
    b=n-i
    if i <=b:
        print(i ,"+",b)
        a+=1
print("số cách :" , a)
   