n=int(input())
rev=0
for i in range(n):
    if n > 0:
         digit=n%10
         rev=rev*10+digit
         n//=10
    else:
        break
print(rev)
