def gcd(res,n):
    while n:
        res,n=n,res%n
    return res
res=0
while True:
    n=int(input())
    if n==-1:
        break
    if res==0:
        res=n
    newgcd=gcd(res,n)
print(newgcd)
