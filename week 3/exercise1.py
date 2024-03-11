
# *Homework-1:*
# Remove duplicates
# Input: hellllllo
# Output: helo

str = input("Enter any String :")
string = []
for i in str :
    if i  in string :
            continue 
    else : 
        string.append(i)
        
print("Removed duplicates :",''.join(string))
