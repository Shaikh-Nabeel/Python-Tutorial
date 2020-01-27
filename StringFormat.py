# String formatting in python

me = "Nabs"
a1 = 3

# a = "this is %s %s"% (me, a1)
# print(a)

# a= "this is {1} {0}"
# b= a.format(me, a1)
# print(b)

a = f"this is {me} {a1} {4*40}"
print(a)


def printjoke(str):
    print(f"this is joke {str}")


""" 
if we insert this line before any program and this file will imported any another file, that file will ignore this
line and execute other content of this file.
"""
if __name__ == '__main__':
    print(printjoke("ha ha ha ha"))
