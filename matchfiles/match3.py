from scipy.stats import t

class Solution():
    def pearsonr(self,x,y):
        n=len(x)
        if(n==0):
            return [None,None]
        
        sum_x=sum(x)
        sum_y=sum(y)
        
        sum_xy=0.0
        sum_x2=0.0
        sum_y2=0.0
        for x,y in zip(x,y):
            sum_xy+=x*y
            sum_x2+=x**2
            sum_y2+=y**2
        
        z=((n*sum_x2-(sum_x)**2)*(n*sum_y2-(sum_y)**2))**0.5
        if(z==0):
            return [None,0]
        
        r=(n*sum_xy-sum_x*sum_y)/z
        if(abs(r)==1):
            return [r,0]
        
        tvalue=r*((n-2)/(1-r**2))**0.5
        p=2*t.sf(x=abs(tvalue),df=n-2)
        return (round(r,6),round(p,6))

s=Solution()
print s.pearsonr([1,2,3],[2,2,3])