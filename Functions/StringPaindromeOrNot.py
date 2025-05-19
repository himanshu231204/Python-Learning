def pallindrome(st):
    rev=""
    for i in range(len(st)-1,-1,-1):
        rev=rev +st[i]

    if rev==st:
        print("pallindROME")
    else:
        print("not a pallindroem")   

pallindrome("Himanshu")
pallindrome("NARAN")

