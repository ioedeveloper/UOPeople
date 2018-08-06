infile = open("unsorted_fruits.txt", "r")
outfile=open("sorted_fruits.txt","w")

fruits=infile.readlines()
fruits.sort()
for fruit in fruits:
    if fruit != '\n':
        outfile.write(fruit)
        
infile.close()
outfile.close()