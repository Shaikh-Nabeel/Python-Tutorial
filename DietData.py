# daily diet
inp_num = int(input("Enter 1 to delete all content\nEnter 2 to add more content\nEnter 3 to read all data: "))


def getdate():
    import datetime
    return datetime.datetime.now()


t = getdate()
global f0
if inp_num == 1:
    f0 = open("Nabs_Data.txt", "w")
    f0.write("")
    print("All content deleted successfully")
    f0.close()
elif inp_num == 2:
    f1 = open("Nabs_Data.txt", "a")
    inp = str(input("Enter what you eat today: "))
    f1.write("\n")
    f1.write(str(t))
    f1.write(" :\n")
    f1.write(str(inp))
    print("Successfully written")
    f1.close
elif inp_num == 3:
    f2 = open("Nabs_Data.txt", "r")
    print(f2.read())
    f2.close()
else:
    print("Error!: Not Valid Input")
