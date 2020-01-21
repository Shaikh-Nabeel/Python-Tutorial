# "r" open file for reading - default
# "w"open file for writing
# "x" creates file if not exist
# "a" add more content to a file
# "t" text mode  - default
# "b" binary mode
# "+" read and write

# fL =open("ShaikhNabs.txt", "r")

# with open("shaikhNabs.txt") as f:
#     a= f.read(5)
#     print(a)
# f.close()

# content =fL.read(5)
# content =fL.read(10)
# print(content)
# print(fL.tell())
# print(fL.readline())
# print(fL.tell())
# # this line pin the pointer on given value
# fL.seek(46)
this is dev branch
# print(fL.readline())
# print(fL.tell())
# print(fL.readlines())

# fL = open("nabsN.txt", "a")
# fL.write("\n hey, this line is inserted by python users")
# fL.close()

fL = open("nabsN.txt", "r+")
print(fL.read())
fL.write("\nThank You Python ")
fL.close()
