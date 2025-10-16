# read
# file = open("new.txt",'r')
# print(file.read())

# file = open("new.txt",'r')
# print(file.readline())
# print(file.readlines())
# print(file.read())

# write 

# file = open("new.txt",'w')
# # file.write("Created bt today")
# file.writelines(["Created by today\n","This new page"])
# print("Text added succesfully")

# append
# file = open("new.txt",'a')
# file.write("\n Today is thursday")
# print("Text added succesfully")

# file.close()


with open("new.txt","r") as f:    
    print(f.seek(2))
    print(f.tell())
    print(f.read())
