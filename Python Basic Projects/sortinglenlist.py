liss=[[1,3,4,2],[3,2,58,18,75],[72,85,74,32,1,5,6],[62,3,85],[23],23,3,2,3,4,5,5]
lss=[]
def sort_(lss):
    return sorted(lss)
def sort_len(lss):
    lens=[]
    for i in lss:
        lens.append(len(i))
    return lens 
liss_out=[]
for i in liss:
    try:
        i=int(i)
        liss_out.append(i)
    except:
        lss.append(i)
liss_out.sort() 
ls=[]
for i in lss:
    ls.append(sort_(i))

sort_list=sort_len(ls)
inxx=0
temp=dict()
for i in sort_list:
    temp[i]=inxx
    inxx+=1
lz=[]
for i in temp.keys():
    lz.append(i)
lz.sort()
for i in lz:
    liss_out.append(ls[temp[i]])
print(liss_out)