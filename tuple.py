tupl = ("Ranjan","a","a","Infant")#declaring tuple
print(tupl)
#output ('Ranjan', 'a', 'Infant')

#since tuple is immutable we have only two methods 
print(tupl.count("a"))#Returns the number of times a specified value occurs in a tuple
#output 2

print(tupl.index("Infant"))#Searches the tuple for a specified value and returns the position of where it was found
#output 3