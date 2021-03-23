##סעיף א
#פונקציית אקספוננט
def exponent (x):
    calc=x
    helper=1
    i=1
    e_x=x
    while i<150:
        calc=calc*x
        helper=helper*(i+1)
        e_x= e_x+calc/(helper)
        i=i+1
    e_x=e_x+1
    return e_x                 
# פונקצציית ln

def Ln(x):
    if x<=0:
        return 0.0
    y=0
    i=0
    while i<1000:
        y=y+2*(x-exponent(y))/(x+exponent(y))
        i=i+1
    return y
##פונקציית החזקה
def XtimesY(x, y):
    if x>0:
        soloution=float(exponent(float(y)*float(Ln(x))))
    else:
        soloution=0.0
    return float('%0.6f'%soloution)
##סעיף ב
##פונקציית שורש
def sqrt (x,y):
    if y<=0 or x==0:
        return 0.0
    x=1/x
    ans=XtimesY(y,x)
    return float('%0.6f'%ans)
##סעיף ג
def calculate(x):
    if x>=0:
        y=float(x)
        n=float((exponent(float(x))*XtimesY(7, float(x))*XtimesY(float(x), -1)*sqrt(float(y),float(x))))
    else:
        n=0
    return '%0.6f'%float(n)