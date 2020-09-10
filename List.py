Lst = ["ranjan",1,2,3,4]#declaring list
print(Lst)
#output ['ranjan', 1, 2, 3, 4]

Lst.append("Infant")#Adding item to the last of the list
print(Lst)
#output ['ranjan', 1, 2, 3, 4, 'Infant']

lst = Lst.copy()#copying list items to another variable
print(lst)
#output ['ranjan', 1, 2, 3, 4, 'Infant']

lst.pop(0)#poping out item from the list at the index 0
print(lst)
#output [1, 2, 3, 4, 'Infant']

lst.reverse()#reversing the list items
print(lst)
#output ['Infant', 4, 3, 2, 1]

lst.clear()#Clearing entire list items
print(lst)
#output []
