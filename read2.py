# file = open("myfile.txt", "r")
# data = file.read()
# data_ints = [ int(x) for x in data.split() ] 
# print ("Largest element is:", max(data_ints))
# file.close()

# Correction

# method 2

# reading all lines from the file and storing in the variable



# convert the data to a list of string
# data_int = [int(x) for x in read_data.split()]

#print the maximum number in the list
#print(max(data_int))


# print(read_data)

file = open("myfile.txt", "r")
read_data =file.read()
read_data = read_data.split()
highest = int(read_data[0])
for line in read_data:
    int_item = int(line)
    if(highest < int_item):
       highest = int_item

print( 'highest value is', highest)