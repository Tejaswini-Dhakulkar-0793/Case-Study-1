students=["priya","aarti","sneha","Durgesh"]
#priya is friend of aarti and sneha
#aarti is friend of priya and durgesh
#sneha is friend of priya and durgesh
#Durgesh is friend aari and sneha
#1=friend,0 = no friend
friendship=[
    [0,1,1,0],
    [1,0,0,1],
    [1,0,0,1],
    [0,1,1,0],
]

print("college friendship")

for i in range(4):
    print(students[i],":",friendship[i])
    
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

#at what index the name1 and name2 in student list
i = students.index(name1)
j = students.index(name2)

if friendship[i][j] == 1:
    print(name1,"and",name2,"are friends.")
else:
    print(name1,"and",name2,"are not friends.")    