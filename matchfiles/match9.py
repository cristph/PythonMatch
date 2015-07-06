import urllib
import json
from scipy.stats import chi2

class Solution():
    def solve(self):
        page=urllib.urlopen('http://112.124.1.3:8060/getData/101.json')
        c=page.read()
        data=json.loads(c)["data"]

        week1=0.0
        week1_2=0.0
        week2=0.0
        week2_2=0.0
        week3=0.0
        week3_2=0.0
        for x in data:
            y=x[2]
            if(y>5 and y<=10):
                y=y*4.33
            if(y>25 and y<=37):
                if(x[5]==1):
                    week1+=1
                else:
                    week1_2+=1
            elif(y>=38 and y<=40):
                if(x[5]==1):
                    week2+=1
                else:
                    week2_2+=1
            elif(y>=41 and y<49):
                if(x[5]==1):
                    week3+=1
                else:
                    week3_2+=1

        week=[week1,week2,week3]
        week_2=[week1_2,week2_2,week3_2]
        
        sum_week=sum(week)
        sum_week_2=sum(week_2)
        tot=sum_week+sum_week_2

        t11=(week1+week1_2)*sum_week/tot
        t12=(week2+week2_2)*sum_week/tot
        t13=(week3+week3_2)*sum_week/tot

        z1=(week1-t11)**2/t11
        z2=(week2-t12)**2/t12
        z3=(week3-t13)**2/t13

        x_2=z1+z2+z3
        p=chi2.sf(x=x_2,df=2)
        return (round(x_2,6),p)
        
       

s=Solution()
print s.solve()