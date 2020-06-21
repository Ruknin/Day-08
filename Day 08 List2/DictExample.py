Students = {'Ali':18,'Rahim':12,'Karim':22,'Joya':25}
print('All Item:')
print(Students)
print('Print by key Rahim :')
print(Students['Rahim'])

print(dir(Students))

#We use the method Students.update to
print('add Sarah to our existing dictionary')
Students.update({"Sarah":9})
print(Students)
print('if exist update dictionary')
Students.update({'Karim':12})
print(Students)

print('Delete by key :')
del Students['Ali']
print(Students)

print('Print Items :')
print("Students Name: %s" % Students.items())
print('Convet dic to list :')
print("Students Name: %s" % list(Students.items()))

print('Print Only Keys :')
for key in Students.keys():
    print(key)

print('Print Only Values :')
for val in Students.values():
    print(val)

print('Print Only Key and value :')
for key in Students.keys():
    print(key +"_"+str(Students[key]))

print("#Loop over items and unpack each item.")
for k, v in Students.items():
    # Display key and value
    print(k,v)