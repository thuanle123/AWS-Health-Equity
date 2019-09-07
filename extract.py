import pandas as pd
import string
import csv

#ntee_whitelist = ["B21",B28,B6,B7,B9,C2,D2,E2,E3,E4,E5,E6,E7,E8,E9,F2,F3,F4,F5,F6,F7,F8,F9,G2,G3,G4,G5,G6,G7,G8,G9,I2,I5,I6,I7,I8,J2,J3,K3,K4,K5,L2,L3,L4,L8,M2,N2,N3,O2,O3,P2,P3,P4,P5,P6,P7,P8,P99,R2,R3,R6,W3,W4,W5,W8,W9,X2,X3,X4,X5,X7,X9]
#activity_whitelist = [001,031,032,061,126,150,152,153,154,155,156,158,160,165,166,179,261,296,297,320,322,323,325,326,327,328,321,324,349,351,380,381,382,383,384,401,406,407,430,431,432,449,460,461,462,463,560,561,562,563,564,565,566,567,568,569,572,573,574,900,902,907,913,915,916,917,990]

ntee_whitelist = []
activity_whitelist = []


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


#f = open("activity_whitelist.csv")
#for row in csv.reader(f):
#    for item in row:
#        activity_whitelist.append(item)



f = pd.read_csv("BMF.csv")
keep_col = ['EIN', 'NAME', 'STREET', 'CITY', 'ZIP', 'ACTIVITY', 'NTEE_CD', 'REVENUE_AMT']
new_f = f[keep_col]
ntee_filter = new_f[new_f['NTEE_CD'].isin(ntee_whitelist)]
ntee_filter.to_csv("ntee_filter_BMF.csv", index=False)


