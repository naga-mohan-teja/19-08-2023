# selection sort
arr=[1,3,4,2,5,1,23,55,23]
n=len(arr)
for i in range(0,n-1):
    min_index=i
    for j in range(i+1,n):
        if arr[j]<arr[min_index]:
            min_index=j
    print(i,min_index)
    arr[i],arr[min_index]=arr[min_index],arr[i]
print(arr)
