#find if function is inc/dec
#check if f(X0) is +/-
#use increaments accordingly to achieve brackets for roots

#def bracket(f, x0):
#	flag = True
#	x = x0
#	if f(x) > 0.0 :
#		xpos = x
#		ival = 1
#		x = x-0.1*x
#	else:
#		xneg = x
#		ival = -1
#		x = x+0.1*x
#	for i in range(1,51):
#		if f(x) > 0:
#			xpos = x
#			if ival == -1 :
#				flag = False
#				break
#			x = x - 0.1*x
#		else:
#			xneg = x
#			if ival == 1:
#				flag = False
#				break
#			x = x + 0.1*x
#	if flag == True:
#		print('havent got sign change')
#	return xpos, xneg



def f(x):
    return x*x -4
def nature(f,x):
    if(f(x+0.1)>f(x)):
        return 0.1
    else:
        return -0.1
def bracketing(f,x0):
    E=10e-5
    value=f(x0)
    a=False
    b=False
    if value>0:
        xp=x0
        xn=x0
        xin=nature(f,x0)
        for i in range(100):
            xn=xn-xin
            if(f(xn)<0):
                a=True
                break
        if(a==False):
            print("Unable to find root")
    if value<0:
        xn=x0
        xp=x0
        xin=nature(f,x0)
        for i in range(200):
            xp=xp+xin
            if(f(xp)>0):
                b=True
                break
        if(b==False):
            print("Unable to find root")
    if value==0:
        return x0,x0
    return xp,xn

def bisec (f,xp,xn):
    E=10e-5
    n=1000
    c=False
    if f(xp)*f(xn)<=0:
        x=(xp+xn)/2
        value=f(x)
        if(value==0):
            return x
        for i in range(n):
            x=(xp+xn)/2
            value=f(x)
           
            if(value>=E):
                xp=x
            else:
                xn=x
            if(abs(xp-xn)<E):   
                c=True
                return x
                break
        if c==False:
            print("Function not converging")
    else:
     print("Invalid input")         

x=float(input("Enter the value of x: "))    
xp,xn=bracketing(f,x)
print("The root is:",bisec(f,xp,xn))






"""
def f(x):
  return x**2+2*x+1
 
def inc_dec(f,x):
  if f(x+0.1*x)>f(x):
    return True #increasing
  else:
    return False #decreasing
   
def bracket(f,x):
  a=inc_dec(f,x)
  flag=True
  if a==True:
    if f(x)>0:
      xp=x
      for i in range(1,51):
        if f(x)>0:
          xp=x
        else:
          xn=x
          flag = False
          break       
        x-=0.1*x
    else:
      xn=x
      for i in range(1,51):
        if f(x)>0:
          xp=x
          flag = False
  				break 
        else:
          xn=x
        x+=0.1*x 
  else:
    if f(x)>0:
        xp=x
        for i in range(1,51):
          if f(x)>0:
            xp=x
          else:
            xn=x
            flag = False
  				  break 
          x+=0.1*x
      else:
        xn=x
        for i in range(1,51):
          if f(x)>0:
            xp=x
            flag = False
  				  break 
          else:
            xn=x
          x-=0.1*x 
  if flag == True:
		print('havent got sign change')        
  return xp,xn
     
       
a,b=bracket(f,4)
print([a,b])
       
"""