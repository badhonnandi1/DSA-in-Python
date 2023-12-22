arr = [2,4,3,2,6,4,2]

max_value = max(arr)

newarray = [0]*(max_value+1)

for i in arr:
    newarray[i] += 1

def search(newarray,elem):
    if elem<len(newarray):
        if newarray[elem] != 0:
            return True
        else:
            return False
    else:
        return False
print(newarray)
sorted_array = []
for i in range(len(newarray)):
    if newarray[i] != 0:
        for j in range(newarray[i]):
            sorted_array.append(i)

print(sorted_array)

#--------------------------------------------------------------------------------------------

main = [2,-3,-1,1,3]
minval = min(main)
for i in range(len(main)):
    main[i] = main[i]-minval

auxilaryArrlen = max(main) + abs(min(main)) + 1
# print(main)
auxilaryArray = [0]*auxilaryArrlen
for i in main:
    auxilaryArray[i] +=1

# print(auxilaryArrlen)
# print(auxilaryArray)
def search(elem,arr):
    idx = elem - minval
    if arr[idx] != 0:
        return True
    else:
        return False
# print(search(2,auxilaryArray))
sorted = []
for i in range(len(auxilaryArray)):
    if auxilaryArray[i] != 0:
        for j in range(auxilaryArray[i]):
            sorted.append(i+minval)
print(sorted)
