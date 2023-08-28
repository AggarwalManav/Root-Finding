def f(x):
  return x**3

print('function is x**3:')

  
def bisec(a,b,E=1e-5,n=200):
  c=True
  if f(a)*f(b)<0:
    for i in range(n):
      c=(a+b)/2
      if f(c)>0:
        a=c
      else:
        b=c
      if abs(b-a)<E:
        return c
        c=False
        break
    if c==True:
	    print('convergence not possible')

  else:
    print('invalid input') 

a=float(input('enter x+ :'))
b=float(input('enter x- :'))
print('approximate root is:',bisec(a,b))
