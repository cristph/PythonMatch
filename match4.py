from scipy.stats import t

class Solution():
    def ttest_1samp(self,a,popmean):
        if(len(a)==0):
            return [None,None]
        if(len(a)==1):
            return [None,None]

        #cal avg
        avg=0.0
        for x in a:
            avg+=x
        avg=avg/len(a)

        S=0.0
        for x in a:
            S+=(x-avg)**2
        S=(S/(len(a)-1))**0.5
        print S
        if(S==0):
            return [None,None]
        tvalue=(avg-popmean)/(S/(len(a)**0.5))
        if(tvalue>=0):
            p=t.sf(x=tvalue,df=len(a)-1)*2
            return [tvalue,p]
        else:
            p=2*t.sf(x=-tvalue,df=len(a)-1)
            return [tvalue,p]



s=Solution()
print s.ttest_1samp([1,2,3,5,6],3.5)