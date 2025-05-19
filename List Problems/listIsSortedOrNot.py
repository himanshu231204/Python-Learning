ls=[1,2,7,10,4,5,9]

for i in range(len(ls)-1):
    if ls[i] < ls[i+1]:
        continue
        print("list is sorted")
    else:
        print("list is not sorted")
        break