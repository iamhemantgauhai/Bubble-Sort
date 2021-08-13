t= int(input())

a = [] 

for i in range(1,t+1):
    N = int(input())
    a.append(N)

c = len(a)

while c> 1:
    for j in range(c-1) :
        if a[j]>a[j+1] :
            a[j],a[j+1] = a[j+1],a[j]
            
    else:
        c -=1

for n in a :
    print(n)