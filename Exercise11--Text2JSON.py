# when you have 1 statement data 
# Python program to convert text 
# file to JSON 


# import json 


# # the file to be converted to 
# # json format 
# filename = 'data.txt'

# # dictionary where the lines from 
# # text will be stored 
# dict1 = {} 

# # creating dictionary 
# with open(filename) as fh: 

# 	for line in fh: 

# 		# reads each line and trims of extra the spaces 
# 		# and gives only the valid words 
# 		command, description = line.strip().split(None, 1) 

# 		dict1[command] = description.strip() 

# # creating json file 
# # the JSON file is named as test1 
# out_file = open("test1.json", "w") 
# json.dump(dict1, out_file, indent = 4, sort_keys = False) 
# out_file.close() 



# Python program to convert text 
# file to JSON 


import json 


# the file to be converted 
filename = 'sample1.txt'

# resultant dictionary 
dict1 = {} 

# fields in the sample file 
fields =['name', 'designation', 'age', 'salary'] 

with open(filename) as fh: 
	

	
	# count variable for employee id creation 
	l = 1
	
	for line in fh: 
		
		# reading line by line from the text file 
		description = list( line.strip().split(None, 4)) 
		
		# for output see below 
		# print(description) 
		
		# for automatic creation of id for each employee 
		sno ='emp'+str(l) 
	
		# loop variable 
		i = 0
		# intermediate dictionary 
		dict2 = {} 
		while i<len(fields): 
			
				# creating dictionary for each employee 
				dict2[fields[i]]= description[i] 
				i = i + 1
				
		# appending the record of each employee to 
		# the main dictionary 
		dict1[sno]= dict2 
		l = l + 1


# creating json file		 
out_file = open("test2.json", "w") 
json.dump(dict1, out_file, indent = 4) 
out_file.close() 
print('your json file is created')


