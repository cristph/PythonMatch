import urllib
import json
from scipy.stats import norm

class Solution():
    def solve(self):
        page=urllib.urlopen('http://112.124.1.3:8050/getData/101')
        c=page.read()
        data=json.loads(c)["data"]

        week=[]
        y=0.0
        for x in data:
            y=x[2]
            if(y>5 and y<=10):
                y=y*4.33
                week.append(y)
            elif(y>25 and y<49):
                week.append(y)

        avg=sum(week)/len(week)
        theta=4.0
        z=1.96
        k=(theta/(len(week)**0.5))*z
        min=avg-k
        max=avg+k
        return [round(min,6),round(max,6)]

s=Solution()
print s.solve()