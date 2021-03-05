def trapezoidePuntos(X,Y):
    I=0
    for h in range(len(X)-1):
        semiI=(X[h+1]-X[h])*(Y[h+1]+Y[h])/2
        I+=semiI
    return I

def trapezoideAnonima(a,b,f,e):
    density=e/100
    I=0
    spacing=(b-a)*density
    xvalue=a
    yvalue=0
    X=[]
    Y=[]
    for m in range(int(1/density)):
        xvalue+=spacing
        yvalue=f(xvalue)
        X.append(xvalue)
        Y.append(yvalue)
    for h in range(len(X)-1):
        semiI=(X[h+1]-X[h])*(Y[h+1]+Y[h])/2
        I+=semiI
    return I

#X=[1,2,3,4,5]
#Y=[2,4,6,8,10]
#I=trapezoidePuntos(X,Y)
a=0
b=50
e=1
f=lambda t: -0.001*t+10
#f=lambda t: t
I=trapezoideAnonima(a,b,f,e)
print(I)
