class Employee:
    no_of_leaves = 8
    pass

harry = Employee()
nabs = Employee()

harry.name = "Harry"
harry.salary = 455
harry.role = "Instructor"

nabs.name = "Nabs"
nabs.salary = 455
nabs.role = "Student"
print(Employee.no_of_leaves)

print(nabs.__dict__)

# nabs can't change the no_of_leaves because it is object only class can change
nabs.no_of_leaves = 9
print(Employee.no_of_leaves)
print(nabs.__dict__)
# nabs.no of leaves is added as variable instead of changing the main class data

Employee.no_of_leaves =10
print(nabs.no_of_leaves)

