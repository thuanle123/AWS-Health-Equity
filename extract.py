import pandas as pd
import string
import csv
from textwrap import wrap
from threading import Thread

#ntee_whitelist = ["B21",B28,B6,B7,B9,C2,D2,E2,E3,E4,E5,E6,E7,E8,E9,F2,F3,F4,F5,F6,F7,F8,F9,G2,G3,G4,G5,G6,G7,G8,G9,I2,I5,I6,I7,I8,J2,J3,K3,K4,K5,L2,L3,L4,L8,M2,N2,N3,O2,O3,P2,P3,P4,P5,P6,P7,P8,P99,R2,R3,R6,W3,W4,W5,W8,W9,X2,X3,X4,X5,X7,X9]
#activity_whitelist = [001,031,032,061,126,150,152,153,154,155,156,158,160,165,166,179,261,296,297,320,322,323,325,326,327,328,321,324,349,351,380,381,382,383,384,401,406,407,430,431,432,449,460,461,462,463,560,561,562,563,564,565,566,567,568,569,572,573,574,900,902,907,913,915,916,917,990]

ntee_whitelist = []
activity_whitelist = []
all_activity = []
holding = []

def ntee_processing():
    f = open("ntee_whitelist.csv")
    for row in csv.reader(f):
        for item in row:
            N = 1
            if len(item) == 2:
                # This loop add 0 into two character NTEE CODE, along with all its subcategories
                # B6 will be B60, B61
                for i in range(0, 9):
                    res = item.ljust(N + len(item), str(i))
                    ntee_whitelist.append(res)
            ntee_whitelist.append(item)
    f.close()

def activity_processing():
    f = pd.read_csv("BMF.csv")
    all_activity_filter = f['ACTIVITY']
    all_activity_filter.to_csv("all_activity.csv", index=False)
    f = open("all_activity.csv")
    next(f,None)
    for row in csv.reader(f):
        for item in row:
            N = 1
            if len(item) == 7:
                N += 1
                res = item.rjust(N + len(item), '0')
                all_activity.append(res)
            if len(item) == 8:
                res = item.rjust(N + len(item), '0')
                all_activity.append(res)
            if len(item) == 9:
                all_activity.append(item)
    f.close()
    f = open("activity_whitelist.csv")
    for row in csv.reader(f):
        for item in row:
            activity_whitelist.append(item)
    for i in range(len(all_activity)):
        for j in range(len(activity_whitelist)):
            wrapper = wrap(all_activity[i], 3)
            whitelist = activity_whitelist[j]
            if whitelist == wrapper[0] or whitelist == wrapper[1] or whitelist == wrapper[2]:
                if all_activity[i] not in holding:
                    holding.append(all_activity[i])
    remove_leading_zero = [i.lstrip('0') for i in holding]
    f.close()

    # Cannot put this in a function because remove_leading_zero is a local variable
    f = pd.read_csv("BMF.csv")
    keep_col = ['EIN', 'NAME', 'STREET', 'CITY', 'ZIP', 'ACTIVITY', 'NTEE_CD', 'REVENUE_AMT']
    new_f = f[keep_col]
    ntee_filter = new_f[new_f['NTEE_CD'].isin(ntee_whitelist)]
    ntee_filter.to_csv("ntee_filter_BMF.csv", index=False)
    activity_filter = new_f[new_f['ACTIVITY'].isin(remove_leading_zero)]
    activity_filter.to_csv("activity_filter_BMF.csv", index=False)

if __name__ == '__main__':
    t1 = Thread(target = ntee_processing)
    t2 = Thread(target = activity_processing())
    t1.setDaemon(True)
    t2.setDaemon(True)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
