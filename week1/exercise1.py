# Generate the following output using for loop. Go until g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba
# look at the output and find the pattern. Hint - add next letter in the alphabet in each row

string = "abcdefg" #assign a to g in an variable 
temp = "a" # assign temp variable for store  previous step for next row

for i  in range(len(string)): # loop the string a to g 
    if string[i] != string[0]: 
        print(f"{temp}{string[i]}{temp}")
        temp += string[i]+ temp  # append the  previous step for next row
    else:
        print(temp)
    