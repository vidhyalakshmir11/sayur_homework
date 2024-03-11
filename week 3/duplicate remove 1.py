
# *Homework-1:*
# Remove duplicates
# Input:helLo Hii
# Output: helLo Hi

str = input("Enter any String :")
string = []
temp = "" # empty string 
for i in str :   
        if i != " " : # not a space 
                if i not in temp : # character not in temp  
                        string.append(i)
                        temp += i # add to the string
                else:
                        continue
        else:            
                string.append(i)
                temp = "" 
print("Removed duplicates :",''.join(string))