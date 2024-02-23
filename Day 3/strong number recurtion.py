def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
def strong(x):
    s=str(x)
    sum=0
    for i in s:
        sum+=factorial(int(i))
    if sum == x:
        return "strong number"
    else:
        return "not a strong number"
x=int(input())
print(strong(x))
