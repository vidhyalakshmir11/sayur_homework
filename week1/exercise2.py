
# you have a list of student names and another list with their marks in CS. 
# hard code the values. no need to get it as input
# Pass mark is 50.
# Print a new list with all the students with pass marks along with their mark in the format name:mark.Also print the number of students who failed.

# list name,mark
# pass mark 50
# check and print 
names = ["vidya","robert","harry","ron","jack"] # create name list
marks = [ 100,40,89,50,45] # create mark list
count = 0 # initialize count of failed students as 0
pass_student = {} # create dictionary for store name : mark of passed students
for mark in range(len(marks)) :
    if marks[mark] >= 50 :  # check passsed students as above 50
        pass_student[names[mark]]= marks[mark]
    else: # increment 1 
        count+=1
print("Total no.of failed :",count)
for key,value in pass_student.items():
    print(f"{key} {value} " )