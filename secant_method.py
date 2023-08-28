#trying to approach root by incrementng
#Xn+1=Xn-f(x)/f'(x)
#in secant method: put f'(x)=f(Xn)-f(Xn-1)/(Xn)-(Xn-1)
#use error limit E=1e-5
#p may be multiplied to increment as damping factor
#def nr(f,f',Xo,E,n)
#def sec(f,Xo,E,n)

def f(x):
  return x**2+2*x+1
    
def sec(f,x,E=1e-5,n=100):
  x0=x
  x1=x-0.1*x
  flag=True
  for i in range(n):
    fx=(f(x1)-f(x))/(x1-x)
    if abs(x-x1)<E:
      flag = False
      break
    else:
      x1=x        
      x-=f(x)/fx
  if flag == True:
    print('havent got root under desired error limits')
  else:         
    print('root by secant method is:',x) 
    return x
  
x=float(input('enter value of x:'))
sec(f,x)