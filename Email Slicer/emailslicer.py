import re

read_file = open('testing.txt', 'r') # r = read the file
write_file = open("testing2.txt", 'w') # w for writing

f =read_file.readlines()

id = 0
for line in f:
    email = line.strip()
    new_list = re.split('\@|\.',email) # for multiple split
    user = "ID:" + str(id) + "\n" +"User name: "+new_list[0]+ "\n" +"Mail server: "+ new_list [1] + "\n" +"Domain: "+ new_list[2] +"\n" # formatting
    write_file.write(user)
    id+=1
