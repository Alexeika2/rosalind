s=" " #DNA line here
cA=0
cC=0
cG=0
cT=0
for n in s:
    if n=="A":
        cA+=1
    elif n=="C":
        cC+=1
    elif n=="G":
        cG+=1
    elif n=="T":
        cT+=1
print(cA,cC,cG,cT)

        
