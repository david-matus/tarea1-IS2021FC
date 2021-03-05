import math

def newtonR(f,df,tol,xi):
    numIt=0
    e=100
    x=xi
    while e>tol and numIt<200:
        a=x
        x=a-f(a)/df(a)
        if x==0:
            e=abs(a-x)*100
        else:
            e=abs(a-x)*100/x
        numIt+=1
    return x

f=lambda t: 0.01/2*(t**2)-5
df= lambda t: 0.01*t
tol=1
xi=1
r=newtonR(f,df,tol,xi)
print(r)
