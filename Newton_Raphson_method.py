#trying to approach root by incrementng
#Xn+1=Xn-f(x)/f'(x)
#in secant method: put f'(x)=f(Xn)-f(Xn-1)/(Xn)-(Xn-1)
#use error limit E=1e-5
#p may be multiplied to increment as damping factor
#def nr(f,f',Xo,E,n)
#def sec(f,Xo,E,n)

def f(x):
  return x**2+2*x+1
  
def fx(x):
  return 2*x+2
    
def nr(f,fx,x,E=1e-5,n=100):
  xp=0
  flag=True
  for i in range(n):
    if abs(x-xp)<E:
      flag = False
      break
    else:
      xp=x        
      x-=(f(x)/fx(x))
  if flag == True:
    print('havent got root under desired error limits')
  else:         
    print('root by NR method is:',x) 
    return x
  
x=float(input('enter value of x:'))
nr(f,fx,x)