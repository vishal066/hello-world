mylist=[12,-7,5,64,-14]

i=0

while i<len(mylist):

    if mylist[i]<0:
        mylist.remove(mylist[i])

    i+=1

print(mylist)
