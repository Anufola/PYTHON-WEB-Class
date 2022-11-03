file = open("myfile.txt", "r")
data = file.read()
data_ints = [ int(x) for x in data.split() ] 
print ("Largest element is:", max(data_ints))
# data_into_list = data.replace('\n', ' ').split(".")  
# Highscore = max(map(int, data_into_list))
# # nums = [int(num) for num in data_into_list]
# print("Largest element is:", max(Highscore))
# print( data_into_list[0])
# # data_into_list = data.replace('\n', ' ').split(".")  

# largest_elem = reduce(max, data_into_list)
# print(largest_elem)


# file = open("myfile.txt", "r")
# data = file.read()  

# lists = data.split(",")
# file.close()


# max = lists[0];    
# for i in range(0, len(lists)):    
#    if(lists[i] > max):    
#        max = lists[i];             
# print("Largest element present in given array: " + str(lists))