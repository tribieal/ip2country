import os

def getPrefix(a,n):
    tlist=a.split(".")
    res=""
    for i in range(n-1):
        res+=tlist[i]+"."
    res+=tlist[n-1]
    return res

def myTrim(ip):
    tlist=ip.split(".")
    while "0" in tlist:
        tlist.remove("0")
    res=".".join(tlist)
    return res

tmp=open("ip2country.txt","r").read()
lines=tmp.split("\n")

countryMap={}
for line in lines:
    i=line.split("|")
    if len(i)!=7:continue
    i.append(9999.9)
    i.append(0.0)
    i.append(0)
    i.append(0)
    countryMap[ myTrim(i[3]) ]=i



tmp=open("speedrate.txt","r").read()
lines=tmp.split("\n")


for line in lines:
    i=line.split(" ")
    if len(i)!=2:continue
    ip=i[0]
    if len(ip) <= 0 : continue
    if len(i[1]) > 0:
        ms=float(i[1].strip()[:-2])
    for j in [4,3,2,1]:
        tip=getPrefix(ip,j)
        if tip in countryMap:
            omin=countryMap[tip][7]
            omax=countryMap[tip][8]
            countryMap[tip][7]=min(omin,ms)
            countryMap[tip][8]=max(omax,ms)
            countryMap[tip][9]+=ms
            countryMap[tip][10]+=1
            break
        
print '1|2|3|4|5|6|7|8|9|10|11|12'
for i in countryMap:
    if countryMap[i][7]==9999.9:
        continue
        countryMap[i][7]="NaN"
    else:
        countryMap[i][7]=str(countryMap[i][7])
    if countryMap[i][8]==0.0:
        countryMap[i][8]="NaN"
    else:
        countryMap[i][8]=str(countryMap[i][8])
    
    countryMap[i].append(str(countryMap[i][9]/countryMap[i][10]))

    countryMap[i][9]=str(countryMap[i][9])
    countryMap[i][10]=str(countryMap[i][10])
    print '|'.join(countryMap[i])
                
        
        
        
