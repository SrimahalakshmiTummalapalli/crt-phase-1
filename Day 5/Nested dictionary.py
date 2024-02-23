n=int(input("Enter No of students:"))
m=int(input("Enter No of subjects:"))
d={}
for i in range(n):
    k=input("Enter rollno:")
    v={}
    for j in range(m):
        sub=input("Enter subject name:")
        marks=int(input("Enter marks:"))
        v[sub]=marks
    d[k]=v
for i in d:
    print(i,"=",d[i])
