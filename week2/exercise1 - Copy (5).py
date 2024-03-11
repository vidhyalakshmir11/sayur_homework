
# Problem #4
# You are inviting 3 of your friends over to your house for watching a movie.
# You have a list of 5 movies you like. Ask each of your friends 5 movies they like.

# 1. List all the movies everyone likes
# 2. List only the movies you like but no one else likes
# 3. List the movies you like and at least one friend likes. Find which friend it is.
# 4. List the movies all your friends like but you don't like.

List_mine=["Harry Potter" ,"Avengers" , "Toy story " , "Zootopia"  , "Inside Out" ]
List_friends =[]
for i in range(3):
    Each_list =[]
    print("Enter the 5 movie")
    for j in range(5):
        Movie = input ()
        Each_list.append(Movie)
    List_friends.append(Each_list)

for i in range(4):
    Every_like =[]
    print("Enter the movie")
    for j in range(5):
        Movie = input ()
        Each_list.append(Movie)

# M1 yes yes yes yes   1 
# M2 yes no no no   2 
# M3 no no no no
# M4 yes no yes no 3 
# M5 no yes yes yes  4