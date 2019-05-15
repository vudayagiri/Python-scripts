#! /usr/bin/env python3

mylist = [20,30,45,34,56,67,56,45,25,19,18,78,57]
b= len(mylist)-1
c = d = e = f = 0
for a in range(b):

    if mylist[a] <= 20:
        c += 1

    elif mylist[a] <= 35:
        d += 1

    elif mylist[a] <= 45:
        e += 1

    else:
        f += 1

    a=a+1
    #print(a)
foo = open("condition.txt", "w")
print(f"There are {c} workers, {d} mills, {e} golfers and {f} retirees in the list", file=foo)
foo.close()



