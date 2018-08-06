# open unsorted_fruits.txt file for reading
infile = open("unsorted_fruits.txt", "r")

# open sorted_fruits.txt file for writing
outfile=open("sorted_fruits.txt","w")

# read fruit names
fruits=infile.readlines()

# sort fruit names in alphabetic order
fruits.sort()
for fruit in fruits:
    if fruit != '\n':
        # write sorted fruit names to sorted_fruits.txt
        outfile.write(fruit)

# close unsorted_fruits.txt file
infile.close()
# close sorted_fruits.txt file
outfile.close()