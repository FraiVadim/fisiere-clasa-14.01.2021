with open ('input.txt',"r") as f:
    a=f.readline()
for i in a:
    if ((ord(i))>64) and ((ord(i))<91):
        with open('litereA.txt',"w") as f:
            f.write(str(i))
for m in a:
    if ((ord(m))>96) and ((ord(m))<123):
        with open('litereB.txt',"w") as f:
            f.write(str(m))
for c in a:
    if ((ord(c))>47) and ((ord(c))<58):
        with open('cifre.txt',"w") as f:
            f.write(str(c))            
for o in a:
    if (((ord(o))>41) and ((ord(o))<46)) and (((ord(o))>57) and ((ord(o))<63)):
        with open('operatori.txt',"w") as f:
            f.write(str(o))