from scipy.stats import norm

class Solution():
    def solve(self,a,b):
        array=norm.rvs(size=1000000)
        num=0.0
        for x in array:
            if x>=a:
                if x<=b:
                    num+=1
        return num/1000000

s=Solution()
print s.solve(0.5,0.7)