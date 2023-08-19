l=[2,3,1,3,2]
d={}
n=len(l)
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)
# d=sorted(d.items(),key=lambda item: item[0])
# d={k:v for k,v in sorted(d.items(),key=lambda item: item[0] ,reverse = True)}# this line is used if you want to sort d.keys from higer to lower i.e reverse order 
sorted_dict = [k  for k, v in sorted(d.items(), key=lambda item: item[1])  for i in range(v)] #if items[0] means keys and items[1] means values
print(sorted_dict)
