from scipy.stats import chi2

class Solution:
    def independence_test(self, A):
        if(len(A)==0):
            return [None.None]
        if(len(A)==1):
            return [0.0,None]

        rows=[]
        columns=[]

        #ini rows
        for row in A:
            r_sum=0.0
            for r in row:
                r_sum+=r
            rows.append(r_sum)

        #ini columns
        for i in range(0,len(A[0])):
            c_sum=0.0
            for row in A:
                c_sum+=row[i]
            columns.append(c_sum)

        tot=sum(rows)

        #cal Ma1
        Ma_1=[]
        for i in range(0,len(rows)):
            row=[]
            for j in range(0,len(columns)):
                T=rows[i]*columns[j]/tot
                row.append(T)
            Ma_1.append(row)

        #cal Ma2
        Ma_2=[]
        for i in range(0,len(rows)):
            row=[]
            for j in range(0,len(columns)):
                Z=(A[i][j]-Ma_1[i][j])**2/Ma_1[i][j]
                row.append(Z)
            Ma_2.append(row)

        #cal X_2
        X_2=0.0
        for x in Ma_2:
            for y in x:
                X_2+=y

        #cal c
        print X_2
        print tot
        c=(X_2/(X_2+tot))**0.5
        print c
        #cal p
        p=chi2.sf(x=X_2,df=(len(rows)-1)*(len(columns)-1))

        return [round(X_2,6),round(p,6)]

s=Solution()
#s.independence_test([[186,38,35],
                     #[227,54,45],
                     #[219,78,78],
                     #[355,112,140],
                     #[653,285,259]])
print s.independence_test([[1,2,3],[2,2,3]])
#print chi2.sf(x=20.09,df=8)