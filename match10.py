import urllib
import json

class Solution:
    def solve(self):
        page=urllib.urlopen('http://112.124.1.3:8060/getData/101.json')
        c=page.read()
        data=json.loads(c)["data"]

        weight=[]
        age=[]

        for x in data:
            w=x[4]
            a=x[6]
            weight.append(w)
            age.append(a)

        sum_x=sum(age)
        sum_y=sum(weight)
        
        sum_xx=0.0
        for x in age:
            sum_xx+=x**2

        sum_xy=0.0
        for x,y in zip(age,weight):
            sum_xy+=x*y

        lxy=sum_xy-sum_x*sum_y/len(age)
        lxx=sum_xx-sum_x**2/len(age)

        b=lxy/lxx
        a=1.0*sum_y/len(weight)-b*sum_x/len(age)
        avg_y=1.0*sum_y/len(age)

        Sr=0.0
        St=0.0
        for x,y in zip(age,weight):
            y_=a+b*x
            Sr+=(y_-avg_y)**2
            St+=(y-avg_y)**2
        print avg_y
        print Sr
        print St
        r2=Sr/St
        return [round(a,6),round(b,6),round(r2,6)]

age=[255.7,263.3,275.4,278.3,296.7,309.3,315.8,318.8,330.0,340.2,350.7,367.3,381.3,406.5,430.8,451.5]
weight=[116.5,120.8,124.4,125.5,131.7,136.2,138.7,140.2,146.8,149.6,153.0,158.2,163.2,170.5,178.2,185.9]
s=Solution()
print s.solve()