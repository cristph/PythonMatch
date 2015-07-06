class Solution():
    def ks_2samp(self, data1, data2):

        data1.sort()
        data2.sort()

        po1=[]
        po2=[]
        for i in range(0,len(data1)):
            fre=0.0
            for j in range(0,len(data2)):
                if(data2[j]<=data1[i]):
                    fre+=1
            po2.append(fre/len(data2))
            po1.append((1.0*i+1)/len(data1))

        po=[]
        for x,y in zip(po1,po2):
            po.append(abs(x-y))

        ks=max(po)
        return (round(ks,6))


                

s=Solution()
print s.ks_2samp([1,2,3,3,5,6],[1,2,3,4,4,8])