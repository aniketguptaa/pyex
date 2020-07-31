# Open My existing file in which raw tags are stored
file = open('tagfile.txt', 'r')
content = file.read()

# Splitting the raw tags 
split_text = content.split('\n\n')

# Writing my raw tags to file with some operations
with open("tagsfile.txt",'w') as data:
    for tags in split_text:
        data.write(tags)
        data.write(",")
        data.write("\n")
data.close()