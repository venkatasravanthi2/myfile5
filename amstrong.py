num=int(input())
temp=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+rem**3
    num=num//10
if(temp==sum):
    print("yes")
else:
    print("no")
