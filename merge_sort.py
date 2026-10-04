# Hospital Patient Record Sorting on the basis of age or patient ID
# By Divide and Conquer - Merge Sort

patients = [
    {"id":101,"name":"Rutuja","age":56},
    {"id":102,"name":"Rakhi","age":67},
    {"id":103,"name":"kai","age":34},
    {"id":104,"name":"swati","age":45},
    {"id":105,"name":"karishma","age":94}
]
# merge sort divide the list into smaller parts
def merge_sort(patients):

    #if there is only one patient
    if len(patients) <= 1:
        return patients
    
    #if there are multiple patients 
    mid = len(patients)//2

    #divide the list in two parts
    left = patients[:mid]#take the element from beginning exclude mid
    right = patients[mid:]#go from mid to end
    return merge(left,right)
    #Again we will use "mid" on left as well as right
    #bcoz we have to divide the list upto single element

    #lets sort left part and right part
    left = merge_sort(left)
    right = merge_sort(right)

#combine the two sorted parts
def merge(left,right):
    result = [] #stores the final sorted position
    i = 0 #position in left list
    j = 0 #stores the left list

    while i < len(left) and j < len(right):

        if left[i]["age"] <= right[j]["age"]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:]) 
    return result  

sorted_patients = merge_sort(patients)
print("patients sorted according to age:\n")

for patient in sorted_patients:
    print(patient["id"],patient["name"],patient["age"])
     