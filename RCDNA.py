#Reverse complement of DNA string
s="" #DNA string here
n=""#for the reverse complement of a DNA string
for i in range(0,len(s)):
    if s[i]=="T":
        n+="A"
    if s[i]=="A":
        n+="T"
    if s[i]=="G":
        n+="C"
    if s[i]=="C":
        n+="G"
print(n[::-1]) #Printing reverse complement of DNA string
