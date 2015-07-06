#-*- coding:utf-8 -*-

from scipy.stats import f

class Solution():
    def f_oneway(slef,*args):

        m=len(args)
        if(m==0):
            return [None,None]

        for arg in args:
            if(len(arg)==0):
                return [None,None]

        #cal avg_array,all_avg
        avg_array=[]
        for arg in args:
            su=0.0
            for x in arg:
                su+=x
            avg=su/len(arg)
            avg_array.append(avg)

        print avg_array

        all_avg=0.0
        for a in avg_array:
            all_avg+=a
        all_avg=all_avg/len(avg_array)

        print all_avg

        #cal Sa,Se,St
        Sa=0.0
        for a in avg_array:
            t=(a-all_avg)**2
            Sa+=t
        Sa=Sa*len(args[0])

        Se=0.0
        i=0
        for arg in args:
            temp=avg_array[i]
            t=0.0
            for x in arg:
                t+=(x-temp)**2
            Se+=t
            i=i+1

        #cal fa,fe
        fa=m-1
        fe=m*len(args[0])-m

        #cal Va,Ve
        Va=Sa/fa
        Ve=Se/fe

        #cal Fa
        Fa=round(Va/Ve,6)
        p=round(f.sf(x=Fa,dfn=fa,dfd=fe),6)
        return [Fa,p]



s=Solution()
print s.f_oneway([1,2,3],[2,2,3])
#s.f_oneway([25.6,22.2,28.0,29.8],
           #[24.4,30.0,29.0,27.5],
           #[25.0,27.7,23.0,32.2],
           #[28.8,28.0,31.5,25.9],
           #[20.6,21.2,22.0,21.2])
#print f.sf(x=0.25,dfn=1,dfd=4)
