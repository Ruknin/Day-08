students = [
    {'Id':1, 'Name':'Nazmul','salary':360},
    {'Id':2, 'Name':'Saiful','salary':450},
    {'Id':3, 'Name':'Atiq','salary':789},
    {'Id':4, 'Name':'Monjur','salary':600}
]
students = {'ID':[1,2,3,4],'Name':['Nazmul','Saiful','Atiq','Monjur'],'Salary':[360,450,789,600]}
for x in zip(*([key] + (value) for key, value in sorted(students.items()))):
    print(*x)
