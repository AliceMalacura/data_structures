#list
my_subjects = ["circuits", "electronics", "logic circuits", "d.e", "numeth"]

#access/edit an item in the list
print("The First item in the list is " + my_subjects[0])

#to replace an item in the list
my_subjects[1] = "envi engg"
print("The second item in the list now is " + my_subjects[1])

#to add and item in the list
my_subjects.append("data structures and algorithm analysis")
print ("my subjects now are " + str(my_subjects[0:6])) #now, data structures and algorithm analysis is added to the last part of the list

#to remove an item in the list
my_subjects.remove("d.e")
print("I removed d.e in the list of items... so my subjects now are " + str(my_subjects))


#tuple
my_subjects = ("circuits", "electronics", "logic circuits", "d.e", "numeth")
print("Im removing entire tuple")
del my_subjects
print(my_subjects) #to prove that i cant print my_subject anymore because i deleted it



