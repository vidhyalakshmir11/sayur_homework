
# *Homework-1:*
# Remove duplicates
# Input: helLo Hii
# Output: helo Hi

str = input("Enter any String :")
string = []
temp = ""
for i in str :   
        if i != " " : 
                if i.lower() not in temp :
                        string.append(i)
                        temp += i.lower() 
                else:
                        continue
        else:            
                string.append(i)
                temp = "" 
print("Removed duplicates :",''.join(string))