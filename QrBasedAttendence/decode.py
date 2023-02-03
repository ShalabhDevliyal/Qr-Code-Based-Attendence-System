import base64
import re   
fob=open('encoded.txt' ,'r')
nub = open('attendencelist.txt','w')
lines=fob.readlines() 
count=0
for i in lines:
    count+=1
    a = re.sub('b"b', '',i).replace('"','')
    decoded = base64.b64decode(a.strip()).decode('utf-8')
    nub.write(decoded+'\n')
    print("Student {}: {}".format(count, decoded))
fob.close()
nub.close()