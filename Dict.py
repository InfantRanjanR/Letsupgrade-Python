dit = {"name":"Infant Ranjan R","designation":"Student","year":"4th year"}#declaring Dictionaries
print(dit)
#output {'name': 'Infant Ranjan R', 'designation': 'Student', 'year': '4th year'}

di=dit.get("name")
print(di)#prints the item present in that key
#output Infant Ranjan R

dit.pop("name")#item with key name is poped out
print(dit)
#output {'designation': 'Student', 'year': '4th year'}

d = dit.values()#gets values
print(d)
#output dict_values(['Student', '4th year'])

di = dit.keys()#prints keys used
print(di)
#output dict_keys(['designation', 'year'])

dit.clear()#clears everything
print(dit)
#output {}