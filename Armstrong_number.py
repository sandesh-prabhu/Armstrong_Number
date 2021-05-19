num=input("Enter a number:\n")
n=len(num)
num=int(num)
sum,temp=0,num
while temp>0:
    a=temp%10
    sum+=a**n
    temp//=10
if sum==num:
    print(num,"is an armstrong number.")
else:
    print(num,"is not an armstrong number.")
