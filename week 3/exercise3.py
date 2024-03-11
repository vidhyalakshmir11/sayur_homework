
# *Homework-3:*
# Get an input string from the user. Add a space at every 3rd char.
# Input: abcdefg
# Output: ab cd ef g
# vi dy al a
# 0123456789  -  2 5 8 11

String = input("Enter any string:")
str = ""  
for i in range(len(String)):
    if  i %2 == 0 and i!=0 : # index position not 0 and its modulo by 2 remainder should be == 0 
        str += " "
    str += String[i]
print(str)

