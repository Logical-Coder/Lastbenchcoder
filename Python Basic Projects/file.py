#This Code Creates New CSV file add heading with Name Mobile Number Age and Adresss
inp=int(input("Number of Members:"))
liss=['Name','Mobile Number','Age',"Address"]

f = open ('myfile.csv','a')
k = open ('myfile.csv','r')
lss=""
for n in k:
    lss+=n
if lss.startswith("Name"):
    print("")
else:
    for i in liss:
        f.write(i+',')
    f.write('\n')

for i in range(0,inp):
    
    for j in range(0,len(liss)):
        f.write(str(input("Enter Your "+liss[j]+":")+','))
    f.write('\n')
f.close()


    

        
        
        
            
    

