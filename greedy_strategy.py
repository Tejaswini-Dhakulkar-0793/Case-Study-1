# list of list = think like 2D array
#cause,we need 3 pieces of information for every event,["meeting a",9,10]->[meeting=name,9=start,10=end]
#you can access individual values by index
#event name + start time + end time
#list of list = array of array
#list of list(python)
#array of array(java/c)

Meetings = [
    ["meeting A" , 6, 7],
    ["meeting B", 6, 8],
    ["meeting C", 7, 9],
    ["meeting D", 8, 10],
]
#we have to sort the meetings according to ending time
#nested loop=>just to go with each and every element
for i in range(len(Meetings)):
    for j in range(i+1,len(Meetings)):
        if Meetings[i][2] > Meetings[j][2]:
            Meetings[i],Meetings[j] = Meetings[j],Meetings[i]

last_end = 0    
print("Scheduled Events")

for Meeting in Meetings:
    name = Meeting[0]
    start = Meeting[1]
    end = Meeting[2]

    if start >= last_end:
        print(name,":",start,"to",end)
        last_end = end