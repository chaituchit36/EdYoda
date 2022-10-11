x=int(input("enter the value of x:"))
n=int(input("enter the value of n:"))
class power:
    def pow(self,x,n):
        if x==0 or x==1 or n==1:return x
        if n==0: return 1
        if x<0:
            y=(-1)*x
            if n%2==0: return self.pow(y,n)
            else:return -self.pow(y,n)
        if n<0:
            return 1/self.pow(x,-n)
        val=self.pow(x,n//2)
        if n%2==0:
            return val*val
        return val*val*x

p=power()
print(p.pow(x,n))                  