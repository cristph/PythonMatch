import numpy as np
from pandas import Series
from scipy.stats import f

class Solution():
    def describe(self, a):
        if(len(a)==1):
            return [round(a[0],6),None,0,-3]

        su=0.000000
        for n in a:
            su=su+n
        mean=su/len(a)

        b2=0.000000
        b3=0.000000
        b4=0.000000
        for x in a:
            z=x-mean
            b2=b2+z**2
            b3=b3+z**3
            b4=b4+z**4
            
        b2=b2/len(a)
        b3=b3/len(a)
        b4=b4/len(a)
        
        var=b2*len(a)/(len(a)-1)
        skew=b3/(b2**1.5)
        kurt=b4/(b2**2)-3
        c=[round(mean,6),round(var,6),round(skew,6),round(kurt,6)]
        return c

m=Solution()
a=[1]
#print np.mean(a)
#print np.var(a)
#print m.describe(a)
#print f.sf(x=0.25, dfn=1, dfd=4)
print m.describe([1.1,2.2,3.3,4.4,5.6])